# ai-policy-research-rag-assistant
markdown
# 📊 AI Digital Policy & Economic Research Assistant

An AI-first Retrieval-Augmented Generation (RAG) web application built with **Python, Streamlit, Google Gemini API, and SQLite**. It enables researchers, policymakers, and analysts to upload dense PDF reports (such as RBI circulars, IAMAI industry reports, and economic policy briefs) and generate cited answers or executive summaries in seconds.

## 🚀 Live Demo
**[Click here to open the Live App](YOUR_STREAMLIT_APP_LINK_HERE)** *(Update this link after Step 3)*

## 🛠️ Tech Stack & Architecture
- **Frontend & Cloud Hosting:** Streamlit & Streamlit Community Cloud
- **LLM Integration:** Google Gen AI SDK (`gemini-2.5-flash`) with grounded prompt engineering
- **Document Parsing:** `pypdf` with page-level metadata indexing for citation accuracy
- **Database:** `SQLite3` backend for persistent query auditing and analytics
- **Development Workflow:** Built using an AI-first development approach (documented in `PROMPTS.md`)

## ⚙️ How to Run Locally
1. Clone the repository: `git clone https://github.com`
2. Install dependencies: `pip install -r requirements.txt`
3. Set your API key: `export GEMINI_API_KEY="your_api_key"`
4. Run the app: `streamlit run app.py`
