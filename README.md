# 📄 Document Question Answering System

A RAG-based (Retrieval-Augmented Generation) application that lets you upload documents and ask questions about them in natural language. Built with LangChain, Google Gemini, FAISS, and Streamlit.

---

## 🚀 Demo

Upload any PDF, TXT, or DOCX file → ask a question → get an answer with source chunks cited.

---

## 🧠 How It Works

```
Documents (PDF/TXT/DOCX)
        ↓
   Text Chunking (RecursiveCharacterTextSplitter)
        ↓
   Embeddings (Gemini gemini-embedding-001)
        ↓
   Vector Store (FAISS)
        ↓
   Query → Retrieve Top-K Chunks → Gemini LLM → Answer
```

---

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| UI | Streamlit |
| Orchestration | LangChain |
| Embeddings | Google Gemini (`gemini-embedding-001`) |
| LLM | Google Gemini (`gemini-2.5-flash`) |
| Vector Store | FAISS |
| File Support | PDF, TXT, DOCX |

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Hetvi511/Document-QA-RAG.git
cd Document-QA-RAG
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:
```
GOOGLE_API_KEY=your_google_api_key_here
```

> Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 5. Run the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Document-QA-RAG/
│
├── app.py                  # Streamlit UI
├── core/
│   ├── loader.py           # Document loading logic
│   └── pipeline.py         # RAG pipeline (chunking, embedding, retrieval, generation)
├── .env                    # API keys (not tracked)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 💡 Features

- Upload multiple documents at once
- Supports PDF, TXT, and DOCX formats
- Displays source chunks used to generate each answer
- Session-based pipeline — no repeated reprocessing
- Clean, minimal UI

---

## 📌 Future Improvements

- Add chat history / multi-turn conversation
- Support more file types (CSV, PPTX)
- Persistent vector store across sessions
- Deploy on Streamlit Cloud

---

## 👩‍💻 Author

**Hetvi Joshi**  
B.Tech Computer Science & Data Science | University of Mumbai  
[LinkedIn](https://www.linkedin.com/in/hetvi-joshi05)  
[GitHub](https://github.com/Hetvi511)
