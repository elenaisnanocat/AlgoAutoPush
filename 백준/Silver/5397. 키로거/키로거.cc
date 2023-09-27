#include <iostream>
#include <list>
#include <string>

using namespace std;

int main(void){
    int n;
    cin >> n;
    
    for(int i = 0; i < n; i++){
        list<char> L = {};
        string s;
        
        auto p = L.begin(); //L처음에 포인터
        cin >> s;
        for(auto c: s) {
            if (c == '<'){
                if(p != L.begin()) p--;
            }
            else if (c == '>'){
                if(p!= L.end()) p++;
            }
            else if (c == '-'){
                if(p!= L.begin()){
                    p--;
                    p = L.erase(p);
                }
            }
            else
                L.insert(p, c);
        }
        for (auto c : L) cout << c;
        cout << "\n";
    }
}