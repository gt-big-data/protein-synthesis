import streamlit as st

st.write("Design New Transcription Factor")
with st.container():
    tab1, tab2, tab3 = st.tabs(["Target Sequence", "Parameters", "Advanced Options"])
    with tab1:
        st.write("Target Type")
        col1, col2 = st.columns(2)
        with col1:
            target_type = st.selectbox(
                "Target Type",
                ("Type 1", "Type 2", "Type 3"),
                index=None,
                placeholder="Select Target Type",
            )
            target_sequence = st.text_area("Target Sequence", placeholder="Enter or paste target sequence")
            transcription_factor_type = st.selectbox(
                "Transcription Factor Type",
                ("Type 1", "Type 2", "Type 3"),
                index=None,
                placeholder="Select Transcription Factor Type",
            )
        with col2:
            optimization_goal = st.selectbox(
                "Optimization Goal",
                ("Type 1", "Type 2", "Type 3"),
                index=None,
                placeholder="Select Optimization Goal",
            )
            number = st.number_input("Number of Designs", value=1, step=1, placeholder="Input Number of Designs")
            cellular_context = st.selectbox(
                "Cellular Context",
                ("Type 1", "Type 2", "Type 3"),
                index=None,
                placeholder="Select Cellular Context",
            )

    with tab2:
    
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with tab3:
        
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

    