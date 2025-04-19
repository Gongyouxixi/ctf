def custom_base64_decode(encoded: str) -> bytes:
    # 自定义编码表
    custom_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    decode_table = {char: (idx - 24) % 64 for idx, char in enumerate(custom_table)}
    padding = 0
    if len(encoded) % 4 == 0:
        if encoded.endswith(('AA==', 'A===')):
            padding = encoded.count('A', len(encoded)-2)
            encoded = encoded.rstrip('A') + '=' * padding
    decoded = bytearray()
    buffer = 0
    bits_collected = 0
    for char in encoded:
        if char == '=':  
            bits_collected -= 6
            continue
        value = decode_table[char]
        buffer = (buffer << 6) | value
        bits_collected += 6
        if bits_collected >= 24:
            bits_collected -= 24
            chunk = (buffer >> bits_collected) & 0xFFFFFF
            decoded.extend([
                (chunk >> 16) & 0xFF,
                (chunk >> 8) & 0xFF,
                chunk & 0xFF
            ])
            buffer = buffer & ((1 << bits_collected) - 1)
    if bits_collected >= 8:
        bits_collected -= 8
        decoded.append((buffer >> bits_collected) & 0xFF)
    if padding:
        decoded = decoded[:-padding]
    
    return bytes(decoded)
encoded_str = "e2lfbDB2ZV95b3V9"  # 替换为实际编码后的字符串,请手动删除=,本人代码出来写的有问题
decoded_data = custom_base64_decode(encoded_str)
print("Decoded:", decoded_data)