# Задача 34

# def ritn(str):
#     str = str.split()
#     list_1 = []
#     for word in str:
#         sum_w = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 sum_w +=1
#         list_1.append(sum_w)
#     return len(list_1) == list_1.count(list_1[0])

# # пара-ра-рам рам-пам-папам па-ра-па-дам
# int = input("Введите текст")
# if ritn(int):
#    print('Парам пам-пам')
# else:
#     print('Пам парам')



# Задача 36
def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i,j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])

print_operation_table(lambda x,y: x * y)