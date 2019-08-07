print("Я загадал число, угадай.")

original_number = 15

while True:
    number_str = input("Введи число: ")
    number = int(number_str)
    if number == original_number:
        print("Ты угадал")
        break
    elif number < original_number:
        print("Мое число больше")
    elif number > original_number:
        print("Мое число меньше")