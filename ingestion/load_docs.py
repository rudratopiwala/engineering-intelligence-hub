from llama_index.core import SimpleDirectoryReader

docs = SimpleDirectoryReader(
    "data/fastapi_repo/docs"
).load_data()

print(f"Loaded {len(docs)} documents")
