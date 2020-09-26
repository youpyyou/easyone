#задача : нужно сделать магазин в котором высчитывается сумма со скидкой и скидка
price=float(input("input the prise: "))
discount100=3                             #discount for price >100 and <=150
discount150=9                             #discount for price >150 and <=200
discount200=18                            #discount for price >200
totalprice100=price-price*discount100/100 #total price with discount100
totalprice150=price-price*discount150/100 #total price with discount150
totalprice200=price-price*discount200/100 #total price with discount200
if price> 200:
    print('u discount: ', f'{discount200}''%','total summ: ','%5.2f' % totalprice200)
elif price> 150:
    print('u discount: ', f'{discount150}''%', 'total summ: ','%5.2f' % totalprice150)
elif price> 100:
    print('u discount: ', f'{discount100}''%', 'total summ: ', '%5.2f' % totalprice100)
else:
    print('u don\'t have a discount',',total summ: ' '%.2f' % price)

