#include <bits/stdc++.h>
using namespace std;
// Password obtained after substitution "tyRgU03diqq"
// The digits in the message have been shifted by '8' digits, so the '8' was originally 4. We subtract 4 from 0 and 3(mod 10)
// in the password to get the password as "tyRgU69diqq"

int main(){
    map<char,char> subs = {{'p','a'},{'P','A'}, {'M','T'}, {'m','t'}, {'i','c'},{'y','e'},{'e','h'},{'w','i'},
    {'a','s'},{'h','n'},{'g','o'},{'t','f'},{'s','r'},{'S','R'},{'b','v'},{'x','y'},{'n','u'},{'N','U'},{'r','g'},{'d','q'},{'v','w'},
    {'f','p'},{'u','d'},{'k','l'},{'j','m'},{'o','b'},{'A','S'}};
    string decr = "Mewa wa mey twsam iepjoys gt mey ipbya. Pa xgn iph ayy, meysy wa hgmewhr gt whmysyam wh mey iepjoys. Agjy gt mey kpmys iepjoysa vwkk oy jgsy whmysyamwhr meph mewa ghy! Mey iguy nayu tgs mewa jyaapry wa p awjfky anoamwmnmwgh iwfeys wh vewie uwrwma epby oyyh aewtmyu ox 8 fkpiya. Mey fpaavgsu wa 'mxSrN03uwdd' vwmegnm mey dngmya.";
    cout << endl << decr << endl;
    for(int i=0;i<decr.size();i++){
        if(subs.find(decr[i])==subs.end()){
            continue;
        }else decr[i]=subs[decr[i]];
    }
    cout << endl << decr << endl << endl;
}