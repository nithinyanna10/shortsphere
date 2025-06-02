import streamlit as st
import pandas as pd
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="ShortSphere Analytics", layout="centered")

st.title("📈 ShortSphere – URL Analytics Dashboard")

code = st.text_input("Enter your short code (e.g., XyZ123):")

if st.button("Get Analytics"):
    if code:
        response = requests.get(f"{BACKEND_URL}/analytics/{code}")
        if response.status_code == 200:
            data = response.json()
            st.success(f"✅ Total Clicks: {data['total_clicks']}")

            # Country Chart
            countries_df = pd.DataFrame(list(data["countries"].items()), columns=["Country", "Clicks"])
            st.subheader("🌍 Clicks by Country")
            st.bar_chart(countries_df.set_index("Country"))

            # User-Agent Chart
            ua_df = pd.DataFrame(list(data["user_agents"].items()), columns=["User Agent", "Count"])
            st.subheader("💻 User Agents")
            st.bar_chart(ua_df.set_index("User Agent"))

            # Download Logs
            df = pd.DataFrame(data["raw_logs"])
            st.subheader("📥 Raw Logs")
            st.dataframe(df)
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("Download CSV", data=csv, file_name=f"{code}_logs.csv", mime="text/csv")
        else:
            st.error(f"❌ No analytics found for code: {code}")
