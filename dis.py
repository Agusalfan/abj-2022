ipAddress={"R1":"10.1.1.1", "R2":"10.1.1.2", "R3":"10.1.1.3"}
print(ipAddress)
print(type(ipAddress))
ipAddress["S1"]="192.168.1.1"
print(ipAddress)
ipAddress["R3"]=["10.1.1.3","10.0.0.3","192.168.1.3"]
print(ipAddress)