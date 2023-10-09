import numpy as np

# we store all S boxes
S_boxes = [
    [
    [14, 4,13, 1, 2,15,11, 8, 3,10, 6,12, 5, 9, 0, 7],
    [ 0,15, 7, 4,14, 2,13, 1,10, 6,12,11, 9, 5, 3, 8],
    [ 4, 1,14, 8,13, 6, 2,11,15,12, 9, 7, 3,10, 5, 0], # S box 1
    [15,12, 8, 2, 4, 9, 1, 7, 5,11, 3,14,10, 0, 6,13]
    ],

    [
    [15, 1, 8,14, 6,11, 3, 4, 9, 7, 2,13,12, 0, 5,10],
    [ 3,13, 4, 7,15, 2, 8,14,12, 0, 1,10, 6, 9,11, 5],
    [ 0,14, 7,11,10, 4,13, 1, 5, 8,12, 6, 9, 3, 2,15],   # S box 2
    [13, 8,10, 1, 3,15, 4, 2,11, 6, 7,12, 0, 5,14, 9]
    ],

    [
    [10, 0, 9,14, 6, 3,15, 5, 1,13,12, 7,11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6,10, 2, 8, 5,14,12,11,15, 1],
    [13, 6, 4, 9, 8,15, 3, 0,11, 1, 2,12, 5,10,14, 7],  # S box 3
    [ 1,10,13, 0, 6, 9, 8, 7, 4,15,14, 3,11, 5, 2,12]
    ],

    [
    [ 7,13,14, 3, 0, 6, 9,10, 1, 2, 8, 5,11,12, 4,15],
    [13, 8,11, 5, 6,15, 0, 3, 4, 7, 2,12, 1,10,14, 9],
    [10, 6, 9, 0,12,11, 7,13,15, 1, 3,14, 5, 2, 8, 4], # S box 4
    [ 3,15, 0, 6,10, 1,13, 8, 9, 4, 5,11,12, 7, 2,14]
    ],

    [
    [ 2,12, 4, 1, 7,10,11, 6, 8, 5, 3,15,13, 0,14, 9],
    [14,11, 2,12, 4, 7,13, 1, 5, 0,15,10, 3, 9, 8, 6],
    [ 4, 2, 1,11,10,13, 7, 8,15, 9,12, 5, 6, 3, 0,14], # S box 5
    [11, 8,12, 7, 1,14, 2,13, 6,15, 0, 9,10, 4, 5, 3]
    ],

    [
    [12, 1,10,15, 9, 2, 6, 8, 0,13, 3, 4,14, 7, 5,11],
    [10,15, 4, 2, 7,12, 9, 5, 6, 1,13,14, 0,11, 3, 8],
    [ 9,14,15, 5, 2, 8,12, 3, 7, 0, 4,10, 1,13,11, 6],  # S box 6
    [ 4, 3, 2,12, 9, 5,15,10,11,14, 1, 7, 6, 0, 8,13]
    ],

    [
    [ 4,11, 2,14,15, 0, 8,13, 3,12, 9, 7, 5,10, 6, 1],
    [13, 0,11, 7, 4, 9, 1,10,14, 3, 5,12, 2,15, 8, 6],
    [ 1, 4,11,13,12, 3, 7,14,10,15, 6, 8, 0, 5, 9, 2], # S box 7
    [ 6,11,13, 8, 1, 4,10, 7, 9, 5, 0,15,14, 2, 3,12]
    ],

    [
    [13, 2, 8, 4, 6,15,11, 1,10, 9, 3,14, 5, 0,12, 7],
    [ 1,15,13, 8,10, 3, 7, 4,12, 5, 6,11, 0,14, 9, 2],
    [ 7,11, 4, 1, 9,12,14, 2, 0, 6,10,13,15, 3, 5, 8], # S box 8
    [ 2, 1,14, 7, 4,10, 8,13,15,12, 9, 0, 3, 5, 6,11]
    ]
    
]

InputXor_S = open("input_xor_sbox.txt").read().split('\n')
OutputXor_S = open("output_xor_sbox.txt").read().split('\n')
OutputXor_Exp = open("expansion1.txt").read().split('\n')

counter_keys = np.zeros((64, 8)) # 64 probable keys corresponding to each S-box, and total of 8 S boxes

for i in range(len(InputXor_S)//10):
    # if(InputXor_S[i]==''):
    #     continue
    if(i%1000==0):
        print("Iteration : ", i)
    currentinpxor = InputXor_S[i]
    currentoutxor = OutputXor_S[i]
    expansion_input_first = OutputXor_Exp[i]
    for j in range(8): # iterating over the S-boxes

        # generate inputs which have currentinputxor = currentinpxor.  (input means input to the S boxes)
        # if their xor of the output of S boxes = currentoutxor, we increment counter of expansion_input_first XOR (value of input 1 generated)
        
        input_xor_to_Sbox  = int(currentinpxor[6*j:6+6*j], 2)
        output_xor_of_Sbox = int(currentoutxor[4*j:4+4*j], 2)
        after_exp          = int(expansion_input_first[6*j:6+6*j], 2)

        for k in range(64): # the inputs are k, k^(input_xor_to_the_Sbox) to the jth S box
            
            # row is determined by the first and last bits of inputs, column by the middle 4 bits of input
            i1 = k
            i2 = int(k^input_xor_to_Sbox)
            a0 = (i1 & (1<<0))>>0
            a1 = (i1 & (1<<1))>>1
            a2 = (i1 & (1<<2))>>2
            a3 = (i1 & (1<<3))>>3
            a4 = (i1 & (1<<4))>>4
            a5 = (i1 & (1<<5))>>5
            
            b0 = (i2 & (1<<0))>>0
            b1 = (i2 & (1<<1))>>1
            b2 = (i2 & (1<<2))>>2
            b3 = (i2 & (1<<3))>>3
            b4 = (i2 & (1<<4))>>4
            b5 = (i2 & (1<<5))>>5

            row1 = 2*a5 + a0
            row2 = 2*b5 + b0
            col1 = a1 + 2*a2 + 4*a3 + 8*a4
            col2 = b1 + 2*b2 + 4*b3 + 8*b4

            calculated_output = int(S_boxes[j][row1][col1]^S_boxes[j][row2][col2])

            # check if output is the same, ie on input k, k^after_exp to jth Sbox, if output = output_xor_of_Sbox 
            if(output_xor_of_Sbox == calculated_output):
                probable_key = k^after_exp
                counter_keys[probable_key][j]+=1    # for jth S-box, increase the count of probable_key by 1 (key_cand is 6 bits long)


avg=[]
maxcount=[]
indices=[]
counter_keys_T = counter_keys.transpose()

print(counter_keys_T)

for i in counter_keys_T:
    avg.append(int(np.mean(i)))
    max_value = max(i)
    max_index = np.argmax(i)
    maxcount.append(max_value)
    indices.append(max_index)

print(avg)
print()
print(maxcount)
print()
print(indices)