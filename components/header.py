import streamlit as st

def display_header():
    # Use markdown with HTML and CSS for styled header or keep simple with st.title and st.markdown
    st.markdown(
        """
        <style>
        .header {
            background: linear-gradient(135deg, #083358 0%, #0b486b 50%, #1a8f7a 100%);
            padding: 22px;
            border-radius: 10px;
            color: white;
            box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="header"><h1 style="margin:0">🦁 Kenyan Wildlife Conservation Advisor</h1>'
        '<p style="margin:6px 0 0 0;opacity:.9">Ask about wildlife corridors, migration, and conservation in the Masai Mara.</p>'
        '</div>',
        unsafe_allow_html=True,
    )
