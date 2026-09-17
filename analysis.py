import pandas as pd

# Load the student dataset
data = pd.read_csv("students.csv")

# Display the data
print("Student Performance:")
print(data)

# Calculate average marks
subjects = ["Python", "SQL", "Maths", "English"]
data["Average"] = data[subjects].mean(axis=1)

# Display average marks
print("\nAverage Marks:")
print(data[["Name", "Average"]])

# Find the top-performing student
top_student = data.loc[data["Average"].idxmax()]

print("\nTop Performing Student:")
print(top_student["Name"])
print("Average:", round(top_student["Average"], 2))
