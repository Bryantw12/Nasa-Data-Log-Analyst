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

print(c.keys())
print(c.values())

plt.bar(c.keys(), c.values())


plt.xticks(rotation=30)

plt.xticks(rotation=30, ha='right')
plt.show()

print(c)
