import serial
import cPickle
import time

ser = serial.Serial("COM4",9600)

#ser.write(open("image2.gif","rb").read())
#ser.write(open("image01.jpg","rb").read())

#serialization
picklestring = open("image01.jpg","rb").read()
sizedata = str(len(picklestring))
print sizedata
data = sizedata+picklestring
ts = time.time()
ser.write(data)
te = time.time()
print te-ts