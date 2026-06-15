# -*- coding: utf-8 -*-
import io

file_path = r'd:\00、AI学习\03、AI写程序\写好的程序\16. 粘接等级划分程序（已上架GitHub）\index.html'

with io.open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 修改1 - 删除footer
old_footer = '<div class="footer">\n  本计算结果仅供参考\n</div>'
content = content.replace(old_footer, '')

# 修改2 - Word report 中删除 note 行和 .note CSS
old_word_note_css = '.note{font-size:11px;color:#666;margin-top:16px;padding-top:12px;border-top:1px solid #ccc}\n'
content = content.replace(old_word_note_css, '')

old_word_note_div = '<div class="note">本计算结果仅供参考。</div>\n'
content = content.replace(old_word_note_div, '')

# 修改3a - 替换PDF打印CSS部分
old_pdf_style_lines = [
    'html,body,div,p,h1,h2,table{margin:0;padding:0;box-sizing:border-box}',
    'body{font-family:"SimSun","宋体",serif;color:#222;line-height:1.4;font-size:12px;background:#fff}',
    '.toolbar{position:sticky;top:0;display:flex;gap:12px;padding:12px 16px;background:#3b82f6;color:#fff;box-shadow:0 2px 4px rgba(0,0,0,.1);z-index:100}',
    '.toolbar button{border:none;padding:8px 16px;border-radius:6px;font-size:14px;font-weight:bold;cursor:pointer}',
    '.toolbar button.back{background:#1e3a8a;color:#fff}',
    '.toolbar button.back:hover{opacity:.9}',
    '.toolbar button.primary{background:#10b981;color:#fff}',
    '.toolbar button.primary:hover{background:#059669}',
    '.print-page{width:210mm;min-height:297mm;margin:0 auto;padding:15mm;box-sizing:border-box;position:relative;overflow:hidden}',
    '.title{text-align:center;font-size:18px;font-weight:bold;margin-bottom:8px}',
    '.meta{text-align:center;font-size:11px;color:#555;margin-bottom:12px}',
    '.section-title{font-size:13px;font-weight:bold;color:#1e3a8a;margin-top:12px;margin-bottom:6px;border-bottom:2px solid #3b82f6;padding-bottom:3px}',
    '.info-row{display:grid;grid-template-columns:140px 1fr;padding:4px 0;border-bottom:1px dashed #ddd}',
    '.info-label{font-weight:500;color:#475569}',
    'table{width:100%;border-collapse:collapse;font-size:11px;margin-top:6px}',
    'th,td{border:1px solid #ddd;padding:5px;text-align:left}',
    'th{background:#dbeafe;font-weight:bold;color:#1e3a8a;font-size:11px}',
    '.result-box{background:#ecfdf5;border-left:4px solid #10b981;padding:10px;margin-top:12px;border-radius:4px}',
    '.result-label{font-size:12px;color:#374151}',
    '.result-value{font-size:18px;font-weight:bold;color:#166534;margin:4px 0}',
    '.signature{margin-top:16px;text-align:center;font-size:11px}',
    '.note{font-size:10px;color:#666;margin-top:12px;padding-top:10px;border-top:1px solid #ccc}',
    '@media print{',
    '  body{background:#fff;margin:0;padding:0}',
    '  .toolbar{display:none!important}',
    '  .print-page{width:210mm;height:297mm;margin:0;padding:15mm;box-sizing:border-box;overflow:hidden}',
    '}',
    '@page{',
    '  size:A4;',
    '  margin:0;',
    '  @top-left{content:""}',
    '  @top-center{content:""}',
    '  @top-right{content:""}',
    '  @bottom-left{content:""}',
    '  @bottom-center{content:""}',
    '  @bottom-right{content:""}',
    '}'
]
old_pdf_style = '\n'.join(old_pdf_style_lines)

new_pdf_style_lines = [
    'html{margin:0;padding:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}',
    'body{margin:0;padding:0;font-family:"SimSun","宋体",serif;color:#222;line-height:1.35;font-size:12px;background:#fff}',
    'div,table,tr,td,th{box-sizing:border-box}',
    '.toolbar{position:sticky;top:0;display:flex;gap:12px;padding:12px 16px;background:#3b82f6;color:#fff;box-shadow:0 2px 4px rgba(0,0,0,.1);z-index:100}',
    '.toolbar button{border:none;padding:8px 16px;border-radius:6px;font-size:14px;font-weight:bold;cursor:pointer}',
    '.toolbar button.back{background:#1e3a8a;color:#fff}',
    '.toolbar button.back:hover{opacity:.9}',
    '.toolbar button.primary{background:#10b981;color:#fff}',
    '.toolbar button.primary:hover{background:#059669}',
    '.print-page{width:210mm;max-width:210mm;height:297mm;max-height:297mm;margin:0;padding:12mm;box-sizing:border-box;overflow:hidden}',
    '.title{text-align:center;font-size:17px;font-weight:bold;margin-bottom:6px}',
    '.section-title{font-size:12px;font-weight:bold;color:#1e3a8a;margin-top:8px;margin-bottom:4px;border-bottom:2px solid #3b82f6;padding-bottom:2px}',
    '.info-row{display:grid;grid-template-columns:110px 1fr;padding:2px 0;border-bottom:1px dashed #ddd;font-size:12px}',
    '.info-label{font-weight:500;color:#475569}',
    'table{width:100%;border-collapse:collapse;font-size:11px;margin-top:3px}',
    'th,td{border:1px solid #ddd;padding:3px 5px;text-align:left}',
    'th{background:#dbeafe;font-weight:bold;color:#1e3a8a;font-size:11px}',
    '.result-box{background:#ecfdf5;border-left:4px solid #10b981;padding:8px;margin-top:8px;border-radius:4px}',
    '.result-label{font-size:12px;color:#374151}',
    '.result-value{font-size:17px;font-weight:bold;color:#166534;margin:2px 0}',
    '.signature{margin-top:10px;text-align:center;font-size:11px}',
    '@media print{',
    '  html,body{margin:0;padding:0;width:210mm;height:297mm;overflow:hidden;background:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}',
    '  body{page-break-after:avoid!important;break-after:avoid!important}',
    '  .toolbar{display:none!important}',
    '  .print-page{width:210mm;height:297mm;margin:0;padding:12mm;box-sizing:border-box;overflow:hidden;page-break-after:avoid}',
    '  .print-page:last-child{page-break-after:auto}',
    '}',
    '@page{',
    '  size:A4 portrait;',
    '  margin:0;',
    '  margin-top:0;',
    '  margin-bottom:0;',
    '  margin-left:0;',
    '  margin-right:0;',
    '  padding:0;',
    '  marks:none;',
    '  bleed:0;',
    '  trimbleed:0;',
    '  cropmarks:none;',
    '  @top-left{content:"";}',
    '  @top-left-corner{content:"";}',
    '  @top-center{content:"";}',
    '  @top-right{content:"";}',
    '  @top-right-corner{content:"";}',
    '  @bottom-left{content:"";}',
    '  @bottom-left-corner{content:"";}',
    '  @bottom-center{content:"";}',
    '  @bottom-right{content:"";}',
    '  @bottom-right-corner{content:"";}',
    '}',
    '@page:first{size:A4 portrait;margin:0;padding:0}',
    '@page:left{margin:0}',
    '@page:right{margin:0}'
]
new_pdf_style = '\n'.join(new_pdf_style_lines)

content = content.replace(old_pdf_style, new_pdf_style)

# 3b) 删除PDF报告中的日期行
old_pdf_meta = '  <div class="meta">报告日期：${dateStr}</div>\n'
content = content.replace(old_pdf_meta, '')

# 3c) 删除PDF报告中的note行
old_pdf_note = '  <div class="note">本计算结果仅供参考。</div>\n'
content = content.replace(old_pdf_note, '')

with io.open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('修改成功')
