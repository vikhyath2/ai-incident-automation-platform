import streamlit as st
import requests
import pandas as pd


API_BASE_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="AI Incident Automation Platform",
    layout="wide"
)

st.title("AI Incident Automation Platform")
st.write("Upload application logs and let AI analyze incidents automatically.")


st.header("Upload Log File")

uploaded_file = st.file_uploader(
    "Upload a .txt or .log file",
    type=["txt", "log"]
)

if uploaded_file is not None:
    if st.button("Analyze Log File"):
        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "text/plain"
            )
        }

        response = requests.post(
            f"{API_BASE_URL}/analyze-log-file",
            files=files
        )

        if response.status_code == 200:
            data = response.json()
            analysis = data["analysis"]

            st.success("Incident analyzed successfully")

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Issue Summary")
                st.write(analysis["issue_summary"])

                st.subheader("Root Cause")
                st.write(analysis["root_cause"])

            with col2:
                st.subheader("Severity")
                st.write(analysis["severity"])

                st.subheader("Suggested Fix")
                st.write(analysis["suggested_fix"])

            st.subheader("Next Action")
            st.write(analysis["next_action"])

        else:
            st.error(response.json().get("detail", "Something went wrong"))


st.divider()

st.header("Incident History")

if st.button("Refresh Incident History"):
    response = requests.get(f"{API_BASE_URL}/incidents")

    if response.status_code == 200:
        data = response.json()
        incidents = data["incidents"]

        if incidents:
            df = pd.DataFrame(incidents)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No incidents found.")
    else:
        st.error("Failed to fetch incidents.")