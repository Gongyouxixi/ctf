```
#include <stdio.h>
void fun(int a2) {
    switch (a2) {
        case 0:
            printf("i");
            fun(7 * (a2 + 1) % 11);
            break;
        case 1:
            // 修复缺少分号的问题
            printf("e");
            fun(7 * (a2 + 1) % 11);
            break;
        case 3:
            printf("n");
            fun(7 * (a2 + 1) % 11);
            break;
        case 4:
            printf("d");
            fun(7 * (a2 + 1) % 11);
            break;
        case 5:
            printf("a");
            fun(7 * (a2 + 1) % 11);
            break;
        case 6:
            printf("g");
            fun(7 * (a2 + 1) % 11);
            break;
        case 7:
            printf("s");
            fun(7 * (a2 + 1) % 11);
            break;
        case 9:
            printf("r");
            fun(7 * (a2 + 1) % 11);
            break;
        // 添加 default 分支，避免无限递归
        default:
            break;
    }
}//isengard
int main() {
char a[]="isengard";
unsigned char ida_chars[] =
{
   15,   0,   0,   0,  31,   0,   0,   0,   4,   0, 
    0,   0,   9,   0,   0,   0,  28,   0,   0,   0, 
   18,   0,   0,   0,  66,   0,   0,   0,   9,   0, 
    0,   0,  12,   0,   0,   0,  68,   0,   0,   0, 
   13,   0,   0,   0,   7,   0,   0,   0,   9,   0, 
    0,   0,   6,   0,   0,   0,  45,   0,   0,   0, 
   55,   0,   0,   0,  89,   0,   0,   0,  30,   0, 
    0,   0,   0,   0,   0,   0,  89,   0,   0,   0, 
   15,   0,   0,   0,   8,   0,   0,   0,  28,   0, 
    0,   0,  35,   0,   0,   0,  54,   0,   0,   0, 
    7,   0,   0,   0,  85,   0,   0,   0,   2,   0, 
    0,   0,  12,   0,   0,   0,   8,   0,   0,   0, 
   65,   0,   0,   0,  10,   0,   0,   0,  20,   0, 
    0,   0
};
for (int i = 0; i <= 32; ++i )
    putchar(ida_chars[i*4] ^ *(char *)(a + i % 8));
return 0;
}
```
犯了个错误，实际第二个函数中字符存的时候以int存，所以是一字节+3空也就是应该是i*4，我给忘了