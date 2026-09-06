import streamlit as st
import pandas as pd
from day30 import process_invoices, generate_summary

st.set_page_config(
    page_title="Invoice Processing System",
    page_icon="🧾",
    layout="wide"
)

st.title("🧾 Automated Invoice Processing System")

st.write(
    "Upload your invoice CSV file to automatically process "
    "invoice details and identify overdue invoices."
)

uploaded_file = st.file_uploader(
    "Upload Invoice CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # Calculate total
    df["Total Amount"] = df["Quantity"] * df["Price"]

    # Convert dates
    df["Invoice Date"] = pd.to_datetime(df["Invoice Date"])
    df["Due Date"] = pd.to_datetime(df["Due Date"])

    today = pd.Timestamp.today().normalize()

    df["Status"] = df["Due Date"].apply(
        lambda x: "Overdue" if x < today else "Pending"
    )

    st.success("Invoice processed successfully!")

    # Summary
    summary = generate_summary(df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Invoices",
        summary["Total Invoices"]
    )

    col2.metric(
        "Total Amount",
        f"₹{summary['Total Amount']:,.2f}"
    )

    col3.metric(
        "Overdue",
        summary["Overdue Invoices"]
    )

    col4.metric(
        "Pending",
        summary["Pending Invoices"]
    )

    st.subheader("📋 Consolidated Invoice Report")

    st.dataframe(
        df,
        use_container_width=True
    )

    # Overdue invoices
    st.subheader("⚠️ Overdue Invoices")

    overdue = df[df["Status"] == "Overdue"]

    if len(overdue) > 0:
        st.dataframe(
            overdue,
            use_container_width=True
        )
    else:
        st.success("No overdue invoices!")

    # Download report
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Consolidated Report",
        data=csv,
        file_name="consolidated_invoice_report.csv",
        mime="text/csv"
    )