import streamlit as st
from transformers import pipeline

# Load models
summarizer = pipeline("summarization")
text_generator = pipeline("text-generation", model="gpt2")

st.set_page_config(page_title="AI Study Buddy", layout="centered")

st.title("📚 AI-Powered Study Buddy (Advanced)")
st.write("Explain topics, summarize notes, ask questions & generate MCQs")

menu = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Explain Topic",
        "Summarize Notes",
        "Ask Any Question",
        "Generate MCQs"
    ]
)

# ---------------- Explain Topic ----------------
if menu == "Explain Topic":
    level = st.selectbox("Choose difficulty level", ["Easy", "Medium", "Advanced"])
    topic = st.text_area("Enter topic")

    if st.button("Explain"):
        if topic.strip():
            prompt = f"Explain {topic} in a {level.lower()} way."
            result = text_generator(prompt, max_length=150)
            st.success(result[0]["generated_text"])
        else:
            st.warning("Please enter a topic")

# ---------------- Summarize Notes ----------------
elif menu == "Summarize Notes":
    notes = st.text_area("Paste your notes")

    if st.button("Summarize"):
        if notes.strip():
            result = summarizer(notes, max_length=120, min_length=40)
            st.success(result[0]["summary_text"])
        else:
            st.warning("Please paste notes")

# ---------------- Ask Any Question ----------------
elif menu == "Ask Any Question":
    question = st.text_input("Ask any question")

    if st.button("Get Answer"):
        if question.strip():
            with st.spinner("Thinking..."):
                result = text_generator(question, max_length=100)
                st.success(result[0]["generated_text"])
        else:
            st.warning("Please enter a question")

# ---------------- MCQ Generator ----------------
elif menu == "Generate MCQs":
    topic = st.text_input("Enter topic for MCQs")

    if st.button("Generate MCQs"):
        if topic.strip():
            prompt = f"Generate 5 multiple choice questions on {topic}."
            result = text_generator(prompt, max_length=200)
            st.success(result[0]["generated_text"])
        else:
            st.warning("Please enter a topic")
