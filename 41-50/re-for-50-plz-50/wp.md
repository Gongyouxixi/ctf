唯一难点是main里的argv参数相当于输入
```
#include <stdio.h>
int main(){
    char a[]="cbtcqLUBChERV[[Nh@_X^D]X_YPV[CJ";
    for(int i=0;i<32;i++){
        printf("%c",a[i]^0x37);
    }
    return 0;
}
```
