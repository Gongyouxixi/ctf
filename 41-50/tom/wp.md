//简单迷宫，不用转化的迷宫
```
#include <stdio.h>
#include <string.h>
int main(){
    char maze[]="S**#########*########**#########**#########*###**##***###**##*#####**##*#####*E##*******#######";
    // 提前计算maze数组的长度
    int len = strlen(maze);
    for(int i=0; i < len; i++){
        if(i % 10 == 0)        
            printf("\n");
        printf("%c", maze[i]);
    }
    return 0;
}
//ddsssdssaasssddddddwd
```
这里人工找迷宫解远比写一个求解算法快，所以这里就不写了。