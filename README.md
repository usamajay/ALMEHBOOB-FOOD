# ALMEHBOOB FOOD ERP (Legacy FoxPro to Cloud Migration)

## 📌 Overview
This repository contains the **legacy FoxPro ERP system** (`ALMEHBOOB FOOD`) currently used by local businesses in Pakistan, migrated here for **modernization into a full-stack, online ERP**.  
The original system was **on-premise** with local servers; this migration aims to enable **anytime, anywhere access** with **cloud hosting**.

## 📂 Contents
- **Original FoxPro Project Files**
  - `.DBF` — Database tables
  - `.FPT` — Memo files
  - `.CDX` — Indexes
  - `.PRG` — Source programs
  - `.SCX` / `.FRX` — Forms and reports
- **Schema Extracts**
  - `foxpro_schema.csv` — All tables and field structures
  - `sample_*.csv` — Masked sample rows for each table

⚠️ **Note:** All sample data is masked — CNIC, phone numbers, and email addresses have been anonymized for security.

## 🏗 Modern ERP Requirements
The new ERP should:
- Be **web-based** (React/Next.js frontend + Node.js/Python backend)
- Store data in **PostgreSQL/MySQL** with migration scripts from `.DBF`
- Include **user authentication**, **role-based access**, and **audit logging**
- Be **mobile-friendly** and **responsive**
- Support **real-time data sync** for multiple branches
- Include **report generation** in PDF/Excel
- Have **inventory**, **sales**, **purchases**, **accounts**, **payroll**, **HR**, and **production modules**
- Support **barcode scanning**, **POS system**, and **multi-currency**
- Implement **localization** for Urdu/English

## 🛠 How Schema Was Extracted
We used a Python script (`extract_dbf_schema.py`) with `dbfread` and `pandas` to:
1. Read `.DBF` tables
2. Extract structure into `foxpro_schema.csv`
3. Save **masked sample data** into `sample_*.csv`

## 🚀 Migration Plan
1. Analyze `foxpro_schema.csv` for table relationships
2. Create PostgreSQL schema from legacy tables
3. Build REST/GraphQL API
4. Rebuild UI in React/Next.js
5. Migrate data via ETL scripts
6. Deploy to cloud (AWS, Azure, or local provider)

---

### 📧 Contact
For migration inquiries, contact:
**Owner:** _Hasee_  
**Location:** Pakistan
