#include <iostream>
#include <list>

using namespace std;

int main(void) {
    int n, k;
    cin >> n >> k;
    
    list<int> lst;
    list<int>::iterator it = lst.begin();
    
    cout << '<';
    
    for(int i = 1; i <= n; ++i)
        lst.push_back(i);
    
    while(!lst.empty()){
        for(int i = 0; i < k; ++i){
            if(++it == lst.end())
                it = lst.begin();
        }
        cout << *it;
        it = --lst.erase(it);
        
        if(lst.empty()) cout << '>';
        else cout << ", ";
    }
    return 0;
}
