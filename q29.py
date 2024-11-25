import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ['red', 'black', 'green', 'blue', 'yellow', 'cyan']

plt.bar(languages, popularity, color=colors)
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title('Popularity of Programming Language\nWorldwide, Oct 2017 compared to a year ago')
plt.grid(axis='y', linestyle='--', color='red', alpha=0.7)
plt.tight_layout()
plt.show()