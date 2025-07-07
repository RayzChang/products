products = []

while True:
	name = input('請輸入商品: ')
	if name == 'q':
		break
	price = input('請輸入售價: ')
	price = int(price)
	p = []
	p.append(name)
	p.append(price)
	# 第 7~9 行簡寫方式：p = [name, price]
	products.append(p)

print(products)

for p in products:
	print(p[0], '的價格是', p[1])

# 將商品資料寫入 csv 檔案
# 使用 encoding='utf-8-sig' 可以讓 Excel 正常顯示中文（避免亂碼）
# 若只用 encoding='utf-8'，Excel 可能會讀取錯誤、出現亂碼
with open('products.csv', 'w', encoding='utf-8-sig') as f:
	f.write('商品,價格\n')  # 寫入欄位名稱
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  # 每筆資料一行，逗號分隔
