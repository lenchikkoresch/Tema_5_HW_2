# На столе лежат n монеток. Некоторые из них лежат 
# вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, 
# которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random


n = int(input("Введите количество монет n:  "))
orel = 0
reshka = 0
for i in range(n):
    a = random.randint(0,1)
    print (a)
    if a==1:
        orel=orel+1
    else:
        reshka=reshka+1
print(f"Монет, лежащих вверх решкой: {reshka}, монет, лежащих вверх гербом: {orel}")
if orel > reshka:
    print (f"Переворачиваем монеты, лежащие вверх решкой: {reshka}")
else:
    print (f"Переворачиваем монеты, лежащие вверх гербом: {orel}")   
    