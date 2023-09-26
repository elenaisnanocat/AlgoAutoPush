#include <iostream>
#include <list>
#include <string>

using namespace std;

int main(void){
    string str;
    cin >> str;
    
    list<char> L;
    for(auto c : str) L.push_back(c);
    auto cursor = L.end();
    
    int n;
    cin >> n;
    while(n--){
        char option;
        cin >> option;
        
        if(option == 'P'){
            char add;
            cin >> add;
            L.insert(cursor, add);   
        }
        else if(option == 'L') {
            if (cursor != L.begin()) cursor--;
        }
        else if(option == 'D'){
            if (cursor != L.end()) cursor++;
        }
        else {
            if(cursor != L.begin()){
                cursor--;
                cursor = L.erase(cursor);
            }
        }
    }
    for(auto c : L)
        cout << c;
    
}