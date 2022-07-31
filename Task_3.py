# Найти сумму чисел списка стоящих на нечетной позиции


list_1 = [1,1,2,3,2,5]
print(sum([y for x,y in enumerate(list_1) if x%2 == 0 ]))