#include <iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter n: ";
    cin>>n;
    int count=1;
    for(int i=0;i<n;i++){
        for(int space = 0; space<n-i-1;space++){
            cout<<" ";
        }
        for(int j=0;j<count;j++){
            cout<<"*";
        }

        count=count+2;
        cout<<endl;
    }
    return 0;
}
