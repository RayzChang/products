# 匯入 os 模組，用來檢查檔案是否存在
import os

products = []

# 檢查是否已經有資料檔案（products.csv）
if os.path.isfile('products.csv'):
	print('資料檔案存在，開始讀取')
	with open('products.csv', 'r', encoding='utf-8-sig') as f:
		for line in f:
			if '商品,價格' in line:
				continue  # 跳過標題欄
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到資料檔案，將建立新的清單')


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
