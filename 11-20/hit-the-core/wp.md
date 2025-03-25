哎我操这题怎么这么坏
core里面藏一个长字符串，长字符串里大写和符号组成了flag
```
string = 'cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}'
flag = ''
for i in range(3, len(string), 5):
    flag += string[i]
 
print(flag)
```