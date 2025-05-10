import streamlit as st
import random
import time
from fpdf import FPDF

# List of motivational quotes
quotes = [
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Success is the sum of small efforts, repeated day in and day out.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "You are capable of more than you know.",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."
]

# Title of the app
st.title("Smart Study Scheduler")

# Input fields for subjects and study hours
subjects = st.text_area("Enter the subjects (separate with commas):", "Math, Science, History")
study_hours = st.text_area("Enter study hours for each subject (separate with commas):", "2, 3, 1")

# Convert the inputs to lists
subjects = [sub.strip() for sub in subjects.split(',')]
study_hours = [int(hour.strip()) for hour in study_hours.split(',')]

# Time available for study
total_study_time = st.number_input("Total available study time (in hours):", min_value=1, max_value=12, value=6)

# Weightage for subjects (e.g., how difficult each subject is, scale 1-10)
weightage = st.text_area("Enter the weightage of subjects (1-10, separate with commas):", "8, 7, 5")
weightage = [int(weight.strip()) for weight in weightage.split(',')]

# Display inputs
st.write("Subjects:", subjects)
st.write("Study Hours:", study_hours)
st.write("Weightage (Difficulty):", weightage)
st.write("Total Study Time:", total_study_time, "hours")

# Calculate total study hours needed
total_needed_hours = sum(study_hours)

# Adjust study hours based on available time
if total_needed_hours <= total_study_time:
    st.write("You have enough time to study all subjects!")
    adjusted_study_hours = study_hours
else:
    scaling_factor = total_study_time / total_needed_hours
    adjusted_study_hours = [round(hour * scaling_factor, 2) for hour in study_hours]
    st.write("Study hours have been adjusted based on available time.")

# Adjust hours according to weightage (priority to harder subjects)
weighted_study_hours = [
    round(adjusted_study_hours[i] * (weightage[i] / max(weightage)), 2) for i in range(len(weightage))
]

# Display the study schedule
schedule = zip(subjects, weighted_study_hours)
st.write("Your Adjusted Study Schedule:")
for subject, hours in schedule:
    st.write(f"{subject}: {hours} hours")

# Show motivational quote
st.write("Motivational Quote for You:")
st.write(random.choice(quotes))

# Pomodoro Timer (25 minutes study, 5 minutes break)
pomodoro_time = 25  # study time in minutes
break_time = 5  # break time in minutes

if st.button("Start Pomodoro Timer"):
    st.write("Pomodoro Timer Started! Study for 25 minutes.")
    for i in range(pomodoro_time, 0, -1):
        st.write(f"Time remaining: {i} minutes")
        time.sleep(60)  # Wait for 1 minute
    st.write("Take a 5-minute break!")
    for i in range(break_time, 0, -1):
        st.write(f"Break time remaining: {i} minutes")
        time.sleep(60)  # Wait for 1 minute
    st.write("Pomodoro session completed! Back to study.")

# Export schedule to PDF
def create_pdf(schedule):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Smart Study Scheduler - Your Schedule", ln=True, align="C")
    
    for subject, hours in schedule:
        pdf.cell(200, 10, txt=f"{subject}: {hours} hours", ln=True)
    
    pdf.output("study_schedule.pdf")
    st.write("Your schedule has been exported to PDF.")
    st.download_button(label="Download PDF", data=open("study_schedule.pdf", "rb").read(), file_name="study_schedule.pdf")

# Add button to generate and download PDF
if st.button("Generate and Export Schedule as PDF"):
    create_pdf(zip(subjects, weighted_study_hours))

# Show progress bar based on study completion
progress = sum(weighted_study_hours) / total_study_time
st.progress(progress)
