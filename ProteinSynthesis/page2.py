import streamlit as st
import requests

# Placeholder for your function - replace this with your actual implementation
def process_input(user_input):
    response = requests.post("https://bdbi-similarity-search-599794866638.us-central1.run.app/run", json={"sequence": user_input})
    print(response)
    print(response.text)
    if response.status_code != 200:
        return "Error: Cannot find similar sequence (may be because sequence is too short)"
    result = response.json()['result']
    s = ""
    for res in result:
        s += f"Similarity: {res['score']}, Tf: {res['tf']}\nSequence: {res['sequence']}\n\n"
    return s

# Streamlit UI
st.title("Similarity Search")

# Text input box
user_input = st.text_input("Enter a sequence:", "")

# Process button
if st.button("Process"):
    if user_input:
        with st.spinner("Processing..."):
            result = process_input(user_input)
        st.write("Output:")
        for line in result.split('\n'):
            st.write(line)
    else:
        st.warning("Please enter a string to process")