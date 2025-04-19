"""
云隐解密脚本
"""
ciphertext = "8842101220480224404014224202480122"
ciphertext = ciphertext.split('0')  # 以0做分割，分成8块，方便对每块做加法
result = ""
for block in ciphertext:  # 遍历所有块，每块对应一个字母
    sum = 0
    for i in range(len(block)):  # 对每块内容做加法，得到对应的数字
        sum += int(block[i])
    result += chr(65 + sum - 1)  # A的ascii码是65，而sum是1->26，表示A->Z ，所以要减1，变成0->25再加上65，变成ascii：65-90表示A->Z
print(result)