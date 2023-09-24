#include <iostream>
#include <string>

using namespace std;

int num;
string res = "DCBAE";

int main(void) {
    for(int i = 0; i < 3; i++){
        int ans = 0;
        for(int j = 0; j < 4; j++){
            cin >> num;
            ans += num;
        }
        cout << res[ans] << "\n";
    }
}