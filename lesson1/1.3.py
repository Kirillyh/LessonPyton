#Задача 2: Найдите сумму цифр трехзначного числа.

#*Пример:*

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |

n = int(input("Введите трехзначное число: "))

 
d1 = n % 10
print(d1)
n = n // 10
print(n)
d2 = n % 10
print(d2)
n = n // 10

print("Сумма цифр числа:", n + d2 + d1)
