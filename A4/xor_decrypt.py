# want to use bitwise XOR to decrypt the message
import numpy as np

# open output_xor.txt
with open('output_xor.txt', 'r') as f:
    output_xor = f.read().split("\n")

output_xor = np.array(output_xor)

with open('output1_binary.txt', 'r') as f:
    output1 = f.read().split("\n")

output1 = np.array(output1)

# final permutation used in encryption
global_permutation = [57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7,58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8]

expansion = [32, 1, 2, 3, 4, 5, 4, 5,6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

permutation = [9, 17, 23, 31, 13, 28, 2, 18, 24, 16, 30, 6, 26, 20, 10, 1, 8, 14, 25, 3, 4, 29, 11, 19, 32, 12, 22, 7, 5, 27, 15, 21]

#apply global_permutation on output_xor array and store it in L6R6

L6R6 = []
actual_L6R6 = []

# for i in range(len(output_xor)-1):
#     # print(i)
#     temp = ''
#     temp1 = ''
#     for j in global_permutation:
#         # print(j)
#         temp = temp + output_xor[i][j-1]
#         temp1 = temp1 + output1[i][j-1]
#     L6R6.append(temp)
#     actual_L6R6.append(temp1)

for i in range(len(output_xor)-1):
    # print(i)
    temp = np.zeros(64)
    temp1 = np.zeros(64)
    for j in range(len(global_permutation)):
        # print(j)
        temp[j] = output_xor[i][global_permutation[j]-1]
        temp1[j] = output1[i][global_permutation[j]-1]
    
    # print(temp)

    temp = ''.join(str(int(x)) for x in temp)
    temp1 = ''.join(str(int(x)) for x in temp1)
    L6R6.append(temp)
    actual_L6R6.append(temp1)

print(L6R6[0][48] is output_xor[0][2])

L6 = []
R6 = []
actual_L6 = []

for i in range(len(L6R6)):
    L6.append(L6R6[i][:32])
    actual_L6.append(actual_L6R6[i][:32])
    R6.append(L6R6[i][32:])

# print(len(R6))

R5 = L6
actual_R5 = actual_L6

# print(R5)
# print("")

E6 = []
actual_E6 = []

for i in range(len(R5)):
    temp = ''
    temp1 = ''
    for j in expansion:
        temp = temp + R5[i][j-1]
        temp1 = temp1 + actual_R5[i][j-1]
    E6.append(temp)
    actual_E6.append(temp1)

# print(E6)

# with probability 0.   Xor of L5 = "00000100000000000000000000000000" for every case

L5 = "00000100000000000000000000000000"

P6 = []

for j in range(len(R6)):
    temp = ''
    for i in range(32):
        temp = temp + str(int(R6[j][i]) ^ int(L5[i]))
    P6.append(temp)

# print(P6)

S6 = []

# try1

# for i in range(len(P6)):
#     # print(i)
#     temp = ''
#     for j in permutation:
#         temp = temp + P6[i][j-1]
#     S6.append(temp)

# try2

# for i in range(len(P6)):
#     # print(i)
#     temp = np.zeros(64)
#     for j in range(len(permutation)):
#         # print(j)
#         temp[permutation[j]-1] = P6[i][j]
#     temp = ''.join(str(int(x)) for x in temp)
#     S6.append(temp)

#  try3

for i in range(len(P6)):
    # print(i)
    temp = np.zeros(64)
    for j in range(len(permutation)):
        # print(j)
        temp[j] = P6[i][permutation[j]-1]
    temp = ''.join(str(int(x)) for x in temp)
    S6.append(temp)

# print(S6)

with open('input_xor_sbox.txt', 'w') as f:
    for i in range(len(E6)):
        f.write(E6[i])
        f.write("\n")

with open('output_xor_sbox.txt', 'w') as f:
    for i in range(len(S6)):
        f.write(S6[i])
        f.write("\n")

with open('expansion1.txt', 'w') as f:
    for i in range(len(actual_E6)):
        f.write(actual_E6[i])
        f.write("\n")

# print(E6)
# print()
# print(actual_E6)