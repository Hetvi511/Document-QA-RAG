import streamlit as st
import tempfile
import os
from core.loader import load_multiple_documents
from core.pipeline import build_pipeline, ask_question

st.set_page_config(page_title="DocQA", page_icon="📄", layout="wide")
st.title("📄 Document Question Answering System")
st.markdown("Upload your documents and ask anything.")

# session state initialization
if "pipeline" not in st.session_state:
    st.session_state["pipeline"] = None

# sidebar — file upload
with st.sidebar:
    st.header("Upload Documents")
    uploaded_files = st.file_uploader(
        "Choose files",
        type=["pdf", "txt", "docx"],
        accept_multiple_files=True
    )

    if uploaded_files and st.button("Process Documents"):
        with st.spinner("Building your knowledge base..."):

            # save uploaded files to temp location
            # collect original names
            temp_paths = []
            original_names = []
            for file in uploaded_files:
                suffix = os.path.splitext(file.name)[-1]
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                    tmp.write(file.read())
                    temp_paths.append(tmp.name)
                    original_names.append(file.name)  # track original name

# pass original names to loader
            documents = load_multiple_documents(temp_paths, original_names)
            st.session_state["pipeline"] = build_pipeline(documents)

            # cleanup temp files
            for path in temp_paths:
                os.remove(path)

        st.success(f"✅ {len(uploaded_files)} document(s) processed!")

# main area — Q&A
if st.session_state["pipeline"] is not None:
    st.subheader("Ask a Question")
    question = st.text_input("Type your question here...")

    if question:
        with st.spinner("Thinking..."):
            result = ask_question(st.session_state["pipeline"], question)

        st.markdown("### Answer")
        st.write(result["answer"])

        with st.expander("📚 Source Chunks Used"):
            for i, doc in enumerate(result["sources"]):
                st.markdown(f"**Chunk {i+1}** — `{doc.metadata.get('source', 'unknown')}`")
                st.write(doc.page_content)
                st.divider()
else:
    st.info("👈 Upload documents from the sidebar to get started.")