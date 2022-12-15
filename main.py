from collections import Counter

myfile = open("NASA_access_log_Jul95", "r")

ip_address= []

try:
    for line in myfile:
    
        ip_address.append(line.split(" ")[0])

except:
   print("uh oh")

print(ip_address)

c = Counter(ip_address).most_common(3)

print(c)
