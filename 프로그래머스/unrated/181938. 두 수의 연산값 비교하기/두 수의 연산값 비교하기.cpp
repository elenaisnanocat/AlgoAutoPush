#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    int answer = 0;
    
    string str1 = to_string(a);
    string str2 = to_string(b);
    string ab;
    
    ab = str1 + str2;
    int abi = stoi(ab);
    if (abi >= 2 * a * b) {
        answer = abi;
    }
    else answer = 2 * a * b;
    
    return answer;
}