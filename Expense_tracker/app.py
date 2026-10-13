import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# DATABASE
# ---------------------------------------------------------

connection = sqlite3.connect("expenses.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    note TEXT,
    date TEXT
)
""")

connection.commit()


# ---------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------

def add_expense(amount, category, note, date):

    query = """
    INSERT INTO expenses (amount, category, note, date)
    VALUES (?, ?, ?, ?)
    """

    connection.execute(
        query,
        (amount, category, note, date)
    )

    connection.commit()


def get_expenses():

    query = "SELECT * FROM expenses ORDER BY date DESC"

    data = pd.read_sql(query, connection)

    return data


def delete_expense(expense_id):

    query = "DELETE FROM expenses WHERE id = ?"

    connection.execute(
        query,
        (expense_id,)
    )

    connection.commit()


# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="📊",
    layout="wide"
)


# ---------------------------------------------------------
# SIDEBAR - ADD EXPENSE
# ---------------------------------------------------------

st.sidebar.title("➕ Add Expense")

st.sidebar.write(
    "Enter your expense details below."
)

amount = st.sidebar.number_input(
    "Amount",
    min_value=0.0,
    step=10.0
)

category = st.sidebar.selectbox(
    "Category",
    [
        "Food",
        "Travel",
        "Shopping",
        "Entertainment",
        "Health",
        "Other"
    ]
)

note = st.sidebar.text_input(
    "Note (Optional)"
)

date = st.sidebar.date_input(
    "Date"
)


if st.sidebar.button(
    "➕ Add Expense",
    use_container_width=True
):

    if amount <= 0:

        st.sidebar.error(
            "Amount must be greater than zero."
        )

    else:

        add_expense(
            amount,
            category,
            note,
            str(date)
        )

        st.sidebar.success(
            "Expense added successfully!"
        )

        st.rerun()


# ---------------------------------------------------------
# MAIN TITLE
# ---------------------------------------------------------

st.title("📊 Expense Tracker Dashboard")

st.write(
    "Track, manage, and understand your daily spending."
)


# ---------------------------------------------------------
# GET EXPENSES
# ---------------------------------------------------------

df = get_expenses()


if len(df) == 0:

    st.info(
        "No expenses recorded yet. "
        "Add your first expense from the sidebar."
    )

else:

    # -----------------------------------------------------
    # CREATE MONTH COLUMN
    # -----------------------------------------------------

    df["month"] = pd.to_datetime(
        df["date"]
    ).dt.strftime("%Y-%m")


    # -----------------------------------------------------
    # FILTER EXPENSES
    # -----------------------------------------------------

    st.subheader("🔎 Filter Expenses")

    col1, col2, col3 = st.columns(3)


    # Month
    with col1:

        months = ["All"]

        for month in df["month"].unique():

            months.append(month)

        selected_month = st.selectbox(
            "Select Month",
            months
        )


    # Category
    with col2:

        categories = ["All"]

        for category_name in df["category"].unique():

            categories.append(category_name)

        selected_category = st.selectbox(
            "Select Category",
            categories
        )


    # Minimum amount
    with col3:

        minimum_amount = st.number_input(
            "Minimum Amount",
            min_value=0.0,
            step=10.0
        )


    # -----------------------------------------------------
    # APPLY FILTERS
    # -----------------------------------------------------

    filtered_data = df.copy()


    if selected_month != "All":

        filtered_data = filtered_data[
            filtered_data["month"] == selected_month
        ]


    if selected_category != "All":

        filtered_data = filtered_data[
            filtered_data["category"] == selected_category
        ]


    if minimum_amount > 0:

        filtered_data = filtered_data[
            filtered_data["amount"] >= minimum_amount
        ]


    # -----------------------------------------------------
    # EXPENSE SUMMARY
    # -----------------------------------------------------

    st.subheader("🎯 Expense Summary")


    total = filtered_data["amount"].sum()

    number_of_expenses = len(filtered_data)


    if number_of_expenses > 0:

        average = total / number_of_expenses

    else:

        average = 0


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "💰 Total Spent",
            f"₹{total:,.2f}"
        )


    with col2:

        st.metric(
            "🧾 Number of Expenses",
            number_of_expenses
        )


    with col3:

        st.metric(
            "💵 Average Expense",
            f"₹{average:,.2f}"
        )


    # -----------------------------------------------------
    # EXPENSE RECORDS
    # -----------------------------------------------------

    st.subheader("📋 Expense Records")


    if len(filtered_data) == 0:

        st.warning(
            "No expenses match the selected filters."
        )

    else:

        table = filtered_data[
            [
                "id",
                "amount",
                "category",
                "note",
                "date"
            ]
        ]

        st.dataframe(
            table,
            use_container_width=True,
            hide_index=True
        )


    # -----------------------------------------------------
    # ANALYTICS
    # -----------------------------------------------------

    st.subheader("🧮 Analytics")


    chart1, chart2 = st.columns(2)


    # -----------------------------------------------------
    # BAR CHART
    # -----------------------------------------------------

    with chart1:

        st.write("### 📊 Spending by Category")


        if len(filtered_data) > 0:

            category_data = (
                filtered_data
                .groupby("category")["amount"]
                .sum()
            )


            categories_for_chart = []
            amounts_for_chart = []


            for category_name in category_data.index:

                categories_for_chart.append(
                    category_name
                )

                amounts_for_chart.append(
                    category_data[category_name]
                )


            fig, ax = plt.subplots(
                figsize=(6, 3.5)
            )


            ax.bar(
                categories_for_chart,
                amounts_for_chart
            )


            ax.set_title(
                "Spending by Category"
            )

            ax.set_xlabel(
                "Category"
            )

            ax.set_ylabel(
                "Amount (₹)"
            )


            plt.xticks(
                rotation=30
            )

            plt.tight_layout()

            st.pyplot(fig)

            plt.close(fig)


    # -----------------------------------------------------
    # MONTHLY LINE CHART
    # -----------------------------------------------------

    with chart2:

        st.write("### 📈 Monthly Spending")


        if len(filtered_data) > 0:

            monthly_data = (
                filtered_data
                .groupby("month")["amount"]
                .sum()
                .sort_index()
            )


            months_for_chart = []
            amounts_for_chart = []


            for month in monthly_data.index:

                months_for_chart.append(
                    month
                )

                amounts_for_chart.append(
                    monthly_data[month]
                )


            fig, ax = plt.subplots(
                figsize=(6, 3.5)
            )


            ax.plot(
                months_for_chart,
                amounts_for_chart,
                marker="o"
            )


            ax.set_title(
                "Monthly Spending"
            )

            ax.set_xlabel(
                "Month"
            )

            ax.set_ylabel(
                "Amount (₹)"
            )


            plt.xticks(
                rotation=30
            )

            plt.tight_layout()

            st.pyplot(fig)

            plt.close(fig)


    # -----------------------------------------------------
    # DELETE EXPENSE
    # -----------------------------------------------------

    st.divider()

    st.subheader("🗑️ Delete an Expense")

    st.write(
        "Select an expense that you want to remove."
    )


    expense_options = []


    for index, row in df.iterrows():

        text = (
            str(row["id"])
            + " - "
            + str(row["category"])
            + " - ₹"
            + str(row["amount"])
            + " - "
            + str(row["date"])
        )

        expense_options.append(text)


    selected_expense = st.selectbox(
        "Select Expense",
        expense_options
    )


    # Get ID from selected expense
    selected_id = int(
        selected_expense.split(" - ")[0]
    )


    if st.button(
        "🗑️ Delete Expense"
    ):

        delete_expense(selected_id)

        st.success(
            "Expense deleted successfully!"
        )

        st.rerun()


    # -----------------------------------------------------
    # DOWNLOAD REPORT
    # -----------------------------------------------------

    st.subheader("📥 Download Report")

    st.write(
        "Download your expense data as a CSV file."
    )


    csv_file = filtered_data.to_csv(
        index=False
    )


    st.download_button(
        "📥 Download CSV",
        csv_file,
        "expense_report.csv",
        "text/csv"
    )