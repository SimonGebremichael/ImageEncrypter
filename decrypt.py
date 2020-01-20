import glob
import os
key = 1

if str(os.access('data.txt', os.R_OK)) == "True":
    for file in glob.glob("*.*"):
    
        if os.path.splitext(file)[1] == ".PNG" or os.path.splitext(file)[1] == ".jpg":

            with open(file, "r+b") as data:

                pic = data.read()
                pic = bytearray(pic)
                print("Decrypting img file: " + os.path.splitext(file)[0] + os.path.splitext(file)[1])

                for index, value in enumerate(pic):
                    if value < 200: pic[index] = value - key
                    else: pic[index] = value + key

            da = open(file,"wb")
            da.write(pic)
            da.close()

            os.remove("data.txt")
else:
    print("nothing to decrypt...")
    input()

