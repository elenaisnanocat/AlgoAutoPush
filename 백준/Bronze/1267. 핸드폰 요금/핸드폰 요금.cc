#include <iostream>
using namespace std;

int main(void) {
    int phone[10000];
    int ysum = 0, msum = 0, n;
    
    cin>> n;
    for (int i = 0; i < n; i++) {
        cin >> phone[i];
    }
    for(int i = 0; i< n; i++)
        ysum += ((phone[i] / 30) + 1) * 10;
    for(int i = 0; i < n; i++)
        msum += ((phone[i]/ 60) + 1) * 15;
    if(ysum < msum) cout << "Y " << ysum;
    else if (ysum > msum) cout << "M " << msum;
    else cout << "Y M " << ysum;
}