python -m venv venv

source venv/bin/activate

pip install langchain chromadb "langchain-text-splitters" pypdf
pip install -U langchain-huggingface

pip install langchain-community
pip install sentence-transformers


python index.py

pip install chromadb

 `pip install -U `langchain-huggingface` and import as `from `langchain_huggingface import HuggingFaceEmbeddings``