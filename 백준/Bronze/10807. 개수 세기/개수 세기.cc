#include <iostream>

using namespace std;

int n, v, a[201];

int main(){
    cin >> n;
    
    while(n--){
        int t;
        cin >> t;
        a[t + 100]++;
    }
    cin >> v;
    cout << a[v+100];
}