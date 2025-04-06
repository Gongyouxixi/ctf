# 简单maze入门
# step：1
分离出迷宫，方便找到路线
这里因为迷宫较为简单就不用写dfs了
# step：2
找到移动方程，如awsd上下左右，这题用的是oO0.四个字符分别替代//顺序不是这个，等下解题代码里有正确对应
# step：3
找到路线，这题的路线是
``` c
#include<stdio.h>
#include<string.h>
int main(){
    unsigned char ida_chars[] =
    {
       32,  32,  42,  42,  42,  42,  42,  42,  42,  32, 
       32,  32,  42,  32,  32,  42,  42,  42,  42,  32, 
       42,  32,  42,  42,  42,  42,  32,  32,  42,  32, 
       42,  42,  42,  32,  32,  42,  35,  32,  32,  42, 
       42,  42,  32,  42,  42,  42,  32,  42,  42,  42, 
       32,  32,  32,  32,  32,  42,  42,  42,  42,  42, 
       42,  42,  42,  42
    };
    for(int i = 0;i<strlen(ida_chars);i++){
        if(i%8==0){
            printf("\n");
        }
        printf("%c",ida_chars[i]);
    }
    char a[]="dsddssasssddddwwaa";
    for(int i=0;i<strlen(a);i++){
        if(a[i]=='d'){
            a[i]='o';
        }
        if(a[i]=='a'){
            a[i]='O';
        }
        if(a[i]=='s'){
            a[i]='0';
        }
        if(a[i]=='w'){
           a[i]='.'; 
        }
    }
    printf("\n%s",a);
    return 0;
}
```
//该解题代码会输出迷宫和正确答案，至于用nctf{包裹答案}这样入门的东西就不多赘述