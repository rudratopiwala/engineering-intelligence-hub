from llama_index.core import SimpleDirectoryReader

code_docs = SimpleDirectoryReader(
    input_dir="Engineer Intelligence Hub/data/fastapi_repo/fastapi",
    required_exts=[".py"],
    recursive=True
).load_data()

print(f"Loaded {len(code_docs)} code files")

for doc in code_docs[:3]:
    print("\n", doc.metadata.get("file_name"))