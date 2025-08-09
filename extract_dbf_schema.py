import os
import re
import pandas as pd
from dbfread import DBF

# Paths
project_path = r"C:\Users\hasee\OneDrive\Desktop\ALMEHBOOB-FOOD"
output_schema_file = os.path.join(project_path, "foxpro_schema.csv")
output_samples_folder = project_path

# Patterns to detect sensitive data
cnic_pattern = re.compile(r"\b\d{5}-\d{7}-\d\b")
phone_pattern = re.compile(r"\b(?:\+92|0)\d{9,10}\b")
name_keywords = ["name", "customer", "client"]  # columns that may have names
address_keywords = ["address", "addr", "location"]

# Store schema
schema_records = []

print("🔍 Starting FoxPro DBF schema extraction and masking...\n")

# Process each DBF
for root, _, files in os.walk(project_path):
    for file in files:
        if file.lower().endswith(".dbf"):
            dbf_path = os.path.join(root, file)
            table_name = os.path.basename(dbf_path)
            print(f"📂 Processing table: {table_name}")

            try:
                table = DBF(dbf_path, ignore_missing_memofile=True)

                # Schema info
                for field in table.fields:
                    schema_records.append({
                        "table": table_name,
                        "field_name": field.name,
                        "field_type": field.type,
                        "field_length": field.length,
                        "field_decimal_count": field.decimal_count
                    })

                # Load sample data
                df = pd.DataFrame(iter(table))
                print(f"   ➡ Loaded {len(df)} records")

                # Mask sensitive fields
                for col in df.columns:
                    col_lower = col.lower()

                    # Mask CNIC and phone numbers
                    df[col] = df[col].astype(str).apply(
                        lambda x: cnic_pattern.sub("XXXXX-XXXXXXX-X", x)
                    )
                    df[col] = df[col].apply(
                        lambda x: phone_pattern.sub("0XXXXXXXXXX", x)
                    )

                    # Mask names
                    if any(keyword in col_lower for keyword in name_keywords):
                        df[col] = "Name Hidden"

                    # Mask addresses
                    if any(keyword in col_lower for keyword in address_keywords):
                        df[col] = "Address Hidden"

                # Save masked sample
                sample_file_path = os.path.join(
                    output_samples_folder,
                    f"sample_{table_name}.csv"
                )
                df.head(20).to_csv(sample_file_path, index=False, encoding="utf-8-sig")
                print(f"   ✅ Sample saved: {sample_file_path}")

            except Exception as e:
                print(f"   ❌ Error reading {table_name}: {e}")

# Save schema
pd.DataFrame(schema_records).to_csv(output_schema_file, index=False, encoding="utf-8-sig")
print(f"\n✅ Extraction complete.\nSchema saved to: {output_schema_file}")
print("📁 Sample CSV files saved in the project folder.")
