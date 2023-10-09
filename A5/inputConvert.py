outfile = open("inputs.txt","w+")
f = open(r"inputnew.txt")
lines = f.readlines()
lines = [line[:-1] for line in lines]
for i in range(8):
    for j in range(127):
        strr = lines[i*128+j]
        outfile.write(strr)
        outfile.write(" ")
    strr = lines[i*128 + 127]
    outfile.write(strr)
    outfile.write("\n")
outfile.close()
f.close()

outfile = open("outputs.txt","w+")
f = open(r"outputnew.txt")
lines = f.readlines()
lines = [line[:-1] for line in lines]
for i in range(8):
    for j in range(127):
        strr = lines[i*128+j]
        outfile.write(strr)
        outfile.write(" ")
    strr = lines[i*128 + 127]
    outfile.write(strr)
    outfile.write("\n")
outfile.close()
f.close()