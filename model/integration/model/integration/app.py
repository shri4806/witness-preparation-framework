import streamlit as st

st.set_page_config(
    page_title="Witness Preparation Framework",
    layout="centered"
)

st.title("Witness Preparation Framework")
st.subheader("AI-assisted Pre-Trial Analysis for Witness Preparation")

st.markdown("---")

st.write("Upload a witness statement or paste a transcript below to analyze potential inconsistencies and preparation risks.")

# Input section
uploaded_file = st.file_uploader("Upload Transcript File", type=["txt", "pdf"])
text_input = st.text_area("Or paste witness statement here", height=200)

st.markdown("---")

if st.button("Analyze Statement"):
    st.info("Analysis logic will be integrated here.")
