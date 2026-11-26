# 📊 AI Digital Policy & Economic Research Assistant

An AI-first **Retrieval-Augmented Generation (RAG)** web application built with **Python, Streamlit, Google Gen AI SDK, and SQLite**. It enables researchers, policy analysts, and developers to upload multi-page PDF documents (such as RBI circulars, IAMAI industry reports, and economic policy briefs) to generate structured executive summaries and cited Q&A responses in seconds.

## 🚀 Live Application
**[Open Live App](https://ai-policy-research-rag-assistant-cab6meyttckskzggekfuaw.streamlit.app/)**

---

## ✨ Key Features
* **Page-Indexed PDF Extraction:** Parses multi-page PDFs using `pypdf` while preserving page numbers so every AI claim includes verifiable citations (e.g., `[Page 2]`).
* **Dynamic LLM Discovery & Fallback:** Automatically queries available Gemini Flash models via `client.models.list()` and falls back seamlessly across models to prevent API downtime or rate-limit failures.
* **Grounded Prompt Engineering:** Enforces strict document-grounded answering to eliminate hallucinations when analyzing dense regulatory text.
* **Persistent SQLite Query Logging:** Logs document names, timestamps, and user queries into a local `SQLite3` database with a live audit sidebar.

---

## 🛠️ Tech Stack
* **Language:** Python 3
* **Frontend & Cloud Hosting:** Streamlit & Streamlit Community Cloud
* **AI / LLM Integration:** Google Gen AI SDK (`google-genai`)
* **Document Parsing:** `pypdf`
* **Database:** `SQLite3`

---

## 📂 Project Structure
```text
├── app.py              # Main Streamlit UI, PDF parser, Gemini fallback logic, and SQLite logger
├── requirements.txt    # Python dependencies for cloud deployment
├── PROMPTS.md          # Log of AI-assisted development and system prompts used
└── README.md           # Project documentation
```

---

## ⚙️ Run Locally
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd ai-policy-research-rag-assistant
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your Gemini API key:**
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```
4. **Launch the app:**
   ```bash
   streamlit run app.py
   ```
