from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


myfile = open("NASA_access_log_Jul95", "r")

ip_address= []

try:
    for line in myfile:
    
        ip_address.append(line.split(" ")[0])

except:
   print("uh oh")

print(ip_address)

c = Counter(ip_address)

newDict = dict()

for key, value in c.items():
    if value >=500:
        newDict[key] = value


print(newDict.keys())
print(newDict.values())

barWidth = 0.9

plt.bar(newDict.keys(), newDict.values(), width = barWidth, color = (0.3,0.1,0.4,0.6))

 
# Create bars
barWidth = 0.9
bars1 = [3, 3, 1]
bars2 = [4, 2, 3]
bars3 = [4, 6, 7, 10, 4, 4]
bars4 = bars1 + bars2 + bars3
 
# The X position of bars
r1 = [1,5,9]
r2 = [2,6,10]
r3 = [3,4,7,8,11,12]
r4 = r1 + r2 + r3
 
# Create legend
plt.legend()

plt.xticks(rotation=30, ha='right')

plt.show()

b = ip_address

plt.xticks(rotation=30)

print(newDict)

plt.show()

print(newDict)
