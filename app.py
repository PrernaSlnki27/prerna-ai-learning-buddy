
import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="AI Learning Buddy Prerna", page_icon="🎓")

st.title("🎓 Prerna – AI Learning Buddy")

topic = st.text_input("Enter a Topic")

option = st.selectbox(
  "Choose Activity",
[
    "Explain Concept",
    "Real-Life Example",
    "Generate Quiz",
    "Answer Feedback",
    "Full Learning Session"
]
)

question = ""
student_answer = ""

if option == "Answer Feedback":
    question = st.text_area("Enter Question")
    student_answer = st.text_area("Enter Student Answer")

if st.button("Generate"):

  if topic == "":
      st.warning("Please enter a topic.")
  else:

      if option == "Explain Concept":
          prompt = f"""
You are Prerna, a friendly and patient AI mentor.

Explain {topic} in simple language.

Requirements:
1. Assume the learner is a beginner.
2. Use easy words.
3. Give one real-life analogy.
4. Explain step-by-step.
5. Keep the explanation engaging.
6. End with one reflection question.
"""

      elif option == "Real-Life Example":
          prompt = f"""
You are Prerna, a friendly and patient AI mentor.

Teach the concept {topic} using a real-life example.

Requirements:
1. Give one realistic scenario.
2. Explain how the concept appears in that scenario.
3. Use simple language.
4. Mention why this concept is useful.
5. End with one quick practice question.
"""

      elif option == "Generate Quiz":
          prompt = f"""
You are Prerna, a friendly AI tutor.

Create 5 multiple-choice questions on {topic}.

Requirements:
1. Difficulty: Beginner.
2. Four options (A, B, C, D).
3. One correct answer.
4. Provide explanation after each answer.
5. Format neatly.
"""

      elif option == "Answer Feedback":
          prompt = f"""
    You are Prerna, a friendly and patient AI mentor.

    Question:
    {question}

    Student's Answer:
    {student_answer}

    Tasks:
    1. Determine whether the answer is correct, partially correct, or incorrect.
    2. Give encouraging feedback.
    3. If the answer is incorrect, explain the correct answer politely.
    4. Suggest one improvement tip.
    5. Keep the tone supportive and beginner-friendly.
    """

      elif option == "Full Learning Session":
          prompt = f"""
    You are Prerna, a friendly and patient AI mentor.

    Help a learner understand {topic}.

    Follow these steps:

    1. Greet the learner warmly.
    2. Ask about their current knowledge level.
    3. Explain the topic in simple language.
    4. Give one real-life example.
    5. Create 5 quiz questions.
    6. Provide answers and explanations.
    7. End with motivation and next learning steps.

    Use beginner-friendly language throughout.
    """

      else:
          prompt = topic

      response = model.generate_content(prompt)

      st.subheader("📖 Learning Output")
      st.markdown(response.text)

st.divider()

st.caption(
    "Built for Infosys AI EMPOW(H)ER Capstone Project | AI Learning Buddy: Prerna"
)
