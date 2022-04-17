device=[]
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    device.append(item)
file.close()
print(device)