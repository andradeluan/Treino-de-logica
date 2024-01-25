cod1, quat1, price1 = map(float, input().split())
cod2, quat2, price2 = map(float, input().split())
total = (quat1*price1) + (quat2*price2)
print(f'VALOR A PAGAR: R$ {total:.2f}')