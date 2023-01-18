from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


myfile = open("NASA_access_log_Jul95", "r")

datetime= []

try:
    for line in myfile:
    
        datetime.append(line.split(" ")[3])

except:
   print("uh oh")

print(datetime)

c = Counter(datetime)

newDict = dict()

for key, value in c.items():
    newDict[key] = value


print(newDict.keys())
print(newDict.values())

barWidth = 0.9

# plt.bar(newDict.keys(), newDict.values(), width = barWidth, color = (0.3,0.1,0.4,0.6))

 

# Plot
plt.plot(newDict.keys['Date'],newDict.values['Temp'])







plt.xticks(rotation=30)


print(newDict)

plt.show()

print(newDict)
