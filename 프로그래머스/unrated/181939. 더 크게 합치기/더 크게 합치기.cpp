#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    int answer = 0;
    string ab, ba;
    string str1 = to_string(a);
    string str2 = to_string(b);
    
    ab = str1 + str2;
    ba = str2 + str1;
    
    //cout << ab << ba;
    int abi = stoi(ab);
    int bai = stoi(ba);
    //cout << abi;
    if (abi >= bai) {
        answer = abi;
    }
    else {
        answer = bai;
    }
    
    return answer;
}