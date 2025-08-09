import os
import pandas as pd
from dbfread import DBF
import re

# Use current folder as base
base = "."

def mask_value(val):
    """Mask CNIC, phone, email, otherwise return as-is."""
    if not isinstance(val, str):
        return val

    # CNIC pattern (Pakistan)
    if re.match(r"^\d{5}-\d{7}-\d$", val):
        return val[:6] + "******-" + val[-1]

    # Phone numbers (7+ digits)
    if re.match(r"^\+?\d[\d\s-]{6,}$", val):
        digits = re.sub(r"\D", "", val)
        if len(digits) >= 7:
            return digits[:4] + "*" * (len(digits) - 4)

    # Email addresses
    if "@" in val:
        parts = val.split("@")
        if len(parts[0]) > 3:
            return parts[0][:3] + "***@" + parts[1]
        else:
            return "***@" + parts[1]

    return val

dbf_files = []
for root, dirs, files in os.walk(base):
    for f in files:
        if f.lower().endswith(".dbf"):
            dbf_files.append(os.path.join(root, f))

print(f"Found {len(dbf_files)} DBF files.")

schemas = []
samples = {}

for fp in dbf_files:
    rel = os.path.relpath(fp, base)
    print("Processing:", rel)
    try:
        table = DBF(fp, encoding="latin1", ignore_missing_memofile=True)
        fields = [(fld.name, fld.type, fld.length, getattr(fld, "decimal_count", None)) for fld in table.fields]
        schemas.append({"table": rel, "fields": fields})

        # First 5 rows only, with masking
        sample_rows = []
        for i, rec in enumerate(table):
            if i >= 5:
                break
            row = {}
            for k, v in rec.items():
                if v is None:
                    row[k] = ""
                else:
                    row[k] = mask_value(str(v))
            sample_rows.append(row)
        samples[rel] = sample_rows
    except Exception as e:
        print("  ERROR reading table:", e)
        schemas.append({"table": rel, "fields": f"Error: {e}"})
        samples[rel] = []

# Save schema
schema_rows = []
for s in schemas:
    if isinstance(s["fields"], list):
        for fld in s["fields"]:
            schema_rows.append({
                "table": s["table"],
                "field_name": fld[0],
                "type": fld[1],
                "length": fld[2],
                "decimals": fld[3]
            })
    else:
        schema_rows.append({
            "table": s["table"],
            "field_name": s["fields"],
            "type": "",
            "length": "",
            "decimals": ""
        })

schema_df = pd.DataFrame(schema_rows)
schema_out = os.path.join(".", "foxpro_schema.csv")
schema_df.to_csv(schema_out, index=False, encoding="utf-8-sig")
print("Wrote schema to", schema_out)

# Save masked samples
for table, rows in samples.items():
    safe_name = table.replace(os.sep, "_").replace("/", "_")
    if rows:
        out_csv = os.path.join(".", f"sample_{safe_name}.csv")
        pd.DataFrame(rows).to_csv(out_csv, index=False, encoding="utf-8-sig")
        print("Wrote sample ->", out_csv)

print("✅ Done! All sensitive data masked in sample files.")
