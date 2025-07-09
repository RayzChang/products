# 匯入 os 模組，用來檢查檔案是否存在
import os

def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            if '日期,商品,價格' in line:
                continue  # 跳過標題欄
            time, name, price = line.strip().split(',')
            products.append([time, name, price])
    return products

# 使用者輸入新資料
def user_input(products):
    date = input('請輸入日期: ')
    print('結束程式請輸入"q", 修改日期請輸入"d".')

    while True:
        name = input('請輸入商品: ')
        if name == 'q':
            break
        elif name == 'd':
            date = input('請重新輸入日期: ')
            continue
        price = input('請輸入售價: ')
        price = int(price)
        products.append([date, name, price])  # 快寫法直接新增

    print(products)
    return products

# 印出所有商品紀錄
def print_products(products):
    for p in products:
        print('消費時間是', p[0], p[1], '的價格是', p[2])

# 將所有商品資料寫入 CSV 檔案（包含舊的 + 新的）
# 使用 utf-8-sig 避免 Excel 開啟中文亂碼
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        f.write('日期,商品,價格\n')  # 寫入標題列
        for p in products:
            f.write(str(p[0]) + ',' + p[1] + ',' + str(p[2]) + '\n')  # 每筆商品一行

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('資料檔案存在，開始讀取')
        products = read_file(filename)
    else:
        print('找不到資料檔案，將建立新的清單')
        products = [] #初始化清單，先前的寫法定義在全局之外。

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()