```
#include<stdio.h>
int main(){
    char a[]="e3nifIH9b_C@n@dH";
    for(int i=0;a[i]!='\0';i++){
        printf("%c",a[i]-i);
    }
    return 0;
}
```
对输出再base64解码即可.