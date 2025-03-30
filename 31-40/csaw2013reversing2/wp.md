# 方法1
首先啊，作为纯正静态派，我管他hint里面写的什么
抓住反汇编代码顷刻炼化
```
  int v3; // ecx
  CHAR *lpMem; // [esp+8h] [ebp-Ch]
  HANDLE hHeap; // [esp+10h] [ebp-4h]

  hHeap = HeapCreate(0x40000u, 0, 0);
  lpMem = (CHAR *)HeapAlloc(hHeap, 8u, SourceSize + 1);
  memcpy_s(lpMem, SourceSize, &unk_409B10, SourceSize);//因为没有执行401000所以if执行了
  if ( !sub_40102A() && !IsDebuggerPresent() )
  {
    MessageBoxA(0, lpMem + 1, "Flag", 2u);
    HeapFree(hHeap, 0, lpMem);
    HeapDestroy(hHeap);
    ExitProcess(0);
  }
  __debugbreak();
  sub_401000(v3 + 4, (int)lpMem);               // 静态分析的关键函数，v3当做是0即可，ipmem需要向上追溯
  ExitProcess(0xFFFFFFFF);
```
sub_401000
```
  int v2; // esi
  unsigned int v3; // eax
  unsigned int v4; // ecx
  unsigned int result; // eax

  v2 = dword_409B38;
  v3 = a2 + 1 + strlen((const char *)(a2 + 1)) + 1;
  v4 = 0;
  result = ((v3 - (a2 + 2)) >> 2) + 1;           
  // result=strlen((const char *)(a2+1)>>2)+1;
  if ( result )
  {
    do
      *(_DWORD *)(a2 + 4 * v4++) ^= v2;
    while ( v4 < result );
  }
  return result;
```
可以得到解密代码
```
# include<stdio.h>
#include<string.h>
int main(){
    // Bug 修复：添加分号，修正数组初始化
    char a[] = {0xbb, 0xaa, 0xcc, 0xdd}; 
    char b[] =
    {
      0xBB, 0xCC, 0xA0, 0xBC, 0xDC, 0xD1, 0xBE, 0xB8, 0xCD, 0xCF, 
      0xBE, 0xAE, 0xD2, 0xC4, 0xAB, 0x82, 0xD2, 0xD9, 0x93, 0xB3, 
      0xD4, 0xDE, 0x93, 0xA9, 0xD3, 0xCB, 0xB8, 0x82, 0xD3, 0xCB, 
      0xBE, 0xB9, 0x9A, 0xD7, 0xCC, 0xDD
    };
    for(int i=0;i<34;i++){
        b[i]^=a[i%4];
        printf("%02x ",b[i]);
    }
    printf("\n");
    for(int i=0;i<34;i++){
        printf("%c",b[i]);
    }
    return 0;
}
```
# 方法2
和花指令的处理方式是一样的
把不想要的patch掉
具体方法等笔者明天来更新