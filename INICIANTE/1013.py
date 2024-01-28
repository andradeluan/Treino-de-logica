import math
a , b ,c = map(int, input().split(" "))
maior = (a + b + abs(a - b))  / 2
resultado = (maior + c + abs(maior - c))/2
print(f'{resultado:.0f} eh o maior')