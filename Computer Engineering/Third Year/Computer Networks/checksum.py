s = str(input("Enter a string "))
a = []
for i in s:
    a.append(bin(ord(i)).replace("0b", ""))
print(a)
print(len(a[0]))

received=[]
for i in range(len(a)-1):
    received.append(bin(int(a[i],2) + int(a[i+1],2)).replace("0b", ""))
    if( len(received[i]) != len(a[i]) ):
        received[i]=bin(int(received[i],2)+1).replace("0b1","")
temp = ""
for j in range(7):
    if(received[i][j]=='0'):
        temp = temp + '1'
    elif(received[i][j]=='1'): 
        temp = temp + '0'
received.append(temp)
print(received)  
temp1 = temp

s = str(input("Enter the received string "))
b = []
for i in s:
    b.append(bin(ord(i)).replace("0b", ""))
print(b)
print(len(b[0]))

receiver=[]
for i in range(len(b)-1):
    receiver.append(bin(int(b[i],2) + int(b[i+1],2)).replace("0b", ""))
    if( len(receiver[i]) != len(b[i]) ):
        receiver[i]=bin(int(receiver[i],2)+1).replace("0b1","")

temp2 = receiver[i]
print(receiver)

temp3 = bin(int(temp1,2)+int(temp2,2)).replace("0b","") 
if(temp3=="1111111"):
    print('correct')
