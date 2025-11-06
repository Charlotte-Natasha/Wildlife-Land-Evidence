import streamlit as st
from dotenv import load_dotenv

# Import your custom components
from components.header import display_header
from components.query_form import display_query_form, display_examples

# Load environment variables from .env file
load_dotenv()

def load_css():
    with open("assets/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    # Load CSS styles
    load_css()

    # Configure the page
    st.set_page_config(page_title="Kenyan Wildlife Conservation Advisor", page_icon="🦁", layout="wide")
    
    # 2. Add the Sidebar Section HERE
    # This renders immediately on the left side of the screen.
    with st.sidebar:
        st.header("About")
        st.info("""
        This agent uses RAG (Retrieval Augmented Generation) to provide accurate
        information about Kenyan wildlife and conservation efforts.
        """)
    # Display header component
    display_header()

    # Create two columns layout: Query input and system info/examples
    col1, col2 = st.columns([2, 1], gap="large")

    with col2:
        st.markdown("### System")

        # Lazy import and initialize retriever
        try:
            from query_agent import create_retriever
            try:
                retriever = create_retriever()
                st.success("Vector DB: available")
                st.caption(f"Collection: {getattr(retriever, 'collection', {}).get('name', '') or 'unknown'}")
            except Exception as e:
                st.warning(f"Vector DB load issue: {e}")
        except Exception:
            st.error("query_agent import failed. Fix query_agent.py before running. See terminal for details.")

        st.markdown("---")
        # Display example queries with buttons
        display_examples()

    with col1:
        # Show query form to accept user input
        query, submit = display_query_form()

        # Inject example query if no query entered
        if "example" in st.session_state and not query:
            query = st.session_state.pop("example")

        if submit and not query:
            st.warning("Please enter a query.")
        elif submit and query:
            from query_agent import run_rag_chain
            with st.spinner("Searching knowledge base..."):
                try:
                    response = run_rag_chain(query)
                    # Show response nicely
                    st.markdown('<div class="response-card">', unsafe_allow_html=True)
                    st.markdown("### Response")
                    if isinstance(response, (list, dict)):
                        st.json(response)
                    else:
                        st.markdown(response)
                    st.markdown('</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"An error occurred while running the RAG chain: {e}")

if __name__ == "__main__":
    main()
