import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("students.csv")

# Calculate average marks
subjects = ["Python", "SQL", "Maths", "English"]
data["Average"] = data[subjects].mean(axis=1)

# Create a bar chart
plt.bar(data["Name"], data["Average"])

plt.title("Student Average Performance")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.show()
