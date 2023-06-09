# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def funk_num(a):
    set_num = set()
    i = 1
    while i <= a:
        k = int(input('Введите элемент множества: '))
        set_num.add(k)
        i += 1
    return set_num

n = int(input('Введите кол-во элементов первого множества: '))
set_1 = funk_num(n)
print(set_1)

m = int(input('Введите кол-во элементов второго множества: '))
set_2 = funk_num(m)
print(set_2)

set_3 = sorted(set_1.intersection(set_2))
print(*set_3)   

if set_3 == list():
    print('Совпадений не найдено')