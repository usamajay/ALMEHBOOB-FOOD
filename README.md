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
**Owner:** _Usama_  
**Location:** Pakistan

# PROMPT

I have uploaded my existing FoxPro ERP system to GitHub here: https://github.com/usamajay/ALMEHBOOB-FOOD.git

This system is currently used in a local-server setup in Pakistan and I want it rebuilt as a modern, online, full-stack ERP system that can be accessed anytime from anywhere.

Please replicate the functionality of the existing system while using modern, scalable technologies such as:
- Backend: Node.js (Express) or Python (FastAPI/Django)
- Frontend: React (Next.js) or Vue.js
- Database: PostgreSQL or MySQL
- Hosting: Cloud-ready (AWS, Azure, GCP, or DigitalOcean)
- Authentication: JWT-based login with role-based access control

The ERP must include:
1. Inventory management with stock in/out, wastage tracking, and supplier records
2. Sales and purchase modules with invoice generation
3. Accounts & ledgers with daily, monthly, and yearly financial reports
4. Customer management (CRM) with contact info and history
5. Supplier and vendor management
6. Multi-user access with admin/user permissions
7. Product categories, units, and pricing management
8. Support for Urdu/local language alongside English
9. Export of reports in PDF and Excel formats
10. Cloud backup and restore system
11. Dashboard with KPIs (sales, inventory alerts, top customers, outstanding balances)
12. Mobile-friendly responsive design
13. Search and filter options in all modules
14. Option for multi-branch support in the future

I have also included a Python script (`extract_dbf_schema.py`) that reads the DBF database files, outputs schema information, and generates masked sample CSVs so you can understand the table structures without exposing private customer data.

Please:
- Analyze the database schema from the provided samples.
- Map the existing fields to the new database design.
- Migrate the data from DBF to a modern SQL database.
- Build all modules with the same or improved workflows.

End goal: A web-based ERP accessible via browser, hosted online, secure, and optimized for low-bandwidth environments in Pakistan.
