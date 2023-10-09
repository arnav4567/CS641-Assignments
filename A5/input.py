import numpy as np

mapping = {}
for i in range(16):
    num = '{:0>4}'.format(format(i, "b"))
    numi = int(num[3]) + 2 * int(num[2]) + int(num[1]) * 4 + int(num[0]) * 8
    mapping[num] = chr(ord('f') + numi)

with open("inputnew.txt", "w+") as file:
    for i in range(8):
        for j in range(128):
            x = np.binary_repr(j, width=8)
            strr = 'ff' * i + mapping[x[:4]] + mapping[x[4:]] + 'ff' * (8 - i - 1)
            file.write(strr)
            file.write("\n")