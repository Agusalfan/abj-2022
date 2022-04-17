device=["R1","R2","R3","S4","S5"]
for item in device:
    print(item)

print("=====================")
for item in device:
    if "R" in item:
        print(item)
        
print("=====================")      
switches=[]
for item in device:
    if "S" in item:
        switches.append(item)
        
print(switches)