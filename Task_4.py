# Используйте операции + - * / приоритет операции стандартный. 
# Пример:
# 2 + 2 = 4
# 1 + 2 * 3 = 7
# Добавьте возможность использования скобок, меняющих приоритет операций
# (1 + 3) * 3 = 9 

def calc(s):
    count = ''
    digit = []
    for i in range(len(s)):
        if s[i].isdigit():
            count += s[i]
        else:
            digit.append(int(count))
            digit.append(s[i])
            count = ''
    digit.append(int(count))
    return digit

def decision(my_list):
    while len(my_list) > 1:
        if '*' in my_list or '/' in my_list: 
            i = my_list.index('*')
            res = my_list[i-1] * my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
            i = my_list.index('/')
            res = my_list[i-1] / my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
        if '+' in my_list or '-' in my_list:
            i = my_list.index('+')
            res = my_list[i-1] + my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
            i = my_list.index('-')
            res = my_list[i-1] - my_list[i+1]
            my_list[i-1] = res
            my_list.pop(i+1)
            my_list.pop(i)
        return res
s = '1+4-2*3/2'
print(eval(s))
my_list = calc(s)
print(calc(s))
print(decision(my_list))




