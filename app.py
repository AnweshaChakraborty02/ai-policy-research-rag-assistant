streamlit
google-genai
pypdf
import os
import sqlite3
from datetime import datetime
import streamlit as st
from pypdf import PdfReader
from google import genai

# Page configuration
st.set_page_config(page_title="AI Policy & Research Assistant", page_icon="📊", layout="wide")

# Initialize SQLite database for query logging
def init_db():
    conn = sqlite3.connect("query_logs.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            document_name TEXT,
            question TEXT,
            answer_preview TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_query(doc_name, question, answer):
    conn = sqlite3.connect("query_logs.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO logs (timestamp, document_name, question, answer_preview) VALUES (?, ?, ?, ?)",
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), doc_name, question, answer[:150] + "...")
    )
    conn.commit()
    conn.close()

def get_recent_logs():
    conn = sqlite3.connect("query_logs.db")
    c = conn.cursor()
    c.execute("SELECT timestamp, document_name, question FROM logs ORDER BY id DESC LIMIT 5")
    rows = c.fetchall()
    conn.close()
    return rows

init_db()

# Sidebar for API Key & Recent SQL Logs
with st.sidebar:
    st.header("Configuration")
    api_key = st.secrets.get("GEMINI_API_KEY", "") or st.text_input("Enter Gemini API Key", type="password")
    st.markdown("---")
    st.subheader("Recent Queries (SQLite Log)")
    logs = get_recent_logs()
    if logs:
        for ts, doc, q in logs:
            st.caption(f"**{ts}** | *{doc}*")
            st.write(f"Q: {q}")
    else:
        st.caption("No queries logged yet.")

# Main UI
st.title("📊 AI Digital Policy & Economic Research Assistant")
st.markdown(
    "Upload any **policy brief, RBI circular, or industry report (PDF)** to extract insights, "
    "summarize key takeaways, and ask grounded questions powered by **Gemini LLM**."
)

uploaded_file = st.file_uploader("Upload Policy or Research PDF", type=["pdf"])

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    extracted_text = ""
    for idx, page in enumerate(reader.pages):
        page_text = page.extract_text() or ""
        extracted_text += f"\n--- Page {idx + 1} ---\n{page_text}"

    st.success(f"Loaded **{uploaded_file.name}** ({len(reader.pages)} pages extracted).")

    col1, col2 = st.columns([2, 1])
    with col1:
        user_question = st.text_input(
            "Ask a question about this document:",
            placeholder="e.g., What are the key regulatory recommendations or economic impacts mentioned?"
        )
    with col2:
        st.write("")
        st.write("")
        summarize_btn = st.button("✨ Generate Executive Summary")

    if not api_key:
        st.warning("Please configure your GEMINI_API_KEY in Streamlit Secrets or enter it in the sidebar.")
    else:
        client = genai.Client(api_key=api_key)

        if summarize_btn:
            with st.spinner("Synthesizing executive summary..."):
                prompt = (
                    "You are an expert economic and digital policy analyst. "
                    "Provide a structured executive summary of the following document with bullet points "
                    "for Key Objectives, Regulatory/Economic Impact, and Actionable Takeaways. "
                    "Cite page numbers where possible.\n\n"
                    f"Document Text:\n{extracted_text[:30000]}"
                )
                response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                st.subheader("Executive Summary")
                st.markdown(response.text)
                log_query(uploaded_file.name, "Executive Summary", response.text)

        if user_question:
            with st.spinner("Analyzing document for your answer..."):
                prompt = (
                    "Answer the user's question strictly using the provided document text. "
                    "Cite exact page numbers (e.g., [Page 2]) for every claim. "
                    "If the answer is not in the document, state that clearly.\n\n"
                    f"Document Text:\n{extracted_text[:30000]}\n\n"
                    f"Question: {user_question}"
                )
                response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                st.subheader("AI Response")
                st.markdown(response.text)
                log_query(uploaded_file.name, user_question, response.text)
