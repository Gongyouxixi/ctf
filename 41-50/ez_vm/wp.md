简单题，打开分析代码即可，并无需要注意的
唯一问题是记得打开vm_excute不然会对base64解出来的乱码感到疑惑
```
import base64
encoded = "/P7sAe/U0s7c1vjb0vjfyt=="
decoded_bytes = base64.b64decode(encoded)
print(decoded_bytes)
result=bytes([((byte-3)&0xff)^0xAA for byte in decoded_bytes])
print(result)
```