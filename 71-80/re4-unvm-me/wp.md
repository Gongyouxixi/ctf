```
import hashlib
md5s = [
    0x831DAA3C843BA8B087C895F0ED305CE7,#ALEXC
    0x6722F7A07246C6AF20662B855846C2C8,
    0x5F04850FEC81A27AB5FC98BEFA4EB40C,
    0xECF8DCAC7503E63A6A3667C5FB94F610,
    0xC0FD15AE2C3931BC1E140523AE934722,
    0x569F606FD6DA5D612F10CFB95C0BDE6D,
    0x68CB5A1CF54C078BF0E7E89584C1A4E,
    0xC11E2CD82D1F9FBD7E4D6EE9581FF3BD,
    0x1DF4C637D625313720F45706A48FF20F,
    0x3122EF3A001AAECDB8DD9D843C029E06,
    0xADB778A0F729293E7E0B19B96A4C5A61,
    0x938C747C6A051B3E163EB802A325148E,
    0x38543C5E820DD9403B57BEFF6020596D
]
print('Can you turn me back to python ? ...')
flag = input('well as you wish.. what is the flag: ')
if len(flag) > 69:
    print('nice try')
    exit()
if len(flag) % 5 != 0:
    print('nice try')
    exit()
for i in range(0, len(flag), 5):
    s = flag[i:i + 5]
    if int('0x' + hashlib.md5(s.encode()).hexdigest(), 16) != md5s[i // 5]:
        print('nice try')
        exit()

print('Congratz now you have the flag')
```
哈哈，免费md5网站没有一个解出来的，直接抄了