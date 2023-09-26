#include <iostream>

using namespace std;

int n, k, ans;
int stu[2][7]; //성별, 학년

int main(void) {
    cin >> n >> k;
    
    for(int i = 0; i < n; i++){
        int a, b;
        cin >> a >> b;
        stu[a][b]++;
    }
    
    for(int i = 0; i < 2; i++){
        for(int j = 1; j < 7; j++){
            ans += stu[i][j] / k;
            if(stu[i][j] % k) ans++;
        }
    }
    cout << ans;
}