file = open("devices.txt", "a")
while True:
    newItem = input("Enter device name: ")
    if newItem == "exit":
        print("=====================")
        print("All done!")
        break
    file.write(newItem + "\n")

file=open("devices.txt","r")
for item in file:
    item=item.strip()
    print("\n VIEW RESULT \n")
    print(item)
file.close()
