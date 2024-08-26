// Finding Largest and Second Largest Number Among Three...

#include <iostream>
using namespace std;

int main(){
    int a,b,c;
    cout<<"Enter Value For A: ";
    cin>>a;
    cout<<"Enter Value For B: ";
    cin>>b;
    cout<<"Enter Value For C: ";
    cin>>c;
    int biggest=(a>b&&a>c?a:(b>a&&b>c?b:c));
    int secbig=(a<biggest&&(a>b||a>c))?a:(b<biggest&&(b>a||b>c)?b:c);
    cout<<"This is Biggest "<<biggest<<endl;
    cout<<"This is Second Biggest "<<secbig<<endl;
    return 0;
}
