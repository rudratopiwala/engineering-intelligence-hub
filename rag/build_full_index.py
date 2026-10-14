from dotenv import load_dotenv
load_dotenv()

import json
import os

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings,
    Document
)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Embedding Model
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

print("Loading FastAPI Docs...")

docs = SimpleDirectoryReader(
    "data/fastapi_repo/docs",
    recursive=True
).load_data()

print(f"Docs Loaded: {len(docs)}")

print("Loading FastAPI Source Code...")

code = SimpleDirectoryReader(
    "data/fastapi_repo/fastapi",
    recursive=True,
    required_exts=[".py"]
).load_data()

print(f"Code Files Loaded: {len(code)}")

# ----------------------------
# Load GitHub Issues
# ----------------------------

issue_docs = []

issues_file = "data/issues/fastapi_issues.json"

if os.path.exists(issues_file):

    print("Loading GitHub Issues...")

    with open(
        issues_file,
        "r",
        encoding="utf-8"
    ) as f:

        issues = json.load(f)

    # Use only first 50 issues for testing
    issues = issues[:50]

    for issue in issues:

        title = issue.get("title", "")
        body = issue.get("body", "")

        text = f"""
Issue Title:
{title}

Issue Description:
{body}
"""

        issue_docs.append(
            Document(
                text=text,
                metadata={
                    "issue_number": issue.get("number"),
                    "issue_url": issue.get("html_url")
                }
            )
        )

print(f"Issue Documents Loaded: {len(issue_docs)}")

# ----------------------------
# Combine Everything
# ----------------------------

all_documents = docs + code + issue_docs

print(f"\nTotal Documents Loaded: {len(all_documents)}")

# Optional: limit size for testing
all_documents = all_documents[:1000]

print(f"Documents Used For Indexing: {len(all_documents)}")

# ----------------------------
# Create Index
# ----------------------------

print("\nCreating Index...")

index = VectorStoreIndex.from_documents(
    all_documents,
    show_progress=True
)

# ----------------------------
# Save Index
# ----------------------------

os.makedirs("storage", exist_ok=True)

index.storage_context.persist(
    persist_dir="./storage"
)

print("\n✅ Full Index Created Successfully!")
print("✅ Saved to ./storage")