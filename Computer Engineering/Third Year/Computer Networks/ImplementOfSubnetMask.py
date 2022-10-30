# Implementation of Subnet mask concept
# Find the complete Problem statement, and assignment at -
# https://www.gyaanibuddy.com/assignments/assignment-detail/ip-addressing-and-subnetting/

import math
address_cidr= input("Enter IP address in CIDR format: ")
a=address_cidr.split('/')
ip_address=a[0]
x=int(a[1])
flag = 0
count = 0
unused=0
unused=unused+pow(2,32-x)
ipLower = ""
ipHigher = ""
lower = []
higher = []
if len(ip_address) > 15:
    flag = 1
for i in ip_address:
    if i == ".":
        count = count + 1
if count != 3:
    flag = 1
octet = ip_address.split(".", 4)
for i in range(0, len(octet)):
    octet[i] = int(octet[i])
    if octet[i] > 255:
        flag = 1
created_mask = []
tmp = []
if flag == 0:
    print("Classless addressing")
    lower = []
    higher = []
    ipLower = ""
    ipHigher = ""
    for i in range(0, x):
        tmp.append("1")
    for i in range(x, 32):
        tmp.append("0")
    print("IP address in binary:")
    for i in octet:
        print(format(int(i),'08b'),end="")
    print("\nSubnet address in binary:")
    for i in tmp:
        print(i,end="") 
    result = []
    for i in range(0, len(tmp), 8):
       result.append("".join(tmp[i:i+8]))
    for i in range(0, len(result)):
        created_mask.append(int(result[i], 2))#int(num,2) for binary to decimal
    print("\nComplement of Subnet address in binary:")
    for i in range(0, len(created_mask)):
        print(format(int(255 - created_mask[i]),'08b'),end="")
    for i in range(0, len(octet)):
        lower.append(str(octet[i] & created_mask[i])) #and operation for 1st address
    ipLower = ipLower + lower[0] + "." + lower[1] + "." + lower[2] + "." + lower[3]
    print("\nThe First address: " + ipLower)
    for i in range(0, len(octet)):
        higher.append(str(octet[i] | (255 - created_mask[i])))# or operation with ip address and complement of subnet
    ipHigher = ipHigher + higher[0] + "." + higher[1] + "." + higher[2] + "." + higher[3]
    print("The Last address: " + ipHigher)

    print()
    n = int(input("\nEnter number of sub blocks: "))
    number = int(input("\nEnter number of IP address required: "))
    b=0
    if(number>unused):
        b=1
    if(b==0):
        created_mask.clear()
        result.clear()
        tmp.clear()
        x = 0
        while 2 ** x < number:
            x = x + 1
        unused=unused-pow(2,x)
        print(f"Mask: /{32-x}")
        for i in range(0, 32-x):
            tmp.append("1")
        for i in range(32-x, 32):
            tmp.append("0")
        for i in range(0, len(tmp), 8):
            result.append("".join(tmp[i:i + 8]))
        for i in range(0, len(result)):
            created_mask.append(int(result[i], 2))
        for i in range(0, len(lower)):
            lower[i] = int(lower[i])
        for i in range(0, len(higher)):
            higher[i] = int(higher[i])
        subblockLower = []
        subblockHigher = []
        ipLower = ""
        ipHigher = ""
        for i in range(0, len(lower)):
            subblockLower.append(lower[i])
        print("For Sub block 1:")
        for j in range(0, len(subblockLower)):
            subblockHigher.append(int(subblockLower[j]) | (255 - created_mask[j]))
        ipLower = ipLower + str(subblockLower[0]) + "." + str(subblockLower[1]) + "." + str(subblockLower[2]) + "." + str(subblockLower[3])
        ipHigher = ipHigher + str(subblockHigher[0]) + "." + str(subblockHigher[1]) + "." + str(subblockHigher[2]) + "." + str(subblockHigher[3])
        print(f"First address: {ipLower}")
        print(f"Last address: {ipHigher}")
        for k in range(1,n):
            b=0
            number = int(input("\nEnter number of IP address required: "))
            if(number>unused):
                b=1
            if(b==0):
                created_mask.clear()
                result.clear()
                tmp.clear()
                x = 0
                while 2 ** x < number:
                    x = x + 1
                unused=unused-pow(2,x)
                print(f"Mask:/{32-x}")
                for i in range(0, 32-x):
                    tmp.append("1")
                for i in range(32-x, 32):
                    tmp.append("0")
                for i in range(0, len(tmp), 8):
                    result.append("".join(tmp[i:i + 8]))
                for i in range(0, len(result)):
                    created_mask.append(int(result[i], 2))
                for i in range(0, len(lower)):
                    lower[i] = int(lower[i])
                for i in range(0, len(higher)):
                    higher[i] = int(higher[i])

                subblockLower[3] = subblockHigher[3] + 1
                if subblockLower[3] > 255:
                    subblockLower[3] = 0
                    subblockLower[2] = subblockLower[2] + 1
                    if subblockLower[2] > 255:
                        subblockLower[2] = 0
                        subblockLower[1] = subblockLower[1] + 1
                        if subblockLower[1] > 255:
                            subblockLower[2] = 0
                            subblockLower[1] = subblockLower[1] + 1
                subblockHigher = []
                ipLower = ""
                ipHigher = ""
                for j in range(0, len(subblockLower)):
                    subblockHigher.append(int(subblockLower[j]) | (255 - created_mask[j]))
                ipLower = ipLower + str(subblockLower[0]) + "." + str(subblockLower[1]) + "." + str(
                    subblockLower[2]) + "." + str(subblockLower[3])
                ipHigher = ipHigher + str(subblockHigher[0]) + "." + str(subblockHigher[1]) + "." + str(
                    subblockHigher[2]) + "." + str(subblockHigher[3])
                print(f"For Sub block: {k+1}")
                print(f"First address: {ipLower}")
                print(f"Last address: {ipHigher}")
            else:
                print("Required no of addresses not available")
    else:
        print("Required no of addresses not available")
    print()
    print(f"Unused addresses: {unused}")
