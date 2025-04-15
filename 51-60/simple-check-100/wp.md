这题的难点在跳过一个奇怪的判断语句
可以用patch的方法，也可以静态分析
作为传统派我直接把代码附赠在下面了//未优化
代码看了半天才明白v2这一句是在4字节异或
```
#include <stdio.h>
int main()
{
  int *result;
  unsigned int v2;
  int *v3;
  int j;
  int i;
  unsigned char flag_data[] =
{
  0xDC, 0x17, 0xBF, 0x5B, 0xD4, 0x0A, 0xD2, 0x1B, 0x7D, 0xDA, 
  0xA7, 0x95, 0xB5, 0x32, 0x10, 0xF6, 0x1C, 0x65, 0x53, 0x53, 
  0x67, 0xBA, 0xEA, 0x6E, 0x78, 0x22, 0x72, 0xD3
};
signed char v4[] = {
    84, -56, 126, -29, 100, -57, 22, -102, -51, 17, 101, 50, 45, -29, -45, 67, -110, -87, -99, -46, -26, 109, 44, -45, -74, -67, -2, 106, 19
};
  for ( i = 0; i <= 6; ++i )
  {
    v2 = *(unsigned long *)(v4 + 4 * i) ^ 0xDEADBEEF;
    //4字节一比较
    result = (int *)&v2;
    v3 = (int *)&v2;
    for ( j = 3; j >= 0; --j )
      result = (int *)putchar((char)(*((char *)v3 + j) ^ flag_data[4 * i + j]));
      //同理
  }
  return 0;
}
```