# 5. Реализуйте алгоритм перемешивания списка.
import random

my_list = []
n = 10
for i in range(n):
    my_list.append(i)
print(my_list)

# перемешивание встроенным методом random.shuffle
# random.shuffle(my_list)
# print(my_list)

# перемешивание "вручную"
list_len = len(my_list)
for i in range(list_len):
    j = random.randint(0, list_len-1)
    tmp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = tmp
print(my_list)


# import datetime
# def random_int(num):
#     rand = datetime.datetime.now().microsecond/10**6
#     return int(num*rand)

# a = [1,2,3,4,5,6]
# print(a)
# random_int(5)
# for i in range(len(a)-1,-1,-1):
#     j = random_int(i+1)
#     a[i],a[j] = a[j],a[i]
# print(a)
