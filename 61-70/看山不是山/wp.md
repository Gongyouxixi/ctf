```
def encrypt(data):
    result = []
    key = 439041101
    for i in range(len(data)):
        byte = data[i]
        byte = (byte ^ key >> (i % 4) * 8) & 255
        byte = byte + i & 255
        result.append(byte)
    return bytes(result)
def check(data):
    target = bytes.fromhex('738495a6b7c8d9e0f123456789abcdef')
    if len(data) != 16:
        return False
    encrypted = encrypt(data)
    return encrypted == target
```
上部分为python代码，下部分为逆向代码
```
def qbcd_main(qbcd_encrypted_data):
    qbcd_key = 439041101
    qbcd_key_bytes = [(qbcd_key >> (shift * 8)) & 0xff for shift in range(4)]
    return bytes((((byte - i) % 256) ^ qbcd_key_bytes[i % 4]) for i, byte in enumerate(qbcd_encrypted_data))
qbcd_target = bytes.fromhex('738495a6b7c8d9e0f123456789abcdef')
qbcd_original_data = qbcd_main(qbcd_target)
print("Original data (hex):", qbcd_original_data.hex())
print("Original data (bytes):", qbcd_original_data)
```