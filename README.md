# Kenyan Wildlife Conservation RAG Agent

This project implements a Retrieval Augmented Generation (RAG) agent designed to provide accurate information about Kenyan wildlife and conservation efforts. The agent uses document retrieval powered by LangChain, embeddings, and a language model to answer natural language queries based on relevant conservation documents.

## Features
- Retrieval from Kenyan wildlife conservation PDFs and texts
- Embedding-based semantic search using HuggingFace and Sentence Transformers
- Streamlit web interface for interactive querying
- Modular Python code for indexing and querying

## Installation and Setup

1. Create and activate a Python virtual environment:
python -m venv venv
source venv/bin/activate

2. Install required dependencies using the provided requirements.txt file:
pip install -r requirements.txt

## Usage

1. To build the document index, run:
python index.py

2. To start the Streamlit app for querying:
streamlit run app.py

## Notes

- The `langchain-huggingface` package should be imported as:
from langchain_huggingface import HuggingFaceEmbeddings

- Make sure your PDF or text documents related to Kenyan wildlife conservation are placed in the appropriate data directory for indexing.

## Project Structure

- `index.py`: Script to build the vector index over conservation documents.
- `app.py`: Streamlit app to interface with the RAG agent.
- `docs/`: Folder containing the conservation PDFs and texts.
- `requirements.txt`: List of all Python dependencies.
- `venv/`: Python virtual environment folder.

## References

- National Wildlife Strategy 2030 - Kenya
- Kenya Wildlife Service Strategic Plans
- African Wildlife Foundation Kenya Conservation Reports

## License

This project is open source and available under the MIT License.
