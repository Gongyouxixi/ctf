跟随DARK SECRET GALAXY找到函数就行
```
#include <stdio.h>
int main(){
    char off_409004[]="Andromeda";
    char off_409008[]="Messier";
    char off_40900C[]="Sombrero";
    char off_409010[]="Triangulum";
    // 修正数组初始化
    char str[] = {
        off_409004[8],
        off_409010[7],
        off_409008[4],
        off_409004[6],
        off_409004[1],
        off_409008[2],
        '_',
        off_409004[8],
        off_409004[3],
        off_40900C[5],
        95,
        off_409004[8],
        off_409004[3],
        off_409004[4],
        off_409010[6],
        off_409010[4],
        off_409004[2],
        95,
        off_409010[6],
        off_409008[3],
        '\0' // 确保字符串以 '\0' 结尾
    };
    printf("%s\n", str);
    return 0;
}
```
拼字游戏，还算有趣