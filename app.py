from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from llama_index.core import (
    StorageContext,
    load_index_from_storage,
    Settings
)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.google_genai import GoogleGenAI

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="Engineering Intelligence Hub",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Engineering Intelligence Hub")
st.markdown(
    "Ask questions about FastAPI code, documentation, and issue history."
)

# -------------------------
# Models
# -------------------------

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

Settings.llm = GoogleGenAI(
    model="gemini-3.6-flash"
)

# -------------------------
# Load Index
# -------------------------

@st.cache_resource
def load_index():

    storage_context = StorageContext.from_defaults(
        persist_dir="./storage"
    )

    return load_index_from_storage(storage_context)

index = load_index()

query_engine = index.as_query_engine(
    similarity_top_k=5
)

# -------------------------
# Question Box
# -------------------------

question = st.text_input(
    "Ask a question:"
)

if st.button("Search"):

    with st.spinner("Thinking..."):

        response = query_engine.query(question)

    st.subheader("Answer")
    st.write(str(response))

    if hasattr(response, "source_nodes"):

        st.subheader("Sources")

        for i, node in enumerate(
            response.source_nodes,
            start=1
        ):

            path = node.metadata.get(
                "file_path",
                "Unknown Source"
            )

            st.write(f"{i}. {path}")