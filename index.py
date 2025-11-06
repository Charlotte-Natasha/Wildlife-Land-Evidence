import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# --- CONFIGURATION ---
DATA_PATH = "docs" # Path to your folder containing the documents
CHROMA_DB_PATH = "wildlife_db" # Folder where ChromaDB will store the data
COLLECTION_NAME = "kenya_wildlife_corpus"
CHUNK_SIZE = 1000 # Max characters per text chunk
CHUNK_OVERLAP = 200 # Overlap ensures context isn't lost at the boundaries of chunks

# --- EMBEDDING MODEL ---
# This model will convert your text chunks into numerical vectors.
# Note: Requires 'sentence-transformers' package.
EMBEDDING_MODEL = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def load_documents():
    """Loads all PDF files from the DATA_PATH folder."""
    # Using DirectoryLoader to load multiple files at once.
    # We specify the PyPDFLoader to handle PDF file types.
    print(f"Loading documents from directory: {DATA_PATH}...")
    loader = DirectoryLoader(DATA_PATH, glob="**/*.pdf", loader_cls=PyPDFLoader)
    # You can add more loaders for .txt or .md files if needed!
    documents = loader.load()
    print(f"Successfully loaded {len(documents)} document pages/sections.")
    return documents

def split_documents(documents):
    """Splits the loaded documents into smaller, optimized chunks."""
    print("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len
    )
    # The split_documents method handles all the loaded documents at once.
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} total text chunks for indexing.")
    return chunks

def store_chunks_in_vectordb(chunks):
    """Generates embeddings and stores the chunks in a persistent ChromaDB."""
    print(f"Indexing chunks into ChromaDB at: {CHROMA_DB_PATH}...")
    
    # This step simultaneously generates embeddings using the specified model
    # and writes the vectors, text, and metadata to the persistent ChromaDB folder.
    db = Chroma.from_documents(
        documents=chunks,
        embedding=EMBEDDING_MODEL,
        persist_directory=CHROMA_DB_PATH,
        collection_name=COLLECTION_NAME
    )
    
    # We explicitly persist the database to ensure the data is saved to disk
    db.persist()
    print(f"Indexing complete! Database saved to '{CHROMA_DB_PATH}'.")
    print("The knowledge base is ready for retrieval.")

def main():
    # 1. Load: Read all files from the 'docs' folder
    documents = load_documents()
    
    if not documents:
        print("No documents found! Please ensure your legal, ecological, and historical PDFs are in the 'docs' folder.")
        return
        
    # 2. Split: Divide the documents into small chunks
    chunks = split_documents(documents)
    
    # 3. Store: Embed and save the chunks to the vector database
    store_chunks_in_vectordb(chunks)

if __name__ == "__main__":
    main()