```
#include<stdio.h>
int main(){
    char s[]="c61b68366edeb7bdce3c6820314b7498";
    for(int i=0;i<strlen(s);i++){
        if(i&1!=0){
            printf("%c",s[i]+1);
        }
        else{
            printf("%c",s[i]-1); 
        }
    }
    return 0;
}
```