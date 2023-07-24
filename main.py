# Здача: 10
# N = int(input("Введите количество моент на столе"))

# orel = reshka = 0

# for _ in range (N):
#     x = int (input("Орёл(1) или решка(0)?"))
#     if x == 1:
#         orel += 1
#     else: 
#         reshka +=1

# if orel < reshka:
#     print(f"Переверните {orel} монет что бы все стали решками")
# elif orel == reshka:
#     print(f"Монет орлов {orel} равен количеству решак {reshka}")
# else:
#     print(f"Переверните {reshka} монет что бы все стали орлами")



# Задача 12
# X = (int(input('Введите первое натуральное число от 0 до 1000 ')))
# Y = (int(input('Введите второе натуральное число от 0 до 1000 ')))

# S = X + Y
# P = X * Y

# y1 = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
# x1 = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)

# print (y1)
# print (x1)



# Задача 14
N = int(input("Введите целое число N"))
stop = 0
D = 2
for i in range (N):
    if stop != 1:
        D = D ** i
        if D <= N:
            print(D, end=" ")
            D = 2
        else:
            stop = 1
    else: i = N