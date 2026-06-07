import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain_core.documents import Document

def load_document(file_path: str, original_name: str = None) -> list[Document]:
    # use original filename for extension if provided
    name = original_name if original_name else file_path
    ext = os.path.splitext(name)[-1].lower()

    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext == ".docx":
        loader = Docx2txtLoader(file_path)
    elif ext == ".txt":
        loader = TextLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    return loader.load()

def load_multiple_documents(file_paths: list[str], original_names: list[str] = None) -> list[Document]:
    all_docs = []
    for i, path in enumerate(file_paths):
        orig = original_names[i] if original_names else None
        docs = load_document(path, original_name=orig)
        all_docs.extend(docs)
    return all_docs