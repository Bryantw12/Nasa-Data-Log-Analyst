from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


myfile = open("NASA_access_log_Jul95", "r")

datetime= []

try:
    for line in myfile:
    
        datetime.append(line.split(" ")[6])

except:
   print("uh oh")

print(datetime)

c = Counter(datetime)

newDict = dict()

for key, value in c.items():
     if value >=2500:
        newDict[key] = value
   


print(newDict.keys())
print(newDict.values())



plt.show()
ax = plt.axes()
ax.set_facecolor("black")

plt.plot(newDict.keys(),newDict.values(),color = ("red"))


plt.xticks(rotation=30)

print(newDict)

plt.title("Most used files accessed from server")
plt.ylabel("Numbers of most files accessed")
plt.xlabel("Files")

plt.tick_params(axis='x', which='major', labelsize=6)
plt.show()

print(newDict)