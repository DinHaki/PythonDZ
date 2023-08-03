# Задача 30 an = a1 + (n-1) * d.

a1 = int(input("Введине число a"))
d = int(input("Введине число d"))
n = int(input("Введине число n"))
m = int(input("Введите размер массива"))
my_array = []

for i in range(m):
    an = a1 + (n-1) * d
    num = an
    my_array.append(an)

print(an)
print(my_array)



# Задача 32

# from random import randint
# mas = [randint(-30,30) for _ in range(5)]
# mas2 = []
# a = int(input("Введине минимум диапазона"))
# d = int(input("Введине максимум диапазона"))

# for getindex in range(len(mas)):
#     if mas[getindex] >= a and mas[getindex] <= d:
#         mas2.append(getindex)

# print(mas)
# print(mas2)

