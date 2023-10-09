#include <bits/stdc++.h>
using namespace std;

const int TOT_INPUTS = 100000;
const int BLOCK_SIZE = 64;  //block size is 64 bits

//since 2 letters correspond to one byte(as told by the spirit), we map the 64-bit random-block generated to 16-lettered strings. 
const int NUM_LETTERS = BLOCK_SIZE/4; 
// const int input_xor[] = {0, 0, 0, 0, 9, 0, 2, 0, 1, 0, 0, 0, 5, 0, 0, 0};
const int input_xor[] = {4, 0, 5, 12, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0};

int main(){
    long long rndm;
    string one_inp,  one_inp_xor_char;//one_inp^characteristic = one_inp_xor_char 

    ofstream myfile1;
    myfile1.open ("input1.txt");

    ofstream myfile2;
    myfile2.open ("input2.txt");

    // srand(time(NULL));

    for(int n=0;n<TOT_INPUTS;n++){
        one_inp="";
        one_inp_xor_char="";
        for (int i=0;i<NUM_LETTERS;i++){
            //generate 4-bit strings and get corresponding letter
            int rndm = rand()%16;
            char temp1 = rndm + 'f';    //map 0000 to f, 0001 to g, 0010 to h ... 1111 to u
            char temp2 = (int)(rndm^(input_xor[i])) + 'f';
            one_inp+=temp1;
            one_inp_xor_char+=temp2;
        }
        myfile1<<one_inp<<"\n";
        myfile2<<one_inp_xor_char<<'\n';
    }
    myfile1.close();
    myfile2.close();
}