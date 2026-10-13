# 💰 Expense Tracker Dashboard

A simple **Python Expense Tracker web application** built using **Streamlit, SQLite, and Pandas**.

The application allows users to add daily expenses, store them permanently in a SQLite database, filter expenses, view spending summaries and charts, download expense data as a CSV file, and delete incorrect expenses.

---

## ✨ Features

* ✅ Add new expenses
* ✅ Store expenses in SQLite database
* ✅ Select expense category
* ✅ Add optional notes
* ✅ Select expense date
* ✅ Filter expenses by month
* ✅ Filter expenses by category
* ✅ Filter expenses by minimum amount
* ✅ View total amount spent
* ✅ View number of expenses
* ✅ View average expense
* ✅ Display expense records in a table
* ✅ View spending by category
* ✅ View monthly spending trend
* ✅ Download expense data as CSV
* ✅ Delete an expense
* ✅ Simple and beginner-friendly interface

---

## 🛠️ Technologies Used

* **Python** – Main programming language
* **Streamlit** – Used to create the web dashboard
* **SQLite** – Used to store expense data
* **Pandas** – Used for reading, filtering, and analyzing expense data

---

## 📂 Project Structure

```text
expense-tracker/
│
├── app.py
├── expenses.db
├── requirements.txt
└── README.md
```

### File Description

**`app.py`**

Contains the complete application:

* Streamlit interface
* SQLite database connection
* Database table creation
* Add expense function
* Get expenses function
* Delete expense function
* Filtering
* Calculations
* Charts
* CSV download

**`expenses.db`**

SQLite database that stores the expense records.

**`requirements.txt`**

Contains the Python libraries required to run the application.

**`README.md`**

Contains information about the project and how to run it.

---

## 🗄️ Database

The application uses **SQLite** to store expense information.

The `expenses` table contains:

| Column     | Description                |
| ---------- | -------------------------- |
| `id`       | Unique ID for each expense |
| `amount`   | Amount spent               |
| `category` | Expense category           |
| `note`     | Optional description       |
| `date`     | Date of the expense        |

The table is automatically created when the application starts.

---

## 📊 Dashboard

The dashboard provides a summary of the expenses.

### Expense Summary

It displays:

* **Total Spent**
* **Number of Expenses**
* **Average Expense**

For example:

```text
Total Spent       Number of Expenses       Average Expense
₹5,000             10                       ₹500
```

---

## 🔎 Expense Filters

Users can filter their expenses using:

### 1. Month

Select a particular month such as:

```text
2026-01
2026-02
2026-03
```

### 2. Category

Available categories:

```text
Food
Travel
Shopping
Entertainment
Health
Other
```

### 3. Minimum Amount

Users can enter a minimum amount to display only expenses above that amount.

For example:

```text
Minimum Amount = ₹500
```

will display expenses of ₹500 or more.

---

## 📈 Charts

The dashboard contains two simple charts.

### Spending by Category

Shows how much money was spent in each category.

Example:

```text
Food             ₹2,000
Travel           ₹3,000
Shopping         ₹1,500
```

### Monthly Spending

Shows the total spending for each month.

Example:

```text
2026-01     ₹3,000
2026-02     ₹4,500
2026-03     ₹2,500
```

---

## 📥 Download Expense Data

Users can download the filtered expense data as a **CSV file**.

The downloaded file can be opened using:

* Microsoft Excel
* Google Sheets
* Python
* Other spreadsheet applications

---

## 🗑️ Delete Expense

Each expense has a unique ID.

The user can enter the expense ID and click **Delete Expense** to remove it from the database.

For example:

```text
Expense ID: 5
```

The application searches for that ID and deletes the corresponding expense.

**Note:** Deleted expenses cannot be recovered.

---

## 🚀 Installation

### Step 1: Create a project folder

```bash
mkdir expense-tracker
cd expense-tracker
```

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

### Step 3: Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS/Linux

```bash
source .venv/bin/activate
```

### Step 4: Install the required libraries

```bash
pip install streamlit pandas
```

---

## ▶️ Run the Application

Run:

```bash
streamlit run app.py
```

The application will open in your web browser.

Usually, Streamlit runs at:

```text
http://localhost:8501
```

---

## 🔄 Application Flow

The basic working flow of the application is:

```text
User
  ↓
Streamlit Interface
  ↓
Enter Expense
  ↓
Python Function
  ↓
SQLite Database
  ↓
Read Expense Data
  ↓
Pandas DataFrame
  ↓
Filter and Analyze Data
  ↓
Dashboard
  ├── Summary
  ├── Expense Table
  ├── Category Chart
  └── Monthly Chart
```

---

## 🧠 Python Concepts Used

This project is designed using basic Python concepts such as:

* Variables
* `if` conditions
* `for` loops
* Functions
* Lists
* Dictionaries
* SQL queries
* Pandas DataFrames

Example of a simple function:

```python
def add_expense(amount, category, note, date):
    connection.execute(
        "INSERT INTO expenses (amount, category, note, date) VALUES (?, ?, ?, ?)",
        (amount, category, note, date)
    )
    connection.commit()
```

---

## 🔐 Data Storage

The application uses SQLite, so the expense data is stored locally in:

```text
expenses.db
```

The data remains available even after closing the Streamlit application.

---

## 📌 Notes

* All expense amounts are stored as numbers in SQLite.
* No currency conversion is performed.
* Expenses are stored locally in the SQLite database.
* Deleted expenses cannot be recovered.
* The CSV download contains the currently filtered expense data.
* The database is automatically created when the application runs.

---

## 🎯 Purpose of the Project

The purpose of this project is to build a simple real-world application using Python.

It demonstrates how Python can be used together with:

```text
Python
   +
SQLite
   +
Pandas
   +
Streamlit
```

to create a useful data-tracking and visualization application.
