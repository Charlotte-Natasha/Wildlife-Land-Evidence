import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# --- CONFIGURATION (Must match your indexing script) ---
CHROMA_DB_PATH = "wildlife_db"
COLLECTION_NAME = "kenya_wildlife_corpus"

# The embedding model MUST be the SAME one used during indexing
EMBEDDING_MODEL = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def verify_index():
    """Attempts to load the database and perform a semantic search."""
    print("--- Starting Index Verification ---")

    # 1. Checks if the database folder exists
    if not os.path.exists(CHROMA_DB_PATH):
        print(f"❌ ERROR: Vector database folder not found at '{CHROMA_DB_PATH}'.")
        print("Please ensure you ran 'index_documents.py' successfully.")
        return

    try:
        # 2. Loads the existing Chroma database from disk
        db = Chroma(
            persist_directory=CHROMA_DB_PATH,
            embedding_function=EMBEDDING_MODEL,
            collection_name=COLLECTION_NAME
        )
        print(f"✅ Success: ChromaDB loaded from disk using collection '{COLLECTION_NAME}'.")

        # 3. Performs a test search using a query that should retrieve specific content
        test_query = "court decision regarding land ownership and conservation"
        print(f"Testing retrieval with query: '{test_query}'")
        
        # Uses the similarity search function
        results = db.similarity_search(test_query, k=2)

        if results:
            print("\n✅ Index Verification Passed! Retrieved relevant documents:")
            
            for i, doc in enumerate(results):
                # Prints the source and the content snippet
                source = doc.metadata.get('source', 'Unknown Source')
                page = doc.metadata.get('page', 'N/A')
                content_snippet = doc.page_content[:150].replace('\n', ' ') + '...'
                
                print(f"--- Document {i+1} ---")
                print(f"Source: {source} (Page: {page})")
                print(f"Snippet: {content_snippet}")
            
            print("\nDocuments are indexed and retrievable. You can now run 'query_agent.py'.")
        else:
            print("❌ Retrieval Failed: No documents were returned for the test query.")
            print("The database loaded, but it might be empty or the embedding function doesn't match.")

    except Exception as e:
        print(f"\n❌ A critical error occurred during index loading: {e}")
        print("This often means the wrong embedding model was used or the database is corrupted.")

if __name__ == "__main__":
    verify_index()