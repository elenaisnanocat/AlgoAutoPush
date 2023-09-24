#include <iostream>
#include <algorithm>

using namespace std;

int arr[5], sum = 0;
    
int main(void) {
    for(int i = 0; i < 5; i++) {
        cin >> arr[i];
        sum += arr[i];
    }
    cout << sum / 5 << "\n";
    sort(arr, arr+5);
    cout << arr[2];
}