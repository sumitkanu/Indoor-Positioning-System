import time
import serial

signal_strength = {}

ser = serial.Serial('com12',115200)

ser.isOpen()

ser.write('AT\r\n')
time.sleep(2)
while ser.inWaiting()>0:
   print(ser.readline())

ser.write('AT+CWMODE=3\r\n')
time.sleep(2)
while ser.inWaiting()>0:
   print(ser.readline())

ser.write('AT+CWLAP\r\n')
time.sleep(2.5)
out=''
while ser.inWaiting()>0:
   out+=ser.read(1)
# To assigna values use statements like shown below
 signal_strength['a'] = -89
 signal_strength['b'] = -98
 signal_strength['c'] = -123
 signal_strength['d'] = -657
#values can be accessed using signal_strength[name_of_wifi]

print signal_strength
print out

