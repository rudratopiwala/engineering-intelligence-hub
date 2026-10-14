# Engineering Intelligence Hub

### A RAG-Based Assistant for Understanding Codebases and Documentation

## About the Project

When working on a large software project, it can take a lot of time to find the right information in source code and documentation. The Engineering Intelligence Hub is a project I built to make this process easier.

It uses Retrieval-Augmented Generation (RAG) to search a software codebase and its documentation and provide answers to questions based on the available information.

For this project, I used the FastAPI repository as a sample codebase. The system reads Python source files and documentation, creates a searchable index, and uses that index to find relevant information when a question is asked.

## Features

- **Codebase Ingestion:** Reads Python source files and documentation from the FastAPI repository.
- **Document Indexing:** Builds a searchable index from the collected files.
- **Semantic Search:** Finds relevant information based on the meaning of a question, rather than relying only on exact keyword matches.
- **RAG-Based Question Answering:** Uses retrieved information to help generate answers to technical questions.
- **Source File References:** Shows the paths of relevant source files so users can check the original information.
- **Local Index Storage:** Saves the generated index locally so it can be reused without rebuilding it every time.

## Technologies Used

- **Python** – Main programming language.
- **LlamaIndex** – Used to build, store, and query the document index.
- **Hugging Face Embeddings** – Uses `BAAI/bge-small-en-v1.5` to convert text into embeddings for semantic search.
- **Google Gemini** – Used as the language model for answering questions.
- **Git and GitHub** – Used for version control and project hosting.

## Project Structure

```text
Engineer-Intelligence-Hub/
│
├── app.py
├── ingestion/
│   ├── load_docs.py
│   ├── load_issues.py
│   ├── load_issue_docs.py
│
├── rag/
│   ├── build_index.py
│   ├── build_full_index.py
│   └── query.py
│
├── data/
│   └── fastapi_repo/
│
├── storage/
│   └── Local index files
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## How It Works

**1. Collect the data**

The project uses the FastAPI repository as its sample codebase. It collects relevant Python files and documentation for indexing.

**2. Create the index**

The collected content is processed and converted into embeddings using the Hugging Face embedding model. LlamaIndex organizes this information into a searchable index.

**3. Store the index**

The index is saved locally in the `storage` folder so it can be loaded again when needed.

**4. Ask questions**

The query script accepts questions about the codebase and retrieves the most relevant information from the index.

**5. Generate answers**

The retrieved information is passed to Google Gemini to help generate an answer. The script also displays relevant source file paths.

