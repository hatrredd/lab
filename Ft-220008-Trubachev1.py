a, b = map(int, input("Введите 2 числа: ").split())
print("Сумма чисел: ", a+b,"\nРазность чисел: ", a-b, "\nПроизведение чисел: ", a*b, "\nСреднее арифметическое чисел: ", (a+b)/2)
if a < 0:
    absa = -a
else: absa = a
if b < 0:
    absb = -b
else: absb = b
if absa > absb:
    maxx = absa
    minn = absb
else: maxx = absb; minn = absa
print("Разность максимального и минимального по модулю: ", maxx - minn)