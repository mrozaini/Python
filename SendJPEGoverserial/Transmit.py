import serial
ser = serial.Serial("COM4",9600)

picklestring = open("image01.jpg","rb").read()
sizedata = str(len(picklestring))
print sizedata
data = sizedata+picklestring
ser.write(data)
