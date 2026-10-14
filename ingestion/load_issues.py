import requests
import json
import os

os.makedirs("data/issues", exist_ok=True)

issues = []

for page in range(1, 6):  # First 500 issues
    url = "https://api.github.com/repos/fastapi/fastapi/issues"

    response = requests.get(
        url,
        params={
            "state": "closed",
            "per_page": 100,
            "page": page
        }
    )

    page_issues = response.json()

    if not page_issues:
        break

    issues.extend(page_issues)

print(f"Downloaded {len(issues)} issues")

with open(
    "data/issues/fastapi_issues.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        issues,
        f,
        indent=4,
        ensure_ascii=False
    )

print("Issues Saved Successfully")