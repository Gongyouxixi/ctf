其实就是一个简单RC4解密，key为UCSC
密文为v5+v6//不然凑不够36的长度
```
def rc4_init(key: bytes):
    sbox = list(range(256))
    k = [key[i % len(key)] for i in range(256)]

    j = 0
    for i in range(256):
        j = (j + sbox[i] + k[i]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]

    return sbox

def rc4_crypt(data: bytes, sbox):
    i = j = 0
    out = bytearray()

    for byte in data:
        i = (i + 1) % 256
        j = (j + sbox[i]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]
        k = sbox[(sbox[i] + sbox[j]) % 256]
        out.append(byte ^ k)

    return bytes(out)
key = b"UCSC"
# 密文（从汇编里提取的 4 个 64-bit QWORD，以小端存储）
cipher_data = (
    0x089B83EC0E7A3CF8.to_bytes(8,'little') +
    0x3F0EA83858C85F6A.to_bytes(8,'little') +
    0xAB8A1E39811B5F22.to_bytes(8,'little') +
    0x649F307A6475E9B1.to_bytes(8,'little') +
    0xAB7BBD90.to_bytes(4,'little')
)#自己填充

cipher_data = cipher_data[:36] # 截断为实际长度
# 初始化 S-box
sbox = rc4_init(key)
# 解密
plaintext = rc4_crypt(cipher_data, sbox)
print(plaintext.decode(errors="replace"))
```