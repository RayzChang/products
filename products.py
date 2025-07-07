# 讀取舊的商品資料（避免每次新增時把原本資料蓋掉）
products = []
with open('products.csv', 'r', encoding='utf-8-sig') as f:
	for line in f:
		if '商品,價格' in line:
			continue  # 跳過標題欄
		name, price = line.strip().split(',')  # 快寫法
		products.append([name, price])  # 存成二維清單

print(products)

# 使用者輸入新資料
while True:
	name = input('請輸入商品: ')
	if name == 'q':
		break
	price = input('請輸入售價: ')
	price = int(price)
	products.append([name, price])  # 快寫法直接新增

print(products)

# 印出所有商品紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 將所有商品資料寫入 CSV 檔案（包含舊的 + 新的）
# 使用 utf-8-sig 避免 Excel 開啟中文亂碼
with open('products.csv', 'w', encoding='utf-8-sig') as f:
	f.write('商品,價格\n')  # 寫入標題列
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')  # 每筆商品一行
