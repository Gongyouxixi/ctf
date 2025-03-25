化简代码
```
#include <stdio.h>
#include <string.h>
int main() {
    int first=0xcafe;
    int second=25;
    char a[]="h4cky0u";
    unsigned int hash = first * 31337 + (second % 17) * 11 + strlen(a) - 1615810207;
    printf("Get your key: ");
    printf("%x\n", hash);
    return 0;
}
```