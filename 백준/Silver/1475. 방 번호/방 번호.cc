#include <iostream>
#include <string>

using namespace std;

int n, arr[10], ans;

int main(){
    cin >> n;
    
    string str1 = to_string(n);
    
    for(char c : str1) {
        arr[c - '0']++;
    }
    for(int i = 0; i < 10; i++){
        if(i == 6 || i == 9) continue;
        ans = max(ans, arr[i]);
    }
    ans = max(ans, (arr[6]+arr[9]+1)/2);
    cout << ans;
}