import streamlit as st

def display_query_form():
    query = st.text_area(
        "Enter your question about Kenyan wildlife:",
        key="query_input",
        height=120,
        placeholder="Example: What are the main wildlife corridors in the Masai Mara?"
    )
    submit = st.button("Submit Query", key="submit_btn")
    return query, submit


def display_examples():
    st.markdown("### Examples")
    if st.button("Where are main wildlife corridors in Masai Mara?"):
        st.session_state.example = "Where are the main wildlife corridors in the Masai Mara?"
    if st.button("Which species are currently migrating?"):
        st.session_state.example = "Which species are currently migrating in the Masai Mara?"
    st.markdown("---")
    st.caption("Built with Streamlit • LangChain • ChromaDB")
