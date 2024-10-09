import streamlit as st
import joblib
import numpy as np

# Load the pre-trained model
model = joblib.load('best_student_performance_model.pkl')

# Title and Description
st.title("Student Performance Prediction")
st.write("Enter the details of the student to predict if they will pass or not.")

# User input fields
study_hours = st.number_input("Study Hours per Week:", min_value=0, max_value=168, value=10)
attendance_rate = st.number_input("Attendance Rate (%):", min_value=0.0, max_value=100.0, value=75.0)
previous_grades = st.number_input("Previous Grades (0 - 100):", min_value=0, max_value=100, value=70)
activities = st.selectbox("Participation in Extracurricular Activities", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
parent_education = st.selectbox("Parent Education Level", options=[1, 2, 3, 4], format_func=lambda x: ["High School", "Bachelor", "Master", "Doctorate"][x-1])

# Prediction button
if st.button("Predict"):
    # Prepare input data
    input_data = np.array([[study_hours, attendance_rate, previous_grades, activities, parent_education]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display the result
    result = "Passed" if prediction == 1 else "Not Passed"
    st.write(f"The student is predicted to: **{result}**")
