from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL = "models/gemini-embedding-001"
GENERATION_MODEL = "gemini-2.5-flash"
TOP_K_RESULTS = 5

prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the context below.
If you don't know the answer, say "I don't know".

Context: {context}

Question: {question}
""")


def build_pipeline(documents: list[Document]) -> dict:

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY
    )
    vectorstore = FAISS.from_documents(chunks, embeddings)

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": TOP_K_RESULTS}
    )

    llm = ChatGoogleGenerativeAI(
        model=GENERATION_MODEL,
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3
    )

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return {"chain": chain, "retriever": retriever}


def ask_question(pipeline: dict, question: str) -> dict:
    chain = pipeline["chain"]
    retriever = pipeline["retriever"]

    answer = chain.invoke(question)
    sources = retriever.invoke(question)

    return {
        "answer": answer,
        "sources": sources
    }