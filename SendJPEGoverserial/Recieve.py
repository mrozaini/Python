import serial
from PIL import Image

ser = serial.Serial("COM11",9600)

jpegdata =""
lendata =""
sizedata = 0
count =0

while True:
    bytedata = ser.read()
    #print bytedata
    if count<=3:
        lendata = lendata+bytedata
        if count==3:
           sizedata = int(lendata)
           print sizedata
    elif count>=4 and count<=(sizedata+3) :
        jpegdata = jpegdata+bytedata
        #print count
        if count == (sizedata+3):
                print len(jpegdata)
                jpegfile = open("1.jpg","wb")
                jpegfile.write(jpegdata);
                jpegfile.close()
                dimage = Image.open('1.jpg')
                dimage.show()
    count = count+1
