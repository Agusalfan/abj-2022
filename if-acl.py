aclnum = int(input("What is Ipv4 ACL Number? "))
if aclnum >= 1 and aclnum <= 99:
    print("This is a standart IPv4 Acl.")
elif aclnum >= 100 and aclnum <= 199:
    print("This is an extended IPv4 Acl.")
else:
    print("This is not standard or extended IPv4 ACL.")