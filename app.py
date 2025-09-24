import streamlit as st
import pandas as pd

st.set_page_config(page_title="Agentic CX Dispute System", layout="wide")

st.title("📊 Agentic CX Dispute System")
st.markdown("This dashboard displays the dispute resolution ledger end-to-end.")

# Load ledger CSV
ledger_file = "agentic_cx_dispute_system_ledger.csv"
df = pd.read_csv(ledger_file)

# Show raw ledger in a table
st.subheader("Dispute Ledger")
st.dataframe(df, use_container_width=True)

# Show summary metrics
st.subheader("Summary")
final_balances = df[df["event_type"] == "final_balances"]["note"].iloc[0]
st.json(eval(final_balances))

# Show charts
st.subheader("Flow of Amounts by Event")
chart_data = df[["event_type", "amount"]]
st.bar_chart(chart_data.set_index("event_type"))
