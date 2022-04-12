# Жубаева Айкен
# Практическое задание 3.
# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn+ nnn.

number = int(input("Введите число "))
sum_1 = number
sum_2 = number + number
sum_3 = number + number + number
print("Сумма чисел равна   {}{}{} ".format(sum_1, sum_2, sum_3))
