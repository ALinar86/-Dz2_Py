# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой. Нельзя юзать find или count.

string1 = input('Введите полную фразу ')
string2 = input('Введите ортезок фразы ')
N = 0
for i in string1:
    for j in string2:
        if i==j:
            N +=1

print(f'Количество вхождений равно {N}')