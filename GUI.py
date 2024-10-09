import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Load the trained model
model = joblib.load('best_student_performance_model.pkl')

# Initialize the main window
root = tk.Tk()
root.title("Student Performance Prediction")
root.geometry("400x500")

# Create input fields and labels
tk.Label(root, text="Study Hours per Week:").pack()
study_hours_entry = tk.Entry(root)
study_hours_entry.pack()

tk.Label(root, text="Attendance Rate (%):").pack()
attendance_entry = tk.Entry(root)
attendance_entry.pack()

tk.Label(root, text="Previous Grades (0 - 100):").pack()
grades_entry = tk.Entry(root)
grades_entry.pack()

tk.Label(root, text="Participation in Extracurricular Activities (1 for Yes, 0 for No):").pack()
activities_entry = tk.Entry(root)
activities_entry.pack()

tk.Label(root, text="Parent Education Level (1 - High School, 2 - Bachelor, 3 - Master, 4 - Doctorate):").pack()
parent_education_entry = tk.Entry(root)
parent_education_entry.pack()

# Function to make predictions
def predict():
    try:
        # Get input values
        study_hours = float(study_hours_entry.get())
        attendance = float(attendance_entry.get())
        grades = float(grades_entry.get())
        activities = int(activities_entry.get())
        parent_education = int(parent_education_entry.get())

        # Prepare the input data for prediction
        input_data = np.array([[study_hours, attendance, grades, activities, parent_education]])
        
        # Make a prediction
        prediction = model.predict(input_data)[0]
        result = "Passed" if prediction == 1 else "Not Passed"
        
        # Display the prediction result
        messagebox.showinfo("Prediction Result", f"The student is predicted to: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid input values.")

# Create a prediction button
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.pack(pady=20)

# Run the application
root.mainloop()
