```
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad  # 导入 unpad 函数
import base64
key = b'1234567890abcdef'
iv = b'1234567890abcdef'
expected_encrypted_data = 'MTIzNDU2Nzg5MGFiY2RlZpOn0SHxbVMvaa7jQztMCBtCCiuX+ZRBzSfcL01St5Bmi8BjGeuXliictrjqzSpCGw=='
encrypted_data = base64.b64decode(expected_encrypted_data)
ciphertext = encrypted_data[16:]  # 去掉 IV 部分
cipher = AES.new(key, AES.MODE_CBC, iv)
padded_plaintext = cipher.decrypt(ciphertext)
try:
    # 去除填充
    plaintext = unpad(padded_plaintext, AES.block_size)
    print("解密成功！Flag 是:", plaintext.decode('utf-8'))
except ValueError:
    print("解密失败，可能是填充不正确")
```