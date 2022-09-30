# Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5]
random.shuffle(list)
print(list)
import random
from random import randint
n = 5
lst = []
result = 1
for i in range(n):
    lst.append(randint(n * -1, n))
print(lst)
random.shuffle(lst)
print(lst)
with open('file.txt', 'r') as f:
    for i in f:
        result *= lst[int(i) - 1]
    print(result)