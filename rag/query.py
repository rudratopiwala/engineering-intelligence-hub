from dotenv import load_dotenv
load_dotenv()

import os

from llama_index.core import (
    StorageContext,
    load_index_from_storage,
    Settings
)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.google_genai import GoogleGenAI

# Embedding Model
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# Gemini LLM
Settings.llm = GoogleGenAI(
    model="gemini-3.6-flash"
)

# Check storage folder
if not os.path.exists("./storage"):
    print("❌ Storage folder not found!")
    print("Run build_full_index.py first.")
    exit()

print("✅ Loading Index...")

storage_context = StorageContext.from_defaults(
    persist_dir="./storage"
)

index = load_index_from_storage(storage_context)

print("✅ Index Loaded Successfully!")

query_engine = index.as_query_engine(
    similarity_top_k=5
)

while True:
    question = input("\nAsk a Question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    try:
        response = query_engine.query(question)

        print("\n" + "="*80)
        print("ANSWER")
        print("="*80)
        print(response)

        if hasattr(response, "source_nodes"):
            print("\n" + "="*80)
            print("SOURCES")
            print("="*80)

            for i, node in enumerate(response.source_nodes, start=1):
                file_path = node.metadata.get(
                    "file_path",
                    node.metadata.get("file_name", "Unknown")
                )

                print(f"{i}. {file_path}")

    except Exception as e:
        print(f"\n❌ Error: {e}")