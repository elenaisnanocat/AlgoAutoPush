#include <iostream>
#include <string>
using namespace std;

int arr[2][26], ans;

int main(void) {
    string s1, s2;
    cin >> s1 >> s2;
   
    for(auto c : s1) arr[0][c - 'a']++;
    for(auto c : s2) arr[1][c - 'a']++;
    
    for(int i = 0; i < 26; i++) {
        ans += abs(arr[0][i] - arr[1][i]);
    }
    cout << ans;
}