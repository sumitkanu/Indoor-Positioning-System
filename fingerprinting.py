import time
import serial
import numpy as np
ser = serial.Serial('com12',115200)
                                                      #reading the values


ser.write('AT\r\n')
time.sleep(2)
while ser.inWaiting()>0:
   print(ser.readline())

ser.write('AT+CWMODE=3\r\n')
time.sleep(2)
while ser.inWaiting()>0:
   print(ser.readline())


out=['','','','','','']
for i in range(6):
    ser.write('AT+CWLAP\r\n')
    time.sleep(2.5)
    while ser.inWaiting()>0:
        out[i]+=ser.read(1)
    print(out[i])
    time.sleep(10)

##########################################################################
wnum=4                                           #Detection and storage of RSSIs
calval=[]
import numpy as np
for i in range(len(out)):
    ilist=[]
    for j in range(wnum):
        ilist.append(99)
    calval.append(np.array(ilist))


port=["A","B","C","D"]
for j in range(len(out)):
    for i in range(len(out[j])):
        for k in range(wnum):
            if (out[j][i-1]=="\"" and out[j][i]==port[k] and out[j][i+1]=="\""):
                num=out[j][i+4:i+6]
                calval[j][k]=int(num);
        
                                                   
print(calval)
print("Reading done")
###############################################################################

time.sleep(5)                      #Positioning
p=np.arange(0,len(out))           #n is the no of nodes
currval=[99,99,99,99]
pout=''
ser.write('AT+CWLAP\r\n')
time.sleep(2.5)
while ser.inWaiting()>0:
   pout+=ser.read(1)
time.sleep(5)

port=["A","B","C","D"]

for i in range(len(pout)):
   for k in range(wnum):
      if (pout[i-1]=="\"" and pout[i]==port[k] and pout[i+1]=="\""):
            num=pout[i+4:i+6]
            currval[k]=int(num)
        
print (currval)


for i in range(len(out)):             
    for j in range(0, len(out)-i-1):
        if (np.sum(np.absolute(calval[j]-currval))>np.sum(np.absolute(calval[j+1]-currval))):
            calval[j],calval[j+1]=calval[j+1],calval[j]
            p[j],p[j+1]=p[j+1],p[j]
            
            


nearn=calval[:4]
pnear=p[0:4]

print(nearn)
print(pnear)

for i in range(4):             
    for j in range(0, 4-i-1):
        if (pnear[j]>pnear[j+1]):
            nearn[j],nearn[j+1]=nearn[j+1],nearn[j]
            pnear[j],pnear[j+1]=pnear[j+1],pnear[j]
print(pnear)


###############################################################################

                                                     #PLot
x=np.sum(np.abs(currval-nearn[0]))/np.sum(np.abs(nearn[1]-nearn[0]))
y=np.sum(np.abs(currval-nearn[0]))/np.sum(np.abs(nearn[2]-nearn[0]))

print(x,y)
