import numpy as np

# output1.txt has encrypted message of input 1
# output2.txt has encrypted message of input 2
# to generate xor of two files

# dictionary which maps 'f' to "0000", 'g' to "0001", ... 'u' to "1111"
maping = {'f': "0000",
          'g': "0001",
          'h': "0010",
          'i': "0011",
          'j': "0100",
          'k': "0101",
          'l': "0110",
          'm': "0111",
          'n': "1000",
          'o': "1001",
          'p': "1010",
          'q': "1011",
          'r': "1100",
          's': "1101",
          't': "1110",
          'u': "1111"}

# read the files
with open('output1.txt', 'r') as f:
    output1 = f.read().split("\n")

with open('output2.txt', 'r') as f:
    output2 = f.read().split("\n")

output1 = np.array(output1)
output2 = np.array(output2)

output = []
out1 = []
out2 = []

for j in range(len(output1)):
    temp = ''
    for i in output1[j]:
        temp = temp + maping[i]
    out1.append(temp)

# print(out1)

for j in range(len(output2)):
    temp = ''
    for i in output2[j]:
        temp = temp + maping[i]
    out2.append(temp)

# print(out2)

for j in range(len(output1)):
    temp = ''
    for i in range(64):
        temp = temp + str(int(out1[j][i]) ^ int(out2[j][i]))
    output.append(temp)

# print(output)

# add the xor of the two files to a new file
with open('output_xor.txt', 'w') as f:
    for i in output:
        f.write(i)
        f.write("\n")

with open('output1_binary.txt', 'w') as f:
    for i in out1:
        f.write(i)
        f.write("\n")
