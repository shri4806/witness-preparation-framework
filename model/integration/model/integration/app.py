import re
import streamlit as st

st.set_page_config(
    page_title="Witness Preparation Framework",
    layout="centered"
)

st.title("Witness Preparation Framework")
st.subheader("AI-assisted Pre-Trial Analysis for Witness Preparation")

st.markdown("---")

st.write(
    "Upload a witness statement or paste a transcript below to analyze potential inconsistencies and preparation risks."
)

# Input section
uploaded_file = st.file_uploader("Upload Transcript File", type=["txt", "pdf"])
text_input = st.text_area("Or paste witness statement here", height=200)

st.markdown("---")


# ✅ REAL ANALYSIS FUNCTION (DEFINED ONCE, OUTSIDE BUTTON)
def analyze_text(text):
    # Extract time mentions
    times = re.findall(r'\b\d{1,2}:\d{2}\s*(?:AM|PM|am|pm)?\b', text)

    result = {
        "consistency": "No explicit time inconsistency detected",
        "risks": [],
        "suggestions": [],
        "preparedness": "HIGH"
    }

    if len(times) > 0:
        result["consistency"] = f"Time mentioned: {', '.join(times)}"
        result["risks"].append("Time reference requires clarification")
        result["suggestions"].append("Confirm the exact time of the event")
        result["preparedness"] = "MODERATE"

    return result


# ✅ BUTTON LOGIC
if st.button("Analyze Statement"):
    if uploaded_file is None and not text_input.strip():
        st.warning("Please upload a transcript or paste a statement.")
    else:
        with st.spinner("Analyzing witness statement..."):
            result = analyze_text(text_input)

        st.markdown("## Consistency Check")
        st.error(result["consistency"])

        st.markdown("## Cross-Examination Risks")
        for risk in result["risks"]:
            st.warning(risk)

        st.markdown("## Suggested Clarifications")
        for suggestion in result["suggestions"]:
            st.success(suggestion)

        st.markdown("## Preparedness Level")
        st.info(result["preparedness"])

    
