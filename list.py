hostname=["R1","R2","R3","R4","R5"]
print(type(hostname))
print(len(hostname))
print(hostname)
print(hostname[1])
print(hostname[-1])
hostname[0]= "RT1"
print(hostname)
del hostname[3]
print(hostname)