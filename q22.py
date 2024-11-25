import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50] 
y = [160, 140, 120, 80, 60] 

plt.plot(x, y, marker='o')
plt.xlabel('x-axis')
plt.ylabel('y-axis') 
plt.title('Sample Line Plot') 
plt.show()