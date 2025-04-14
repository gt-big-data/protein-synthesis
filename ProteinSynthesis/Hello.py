import streamlit as st

pages = {
    "Design Tools": [
        st.Page("page1.py", title="New Design"),
        # st.Page("page2.py", title="My Designs"),
    ],
    "Analysis": [
        st.Page("page2.py", title="Similarity Search"),
        # st.Page("trial.py", title="Try it out"),
    ],
}
    
pg = st.navigation(pages)
pg.run()
    