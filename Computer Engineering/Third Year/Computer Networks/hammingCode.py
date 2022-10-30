# To implement Layer 2 Error Control schemes: Hamming Codes.
# Find the complete Problem statement, and assignment at -
# https://www.gyaanibuddy.com/assignments/assignment-detail/error-correction-and-detection-hamming-code/


def calRedundantBits(k):
   for i in range(k): 
      if(2**i >= k + i + 1): 
         return i 

def insertRedundantBits(datawordBits,pow_of_two,m):
   cw=[]
   x=0
   for j in range(m):
      if j+1 in pow_of_two:
         cw.append(0)
      else:
         cw.append(datawordBits[-1*(x+1)])
         x=x+1
   return cw[::-1] 

def calParityBits(codewordBits,r,pow_of_two):
   codewordBits_temp=codewordBits[::-1] 
   list1=[]
   for i in range(r):
      list2=[]
      x=0
      p=pow_of_two[i]
      s=p-1
      while s<=len(codewordBits):
         list2.extend(codewordBits_temp[s:s+p])
         s=s+2*p
      for val in list2:
         x=x^val
      list1.append(x)
   return list1[::-1]

datawordBits=[]
print("------------------SENDER'S SIDE------------------------")
k=int(input('Enter size of dataword k:'))
datawordBits=list(map(int,input("Enter dataword bits:").split(" ")))

r=calRedundantBits(k)
m=k+r
print('Number of redundant bits r:',r)
print('Number of codeword bits m :',m)

pow_of_two=[]
for i in range (r):
   pow_of_two.append(2**i)

codewordBits=[]
codewordBits=insertRedundantBits(datawordBits,pow_of_two,m)

rFound1=calParityBits(codewordBits,r,pow_of_two)
for i in range(r):
   codewordBits[-1*pow_of_two[i]]=rFound1[-1*(i+1)]
print('redundant bits:',rFound1)
x=0
for i in range(r):
   print("r",pow_of_two[-1*(x+1)],":",rFound1[i])
   x+=1
print('Codeword sent:',codewordBits)
codewordBits.clear()

print("------------------RECEIVER'S SIDE------------------------")
codewordBits=list(map(int,input("Enter the received codeword:").split(" ")))

rFound2=calParityBits(codewordBits,r,pow_of_two)

print('redundant bits:')
syndrome=""
x=0
for i in range(r):
   print("r",pow_of_two[-1*(x+1)],":",rFound2[i])
   x+=1
print('Syndrome:',rFound2)

position=0
for i in range(r):
  position+=rFound2[-1*(i+1)]*(2**i)
if(position==0):
   print("No error detected")
else:
   print("Error detected at position at:",position)
   if(codewordBits[-1*position]==0):
      codewordBits[-1*position]=1
   else:
      codewordBits[-1*position]=0
   print('Corrected Codeword bits:',codewordBits)
x=0
final_dataword=[]

for i in range(len(codewordBits)):
   if(i==(2**x-1)):
         x+=1
   else:
      final_dataword.append(codewordBits[-1*(i+1)])  
print('Final Corrected datword:',final_dataword[::-1])
