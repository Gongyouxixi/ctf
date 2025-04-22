```
#include <stdio.h>
#include <string.h>
int main(){
    char a[]="n=<;:h2<'?8:?'9hl9'h:l>'2>>2>hk=>;:?";
    char b[37];
    for(int i=0;a[i]!='\0';i++){
        b[i]=a[i]^10;
    }
    b[strlen(a)]=0;
    printf("%s",b);
    return 0;
}
```
直接按照逻辑即可得到flag，非常可惜因为早上服务器问题没能拿下一血