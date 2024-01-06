#include<iostream>
#include<unistd.h>

using namespace std;

int main(){
    char* s = new char[5];
    if(s == nullptr){
        cout<<"error";
        exit(1);
    }
    s[0] = 'A';
    s[1] = 'P';
    s[2] = 'P';
    s[3] = 'L';
    s[4] = 'E';
    s[5] = '$';
    s[6] = '%';
    int i = 0;
    while(s){
        
        cout<<i<<" "<<s<<" "<<(void*)s<<endl;
        sleep(1);
        i++;

    }
}