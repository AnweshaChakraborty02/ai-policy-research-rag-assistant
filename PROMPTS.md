# AI-First Development & Prompt Engineering Log

This project was built rapidly using an AI-assisted workflow. Below are the core prompts used to architect, build, and refine the application:

1. **System Architecture Prompt:**
   > "Design a lightweight RAG web application in Python and Streamlit that parses multi-page economic policy PDFs, preserves page numbers for citations, and logs user queries into a local SQLite database."

2. **Grounded Citation Prompt (Used inside `app.py`):**
   > "Answer the user's question strictly using the provided document text. Cite exact page numbers (e.g., [Page 2]) for every claim. If the answer is not in the document, state that clearly."

3. **Executive Synthesis Prompt (Used inside `app.py`):**
   > "You are an expert economic and digital policy analyst. Provide a structured executive summary of the following document with bullet points for Key Objectives, Regulatory/Economic Impact, and Actionable Takeaways."
