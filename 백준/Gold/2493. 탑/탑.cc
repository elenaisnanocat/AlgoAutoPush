#include <iostream>
#include <stack>
#define x first
#define y second

using namespace std;

int n;
stack<pair<int,int>> tower;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin>>n;
    tower.push({100000001, 0});
    for(int i = 1; i <= n; ++i){
        int height;
        cin >> height;
        while(tower.top().x < height)
            tower.pop();
        cout << tower.top().y << " ";
        tower.push({height, i});
    }
}