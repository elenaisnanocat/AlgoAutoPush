#include <iostream>
#include <algorithm>

using namespace std;

int num[9], res[7];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    for(int i = 0; i < 9; i++) cin >> num[i];
    
    for(int a = 0; a<8; a++) {
        int total = 0;
        for(int b = a + 1; b < 9; b++) {
            total = 0;
            for (int c= 0, i = 0; c < 9; c++) 
                if (c!=a && c!= b)
                    res[i++] = num[c];
            for(int i = 0; i < 7; i++)
                total += res[i];
            if(total == 100) break;
        }
        if(total == 100) break;
    }
    sort(res, res+7);
    for(int i = 0; i < 7; i++)
        cout << res[i] << "\n";
}