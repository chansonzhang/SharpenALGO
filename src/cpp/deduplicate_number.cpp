# include <iostream>
using namespace  std;

int main(){
    int a;
    int b[10]={0};
    cin >> a;
    while (a%10!=0){
        if(b[a%10]==0){
            b[a%10] = 1;
            cout<<a%10;
        }
        a = a/10;
    }
    return 0;
}