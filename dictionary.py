from collections import Counter
import matplotlib.pyplot as plt

fruits = [
"apple", 
"oranges","oranges",
"banana", "banana", "banana",
"grapes", "grapes","grapes","grapes",
]

fruit_counter = Counter(fruits)

print(fruit_counter.keys())
print(fruit_counter.values())

plt.bar(fruit_counter.keys(), fruit_counter.values())

plt.show()


