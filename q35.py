import matplotlib.pyplot as plt

# Define the data
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]  # Mathematics marks
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]  # Science marks
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Marks range (not used here)

# Create the scatter plot
plt.scatter(math_marks, science_marks)

# Add a title and labels
plt.title("Scatter Plot: Mathematics vs Science Marks")
plt.xlabel("Mathematics Marks")
plt.ylabel("Science Marks")

# Display the plot
plt.show()