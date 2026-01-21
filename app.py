import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Study Buddy", layout="centered")

st.title("📚 AI Study Buddy")
st.write("Summarize your study notes using AI")

@st.cache_resource
def load_summarizer():
    return pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6",
        device=-1
    )

summarizer = load_summarizer()

text = st.text_area("📄 Paste your notes here")

if st.button("✨ Summarize"):
    if text.strip():
        with st.spinner("Summarizing..."):
            summary = summarizer(
                text,
                max_length=120,
                min_length=30,
                do_sample=False
            )
        st.success(summary[0]["summary_text"])
    else:
        st.warning("Please paste some text")
