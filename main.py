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
    if value >=200:
        newDict[key] = value


print(newDict.keys())
print(newDict.values())

plt.bar(newDict.keys(), newDict.values())

b = ip_address

plt.xticks(rotation=30)

plt.xticks(rotation=30, ha='right')

print(newDict)

plt.show()

print(newDict)
