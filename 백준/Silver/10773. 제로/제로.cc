#include <iostream>
#include <stack>

using namespace std;

int main(void) {
    int k;
    cin >> k;
    
    stack<int> st;
    while(k--){
        int n;
        cin >> n;
        
        if(n == 0){
            st.pop();
        }
        else st.push(n);
    }
    int ans = 0;
    while(!st.empty()){
        ans += st.top();
        st.pop();
    }
    cout << ans;
}