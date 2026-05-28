import streamlit as st

from utils.extractor import (
    extract_text_from_pdf,
    extract_text_from_docx
)

from utils.preprocessing import preprocess_text

from utils.matcher import (
    calculate_similarity,
    extract_skills,
    predict_category
)

st.set_page_config(
    page_title="Resume Parser AI",
    layout="centered"
)

st.title("📄 Resume Parser AI + Job Match Scoring System")

st.write("Upload your resume and compare it with a job description.")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if uploaded_file and job_description:

    file_extension = uploaded_file.name.split(".")[-1]

    if file_extension == "pdf":
        resume_text = extract_text_from_pdf(uploaded_file)

    else:
        resume_text = extract_text_from_docx(uploaded_file)

    cleaned_resume = preprocess_text(resume_text)

    cleaned_jd = preprocess_text(job_description)

    similarity_score = calculate_similarity(
        cleaned_resume,
        cleaned_jd
    )

    extracted_skills = extract_skills(resume_text)

    predicted_category = predict_category(cleaned_resume)

    st.subheader("📊 Resume Match Score")

    st.progress(int(similarity_score))

    st.success(f"{similarity_score:.2f}% Match")

    st.subheader("🧠 Predicted Resume Category")

    st.info(predicted_category)

    st.subheader("🛠 Extracted Skills")

    st.write(extracted_skills)

    jd_words = set(cleaned_jd.split())

    resume_words = set(cleaned_resume.split())

    missing_keywords = jd_words - resume_words

    st.subheader("❌ Missing Keywords")

    st.write(list(missing_keywords)[:20])

    st.subheader("📃 Resume Preview")

    st.text(resume_text[:3000])