products = []
while True:
	name = input('請輸入商品: ')
	if name == 'q':
		break
	price = input('請輸入售價: ')
	p = []
	p.append(name)
	p.append(price)
	#7-9行簡寫方式 p = [name, price]
	products.append(p)
print(products)

products[0][0]