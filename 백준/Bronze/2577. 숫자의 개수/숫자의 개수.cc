#include <iostream>
#include <string>
using namespace std;

int a,b,c,sum;
int arr[10];    

int main(void) {
    cin >> a >> b >> c;
    sum = a * b * c;
    string str1 = to_string(sum);
    
    for(char chr : str1){
        arr[chr - '0']++;
    }
    for(int i : arr)
        cout << i << "\n";
}