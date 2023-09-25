#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
    
    int arr[9] = {};
    for(int i = 0; i < 9; i++) {
        cin >> arr[i];
    }
    int max= *max_element(begin(arr), end(arr));
    
    cout << max << "\n";
    
    for(int i = 0; i < 9; i++){
        if(arr[i] == max) {
            cout << i + 1;
        }
    }
}