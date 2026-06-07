import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path=dotenv_path)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

print("KEY:", GOOGLE_API_KEY)  # ← add here

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBEDDING_MODEL = "models/embedding-001"
GENERATION_MODEL = "gemini-pro"
TOP_K_RESULTS = 5