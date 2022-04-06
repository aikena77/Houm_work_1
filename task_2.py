# Жубаева Айкен
# Практическое задание 2.
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч.мм.сс.

time_seconds = int(input("Введите время в секундах? "))
time_hour = time_seconds // 3600
remainder = time_seconds % 3600
time_minute = remainder // 60
sec = remainder % 60
print("Переводим в новый формат  {}:{}:{} ".format(time_hour, time_minute, sec))