from dotenv import load_dotenv
load_dotenv()

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings
)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

documents = SimpleDirectoryReader(
    "Engineer Intelligence Hub/data/fastapi_repo/docs"
).load_data()

print(f"Loaded {len(documents)} documents")

index = VectorStoreIndex.from_documents(documents)

index.storage_context.persist(
    persist_dir="./storage"
)

print("Index Created Successfully!")