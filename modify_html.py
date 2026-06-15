import re

# 读取文件
with open(r'd:\00、AI学习\03、AI写程序\写好的程序\16. 粘接等级划分程序（已上架GitHub）\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复重复的@page规则
content = content.replace('@page{size:A4!important;margin:0!important;padding:0!important}\n  @page{size:A4!important;margin:0!important;padding:0!important}', '@page{size:A4!important;margin:0!important;padding:0!important}')

# 保存文件
with open(r'd:\00、AI学习\03、AI写程序\写好的程序\16. 粘接等级划分程序（已上架GitHub）\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('修改成功')
