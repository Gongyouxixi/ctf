```
enc=[
  0x5F, 0xF2, 0x5E, 0x8B, 0x4E, 0x0E, 0xA3, 0xAA, 0xC7, 0x93, 
  0x81, 0x3D, 0x5F, 0x74, 0xA3, 0x09, 0x91, 0x2B, 0x49, 0x28, 
  0x93, 0x67
]
for i in range(22):
    temp=0
    for j in range(i+1):
        temp=temp*1828812941+12345
    print(chr((temp^enc[i])%256),end='')
```
多用python，少用c，c的数据类型太麻烦