import base64

with open('imgdmp.dat') as infile:
    a = infile.readline()
    bimg = base64.b64decode(a)

#print(bimg)
with open('tmpimg.jpg', 'wb') as outfile:
    outfile.write(bimg)


