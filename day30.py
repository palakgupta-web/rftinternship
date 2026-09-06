import pandas as pd
from datetime import datetime


def process_invoices(file_path):
    df = pd.read_csv(file_path)

    # Calculate total amount
    df["Total Amount"] = df["Quantity"] * df["Price"]

    # Convert date columns
    df["Invoice Date"] = pd.to_datetime(df["Invoice Date"])
    df["Due Date"] = pd.to_datetime(df["Due Date"])

    # Identify overdue invoices
    today = pd.Timestamp.today().normalize()

    df["Status"] = df["Due Date"].apply(
        lambda x: "Overdue" if x < today else "Pending"
    )

    return df


def generate_summary(df):
    total_invoices = len(df)
    total_amount = df["Total Amount"].sum()
    overdue_count = (df["Status"] == "Overdue").sum()
    pending_count = (df["Status"] == "Pending").sum()

    summary = {
        "Total Invoices": total_invoices,
        "Total Amount": total_amount,
        "Overdue Invoices": overdue_count,
        "Pending Invoices": pending_count
    }

    return summary


if __name__ == "__main__":

    file_path = "data/invoices.csv"

    df = process_invoices(file_path)

    print("\nConsolidated Invoice Report")
    print(df)

    summary = generate_summary(df)

    print("\nInvoice Summary")
    for key, value in summary.items():
        print(f"{key}: {value}")

    df.to_csv(
        "output/consolidated_invoice_report.csv",
        index=False
    )

    print("\nReport exported successfully!")