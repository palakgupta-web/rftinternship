import os
import pandas as pd
import streamlit as st

# Job required skills
required_skills = ["python", "sql", "pandas", "machine learning"]

results = []

# Read all resumes
for file in os.listdir("resumes"):

    if file.endswith(".txt"):

        with open("resumes/" + file, "r") as f:
            resume = f.read().lower()

        # Find matching skills
        found = []

        for skill in required_skills:
            if skill in resume:
                found.append(skill)

        # Missing skills
        missing = []

        for skill in required_skills:
            if skill not in found:
                missing.append(skill)

        # Calculate score
        score = len(found) / len(required_skills) * 100

        results.append([
            file.replace(".txt", ""),
            ", ".join(found),
            ", ".join(missing),
            score
        ])


# Create DataFrame
df = pd.DataFrame(
    results,
    columns=["Name", "Skills Found", "Missing Skills", "Match Score"]
)

# Rank candidates
df = df.sort_values("Match Score", ascending=False)

# Shortlist candidates
shortlisted = df[df["Match Score"] >= 50]

# Export CSV
shortlisted.to_csv("shortlisted_candidates.csv", index=False)

print("\nResume Screening Result:")
print(df)

print("\nShortlisted Candidates:")
print(shortlisted)

print("\nCSV file created successfully!")

#streamlit

st.title("AI Resume Screening Tool")

# Required skills
required_skills = ["python", "sql", "pandas", "machine learning"]

# Upload resume
file = st.file_uploader("Upload Resume", type=["txt"])

if file is not None:

    resume = file.read().decode("utf-8").lower()

    found = []
    missing = []

    # Check skills
    for skill in required_skills:
        if skill in resume:
            found.append(skill)
        else:
            missing.append(skill)

    # Calculate score
    score = len(found) / len(required_skills) * 100

    # Display result
    st.subheader("Resume Result")

    st.write("Skills Found:", ", ".join(found))
    st.write("Missing Skills:", ", ".join(missing))
    st.write("Match Score:", round(score, 2), "%")

    # Shortlist
    if score >= 50:
        st.success("Candidate Shortlisted!")
    else:
        st.error("Candidate Not Shortlisted!")