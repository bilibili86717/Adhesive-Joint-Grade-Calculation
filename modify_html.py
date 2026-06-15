import re

file_path = r'd:\00、AI学习\03、AI写程序\写好的程序\16. 粘接等级划分程序（已上架GitHub）\index.html'

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 找到buildPdfPageHtml函数的起始和结束位置
start_idx = content.find('function buildPdfPageHtml()')
if start_idx == -1:
    print('未找到函数')
    exit(1)

# 找到函数结束位置（匹配大括号）
brace_count = 0
end_idx = start_idx
for i, char in enumerate(content[start_idx:]):
    if char == '{':
        brace_count += 1
    elif char == '}':
        brace_count -= 1
        if brace_count == 0:
            end_idx = start_idx + i + 1
            break

if brace_count != 0:
    print('函数大括号不匹配')
    exit(1)

# 新函数内容
new_function = '''function buildPdfPageHtml() {
  var projectName = document.getElementById('projectName').value || '-';
  var partName = document.getElementById('partName').value || '-';
  var drawingNo = document.getElementById('drawingNo').value || '-';
  var engineer = document.getElementById('engineer').value || '-';
  var calculatedGrade = document.getElementById('calculatedGrade').textContent || '-';
  var finalGrade = document.getElementById('finalGrade').value || '-';
  
  var I12 = document.getElementById('bondingFunction').options[document.getElementById('bondingFunction').selectedIndex].text;
  var I13 = document.getElementById('bondingProtection').options[document.getElementById('bondingProtection').selectedIndex].text;
  var I14 = document.getElementById('bondingLocation').options[document.getElementById('bondingLocation').selectedIndex].text;
  var I16 = document.getElementById('bondingWeight').options[document.getElementById('bondingWeight').selectedIndex].text;
  var I19 = document.getElementById('personnelInjury').value || '-';
  var I20 = document.getElementById('vehicleDamage').options[document.getElementById('vehicleDamage').selectedIndex].text;
  var I21 = document.getElementById('economicLoss').options[document.getElementById('economicLoss').selectedIndex].text;
  
  var html = '<!DOCTYPE html>\\n';
  html += '<html lang="zh-CN">\\n';
  html += '<head>\\n';
  html += '<meta charset="UTF-8">\\n';
  html += '<meta name="viewport" content="width=device-width,initial-scale=1">\\n';
  html += '<title>粘接接头等级划分报告</title>\\n';
  html += '<style>\\n';
  html += 'html{margin:0;padding:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}\\n';
  html += 'body{margin:0;padding:0;font-family:"SimSun","宋体",serif;color:#222;line-height:1.35;font-size:12px;background:#fff;height:297mm;overflow:hidden}\\n';
  html += '.print-page{width:210mm;height:297mm;margin:0;padding:12mm;box-sizing:border-box;overflow:hidden}\\n';
  html += '.title{text-align:center;font-size:17px;font-weight:bold;margin-bottom:6px}\\n';
  html += '.section-title{font-size:12px;font-weight:bold;color:#1e3a8a;margin-top:8px;margin-bottom:4px;border-bottom:2px solid #3b82f6;padding-bottom:2px}\\n';
  html += '.info-row{display:grid;grid-template-columns:110px 1fr;padding:2px 0;border-bottom:1px dashed #ddd;font-size:12px}\\n';
  html += '.info-label{font-weight:500;color:#475569}\\n';
  html += 'table{width:100%;border-collapse:collapse;font-size:11px;margin-top:3px}\\n';
  html += 'th,td{border:1px solid #ddd;padding:3px 5px;text-align:left}\\n';
  html += 'th{background:#dbeafe;font-weight:bold;color:#1e3a8a;font-size:11px}\\n';
  html += '.result-box{background:#ecfdf5;border-left:4px solid #10b981;padding:8px;margin-top:8px;border-radius:4px}\\n';
  html += '.result-label{font-size:12px;color:#374151}\\n';
  html += '.result-value{font-size:17px;font-weight:bold;color:#166534;margin:2px 0}\\n';
  html += '.signature{margin-top:10px;text-align:center;font-size:11px}\\n';
  html += '@media print{\\n';
  html += '  @page{size:A4!important;margin:0!important;padding:0!important}\\n';
  html += '  html,body{margin:0!important;padding:0!important;width:210mm!important;height:297mm!important;overflow:hidden!important}\\n';
  html += '  .print-page{width:210mm!important;height:297mm!important;margin:0!important;padding:12mm!important}\\n';
  html += '}\\n';
  html += '@page{size:A4 portrait;margin:0;padding:0}\\n';
  html += '</style>\\n';
  html += '</head>\\n';
  html += '<body>\\n';
  html += '<div class="print-page">\\n';
  html += '<div class="title">粘接接头等级划分报告</div>\\n';
  html += '<div class="section-title">一、基本信息</div>\\n';
  html += '<div class="info-row"><span class="info-label">项目名称：</span><span>' + projectName + '</span></div>\\n';
  html += '<div class="info-row"><span class="info-label">部件名称：</span><span>' + partName + '</span></div>\\n';
  html += '<div class="info-row"><span class="info-label">图纸号：</span><span>' + drawingNo + '</span></div>\\n';
  html += '<div class="info-row"><span class="info-label">粘接工程师：</span><span>' + engineer + '</span></div>\\n';
  html += '<div class="section-title">二、评价指标</div>\\n';
  html += '<table>\\n';
  html += '<tr><th>编号</th><th>评价项目</th><th>评价结果</th></tr>\\n';
  html += '<tr><td>1</td><td>粘接功能评价</td><td>' + I12 + '</td></tr>\\n';
  html += '<tr><td>2</td><td>粘接防护评价</td><td>' + I13 + '</td></tr>\\n';
  html += '<tr><td>3</td><td>粘接位置评价</td><td>' + I14 + '</td></tr>\\n';
  html += '<tr><td>4</td><td>粘接件重量评价</td><td>' + I16 + '</td></tr>\\n';
  html += '<tr><td>5</td><td>人员伤害评价</td><td>等级' + I19 + '</td></tr>\\n';
  html += '<tr><td>6</td><td>车辆运行损害评价</td><td>' + I20 + '</td></tr>\\n';
  html += '<tr><td>7</td><td>经济损失评价</td><td>' + I21 + '</td></tr>\\n';
  html += '</table>\\n';
  html += '<div class="section-title">三、评定结果</div>\\n';
  html += '<div class="result-box">\\n';
  html += '<div class="result-label">计算得出的级别：</div>\\n';
  html += '<div class="result-value">' + calculatedGrade + '</div>\\n';
  html += '<div class="result-label">最终评定等级：</div>\\n';
  html += '<div class="result-value">' + finalGrade + '</div>\\n';
  html += '</div>\\n';
  html += '<div class="signature">\\n';
  html += '<div>编制人：________ 审核人：________ 批准人：________</div>\\n';
  html += '</div>\\n';
  html += '</div>\\n';
  html += '</body>\\n';
  html += '</html>';
  
  return html;
}'''

# 替换函数
result = content[:start_idx] + new_function + content[end_idx:]

# 写入文件
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(result)

print('修复成功')
