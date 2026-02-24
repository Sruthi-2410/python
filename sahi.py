import tkinter as tk
from tkinter import messagebox

career_database = {
    "Data Scientist": {
        "required_skills": ["python", "statistics", "machine learning", "data visualization"],
        "learning_path": [
            "Learn Python basics (variables, loops, functions)",
            "Study statistics and probability",
            "Take a machine learning course (e.g., Scikit-learn, TensorFlow)",
            "Practice with real-world datasets (Kaggle, etc.)",
            "Build a portfolio with data science projects"
        ]
    },
    "Web Developer": {
        "required_skills": ["html", "css", "javascript", "python", "frameworks"],
        "learning_path": [
            "Master HTML, CSS, and JavaScript",
            "Learn a frontend framework (React, Vue)",
            "Understand backend using Python (Flask/Django)",
            "Build full-stack web projects",
            "Deploy websites using GitHub & hosting platforms"
        ]
    },
    "Android Developer": {
        "required_skills": ["java", "kotlin", "android sdk", "ui design", "firebase"],
        "learning_path": [
            "Learn Java or Kotlin",
            "Understand Android SDK and components",
            "Design responsive UIs for different devices",
            "Integrate Firebase for backend services",
            "Publish apps to Google Play Store"
        ]
    },
    "AI Engineer": {
        "required_skills": ["python", "deep learning", "tensorflow", "nlp", "data processing"],
        "learning_path": [
            "Learn Python and its AI libraries",
            "Study deep learning concepts (CNN, RNN)",
            "Work with TensorFlow or PyTorch",
            "Explore Natural Language Processing (NLP)",
            "Build and train custom AI models"
        ]
    },
    "UI/UX Designer": {
        "required_skills": ["design principles", "figma", "adobe xd", "user research", "prototyping"],
        "learning_path": [
            "Understand design principles and color theory",
            "Learn Figma and Adobe XD",
            "Conduct user research and create personas",
            "Design wireframes and interactive prototypes",
            "Test designs and iterate based on feedback"
        ]
    }
}

def generate_learning_path(user_skills, career_interest):
    career_info = career_database.get(career_interest)
    if not career_info:
        return f"Sorry, career path for '{career_interest}' not found."

    required = set(career_info["required_skills"])
    user = set(skill.lower() for skill in user_skills)
    missing_skills = required - user

    if not missing_skills:
        return f"You already have all the required skills for {career_interest}!"

    path = career_info["learning_path"]
    return "\nTo become a " + career_interest + ", you should:\n\n" + "\n".join(f"- {step}" for step in path)

def on_submit():
    skills_input = skills_entry.get()
    career_input = career_entry.get()
    user_skills = [skill.strip().lower() for skill in skills_input.split(",")]
    career_interest = career_input.strip()

    result = generate_learning_path(user_skills, career_interest)
    messagebox.showinfo("Learning Path", result)

# GUI Setup
root = tk.Tk()
root.title("SkillMap - Learning Path Generator")
root.geometry("500x400")

heading = tk.Label(root, text="SkillMap: Career Learning Path Finder", font=("Arial", 16))
heading.pack(pady=10)

skills_label = tk.Label(root, text="Enter your current skills (comma-separated):")
skills_label.pack()
skills_entry = tk.Entry(root, width=50)
skills_entry.pack(pady=5)

career_label = tk.Label(root, text="Enter your career interest (e.g., Data Scientist, Web Developer):")
career_label.pack()
career_entry = tk.Entry(root, width=50)
career_entry.pack(pady=5)

submit_button = tk.Button(root, text="Generate Learning Path", command=on_submit)
submit_button.pack(pady=20)

root.mainloop()