```
import idc
s = 0x600b00
length = 182
for i in range(length):
    current_ea = s + i
    # 检查地址是否有效
    if not idc.is_loaded(current_ea):
        print(f"警告: 地址 {hex(current_ea)} 不可访问，跳过！")
        continue
    # 读取-解密-写入
    original_byte = idc.get_wide_byte(current_ea)
    idc.patch_byte(current_ea, original_byte ^ 0xC)
print("操作完成，共处理 %d 字节" % length)
```
这题有点意思，直接用ida内置python，提前处理judge数据然后再框选judge数据u+c+p得到一个新的函数
然后就变成简单题了，主要难度在ida的python脚本上