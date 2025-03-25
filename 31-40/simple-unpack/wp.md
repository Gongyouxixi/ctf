# 唯一问题
elf文件upx打包后在windows下无法解壳
主要原因是不同平台（Windows/Linux）的存根不同，需匹配目标文件格式（PE/ELF）
所以可能导致windows下的解壳工具无法解壳
解决方案，还能怎么办，linux下解壳就行