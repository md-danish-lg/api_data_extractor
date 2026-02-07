

# API Data Extractor

## 📌 Intro
This Python tool fetches data from a public REST API,
processes nested JSON responses,
and exports the cleaned data into CSV and Excel files. 

## 🚀 Features
- Fetches data from a REST API
- Handles JSON arrays and nested fields
- Extracts selected fields into tabular format
- Exports data to:
  - CSV (.csv)
  - Excel (.xlsx)
- Basic error handling for file saving
- Console status messages for easy monitoring

## 🛠 Requirements
- Python 3.8+
- requests
- pandas
- openpyxl

## 📦 Installation
1. Clone or download this repository
2. Create and activate a virtual environment (recommended)
3. Install dependencies:

```
pip install requests pandas openpyxl
```

## ▶️ How to Run
Run the script using:

```
python extract.py
```

## 📄 Output
After successful execution, the following files will be created in the project folder:

- users.csv
- users.xlsx

Each file contains:
- User ID
- Username
- Email
- City
- Company Name

## 🧩 Use Cases
- Converting API data to Excel for business analysis
- Automating data collection tasks
- Creating reports from REST APIs
- Preparing datasets for non-technical users

## 🧪 Example
The script fetches user data from:

https://jsonplaceholder.typicode.com/users

And converts it into structured spreadsheet files.
link can be changed to use any api that doesnt use authenticatio

## ⚠️ Notes
- Make sure output files are not open in Excel while running the script
- Internet connection is required
- The API endpoint can be changed to any compatible REST API

