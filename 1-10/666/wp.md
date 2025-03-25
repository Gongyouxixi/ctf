```
#include<stdio.h>
int main(){
    char a[18]="izwhroz\"\"w\"v.K\".Ni";
    char b[18];
    for(int i=0;i<18;i+=3){
        b[i]=(a[i]^18)-6;
        b[i+1]=(a[i+1]^18)+6;
        b[i+2]=a[i+2]^18^6;
    }
    for(int i=0;i<18;i++){
        printf("%c",b[i]);
    }
    return 0;
}
```