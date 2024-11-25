# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Generate random data for X, Y, and sizes
x = np.random.rand(50)  # 50 random values for X
y = np.random.rand(50)  # 50 random values for Y
sizes = np.random.rand(50) * 1000  # Generate random sizes scaled up to 1000

# Create a scatter plot with variable ball sizes
plt.scatter(x, y, s=sizes, alpha=0.5)

# Add a title and labels
plt.title("Scatter Plot with Variable Ball Sizes")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Display the plot
plt.show()