这道题还是有点难度，读代码实际倒是比我想的简单点。
下面我会给出我粗读之后的代码注释
```
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>

#define FLAG_LEN 20

void * checking(void *arg) {
    char *result = malloc(sizeof(char));
    char *argument = (char *)arg;
    *result = (argument[0]+argument[1]) ^ argument[2];
    return result;
}//一个检验函数全代码最重要的，结合后续内容可知，这是用于检测用户输入是否与随机字符+偏移的结果相同的

int highly_optimized_parallel_comparsion(char *user_string)
{
    int initialization_number;
    int i;
    char generated_string[FLAG_LEN + 1];
    generated_string[FLAG_LEN] = '\0';

    while ((initialization_number = random()) >= 64);
    
    int first_letter;
    first_letter = (initialization_number % 26) + 97;
    //随机化第一个字母，从a到z
    pthread_t thread[FLAG_LEN];
    char differences[FLAG_LEN] = {0, 9, -9, -1, 13, -13, -4, -11, -9, -1, -7, 6, -13, 13, 3, 9, -13, -11, 6, -7};
    //偏移量
    char *arguments[20];
    for (i = 0; i < FLAG_LEN; i++) {
        arguments[i] = (char *)malloc(3*sizeof(char));
        arguments[i][0] = first_letter;
        arguments[i][1] = differences[i];
        arguments[i][2] = user_string[i];
        pthread_create((pthread_t*)(thread+i), NULL, checking, arguments[i]);//没看懂但不重要
    }

    void *result;
    int just_a_string[FLAG_LEN] = {115, 116, 114, 97, 110, 103, 101, 95, 115, 116, 114, 105, 110, 103, 95, 105, 116, 95, 105, 115};
    for (i = 0; i < FLAG_LEN; i++) {
        pthread_join(*(thread+i), &result);
        generated_string[i] = *(char *)result + just_a_string[i];//检验值+检验用字符串
        free(result);
        free(arguments[i]);
    }

    int is_ok = 1;
    for (i = 0; i < FLAG_LEN; i++) {
        if (generated_string[i] != just_a_string[i])//判断是否相等，需要检验值=0也就是输入和随机验证一致
            return 0;
    }

    return 1;
}

int main()
{
    char *user_string = (char *)calloc(FLAG_LEN+1, sizeof(char));
    fgets(user_string, FLAG_LEN+1, stdin);
    int is_ok = highly_optimized_parallel_comparsion(user_string);
    if (is_ok)
        printf("You win!\n");
    else
        printf("Wrong!\n");
    return 0;
}
```
于是可以得到一个尝试用的代码
```
#include <stdio.h>
int  main(){
    int first_letter;
    int i;
    int differences[20] = {0, 9, -9, -1, 13, -13, -4, -11, -9, -1, -7, 6, -13, 13, 3, 9, -13, -11, 6, -7};
    for(int i=0;i<26;i++){
        first_letter=i+97;
        printf("first_letter= %d ",first_letter);
        for(int j=0;j<20;j++){
            printf("%c",differences[j]+first_letter);
        }
        printf("\n");
    }
    return 0;
}
```
我反正没明白为什么网上题解老保留那个just_a_string
明明没有用