```
# include <stdio.h>
# include <string.h>
int main(){
    char a[]="KanXueCTF2019JustForhappy";
    char b[]="abcdefghiABCDEFGHIJKLMNjklmn0123456789opqrstuvwxyzOPQRSTUVWXYZ";
    char c[26];
    for(int i=0;i<strlen(a);i++){
        for(int j=0;j<strlen(b);j++){
            if(a[i]==b[j]){
                c[i]=j;
            }
        }
    }
    for(int i=0;i<strlen(a);i++){
        if(c[i]<=61&&c[i]>=36){
            printf("%c",c[i]+29);
        }
        else if(c[i]<=35&&c[i]>=10){
            printf("%c",c[i]+87);
        }
        else{
            printf("%c",c[i]+48);
        }
    }
    return 0;
}
```
