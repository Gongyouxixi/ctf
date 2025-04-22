def rc4_init(key: bytes):
    sbox = list(range(256))
    # 修复列表推导式的语法错误
    k = [key[i % len(key)] for i in range(256)]

    j = 0
    for i in range(256):
        # 修复括号缺失问题
        j = (j + sbox[i] + k[i]) % 256
        # 修复逗号缺失问题
        sbox[i], sbox[j] = sbox[j], sbox[i]

    return sbox

def rc4_crypt(data: bytes, sbox):
    i = j = 0
    out = bytearray()

    for byte in data:
        i = (i + 1) % 256
        j = (j + sbox[i]) % 256
        # 修复逗号缺失问题
        sbox[i], sbox[j] = sbox[j], sbox[i]
        # 修复括号缺失问题
        k = sbox[(sbox[i] + sbox[j]) % 256]
        out.append(byte ^ k)

    return bytes(out)

key = b"gamelab@"#自己填充
# 修复语句分隔符问题，使用逗号替代分号
cipher_data = (
   0xB6,
   0x42,
   0xB7,
   0xFC,
   0xF0,
   0xA2,
   0x5E,
   0xA9,
   0x3D,
   0x29,
   0x36,
   0x1F,
   0x54,
   0x29,
   0x72,
   0xA8,
   0x63,
   0x32,
   0xF2,
   0x44,
   0x8B,
   0x85,
   0xEC,
   0xD,
   0xAD,
   0x3F,
   0x93,
   0xA3,
   0x92,
   0x74,
   0x81,
   0x65,
   0x69,
   0xEC,
   0xE4,
   0x39,
   0x85,
   0xA9,
   0xCA,
   0xAF,
   0xB2,
   0xC6
)#自己填充

cipher_data = cipher_data # 截断为实际长度
# 初始化 S-box
sbox = rc4_init(key)
# 解密
plaintext = rc4_crypt(cipher_data, sbox)
print(plaintext.decode(errors="replace"))
