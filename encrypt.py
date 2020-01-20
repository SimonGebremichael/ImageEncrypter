import glob
import os
key = 1

for file in glob.glob("*.*"):
    if os.path.splitext(file)[1] == ".PNG" or os.path.splitext(file)[1] == ".jpg":
              
        with open(file, "rb") as data:

            pic = data.read()
            pic = bytearray(pic)
            print("Encrypting img file: " + os.path.splitext(file)[0] + os.path.splitext(file)[1])

            for index, value in enumerate(pic):
                if value < 200: pic[index] = value + key
                else: pic[index] = value - key

        da = open(file,"wb")
        da.write(pic)
        da.close()

        da = open("data.txt","w")
        da.write("encrypt")
        da.close()

    else: 
        stri += str(os.path.splitext(file)[0]) + str(os.path.splitext(file)[1]) + ","

print("invalid Files Below:")
hold = stri.split(',')
for x in hold:
    print(x)
input()