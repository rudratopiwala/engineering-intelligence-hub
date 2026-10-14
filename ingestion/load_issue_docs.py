import json
from llama_index.core import Document

with open(
    "data/issues/fastapi_issues.json",
    "r",
    encoding="utf-8"
) as f:
    issues = json.load(f)

documents = []

for issue in issues:

    title = issue.get("title", "")
    body = issue.get("body", "")

    text = f"""
Issue Title:
{title}

Issue Description:
{body}
"""

    documents.append(
        Document(
            text=text,
            metadata={
                "issue_number": issue.get("number"),
                "issue_url": issue.get("html_url")
            }
        )
    )

print(f"Created {len(documents)} issue documents")