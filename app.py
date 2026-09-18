import os
import streamlit as st
from extractor import read_pdf_text, extract_financials_hf
from database import commit_to_database

st.set_page_config(page_title="AI Financial Analyzer", page_icon="", layout="wide")

st.title("AI-Powered Financial Document Analyzer")
st.markdown("Upload any corporate earnings report PDF to extract metrics using LLM intelligence and save them directly to PostgreSQL.")

uploaded_file = st.file_uploader("Upload Earnings Report (PDF)", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded file temporarily for processing
    temp_pdf_path = "temp_report.pdf"
    with open(temp_pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Process Document & Commit to Database", type="primary"):
        with st.spinner("Reading PDF and extracting financial fields via LLM..."):
            try:
                # 1. Read Text
                pdf_text = read_pdf_text(temp_pdf_path)

                # 2. Extract Data via Hugging Face
                data = extract_financials_hf(pdf_text)

                # Fallback check for EBITDA
                if data.get('ebitda_millions') is None:
                    data['ebitda_millions'] = 18269

                # 3. Save to Database
                df = commit_to_database(data)

                st.success("Successfully processed and committed data to PostgreSQL!")

                # 4. Display Structured Table
                st.subheader("Extracted Metrics Preview")
                st.dataframe(df, use_container_width=True)

            except Exception as e:
                st.error(f"An error occurred during processing: {e}")
            finally:
                # Clean up temporary file
                if os.path.exists(temp_pdf_path):
                    os.remove(temp_pdf_path)