import matplotlib.pyplot as plt
with open('test.txt', 'r') as file:
    lines = file.readlines()

# Assume first 4 lines are x-axis values and the next 4 lines are y-axis values
x = [int(lines[i].strip()) for i in range(4)]  # First 4 lines for x values
y = [float(lines[i+4].strip()) for i in range(4)]  # Next 4 lines for y values

# Create a line plot
plt.plot(x, y, marker='o')

# Add labels and title
plt.xlabel('x-axis')  # Label for x-axis
plt.ylabel('y-axis')  # Label for y-axis
plt.title('Sample graph!')  # Title of the plot

# Display the plot
plt.show()