# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Generate random data for X and Y
x = np.random.rand(50)  # 50 random values for X
y = np.random.rand(50)  # 50 random values for Y

# Create a scatter plot
plt.scatter(x, y)

# Add a title and labels
plt.title("Scatter Plot of Random Distribution")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Display the plot
plt.show()