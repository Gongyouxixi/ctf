哎，铸币了，把\"当成两个字符了，实际是转义符号"\"+"的一个字符
```
#include<stdio.h>
#include<string.h>
int main(){
	char v8[]=":\"AL_RT^L*.?+6/46";
	char v7[]="harambe";
	int a=strlen(v8);
	char s[a];
	for(int i=0;i<strlen(v8);i++){
		s[i]=v7[i%7]^v8[i];
		printf("%c",s[i]);
	}
	return 0;
}
```