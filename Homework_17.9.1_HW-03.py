import re
import random

def generate_array():
    return [(lambda i: round(random.random()*i, 2))(i) for i in range(-10, 10)]


def init_array():
    while True:
        try:
            sequence_string = input(
                "Введите последовательность чисел через пробел (int, float, positive or negative): (или можно сгенерировать [press Enter])")
            if sequence_string == "":
                return generate_array()
            sequence_array = " ".join(re.split("\s+", sequence_string))
            sequence_array = sorted(list(map(float, sequence_array.split())))

            if len(sequence_array) > len(set(sequence_array)):
                sequence_array = list(set(sequence_array))
                print(
                    "Повторяющиеся значения удалены, ждите обновлений программы для данной фичи:)")
        except ValueError:
            print(
                "Неверный форма ввода:\nпример [0001 0.1 1 2 -3    89.7 -101.2      ] ")
            continue
        else:
            if len(sequence_array) in [0, 1]:
                print(
                    "В нашей программе последовтельность не может быть пустой или состоять из 1-го элемента")
                continue
            else:
                return sequence_array


def init_number():
    while True:
        try:
            number = float(input(
                "Теперь введите любое число. Для проверки входения в диапазон последовательности: "))
        except ValueError:
            print(
                "Неверный форма ввода:\nпример [0001 0.1 1 2 -3    89.7 -101.2      ] ")
            continue
        else:
            print("Ваше число: ", number)
            return number

def binary_search(array, element, left, right):
    if left > right:
        if element < array[0]:
            return f"Число {element} не входит в диапазон. Меньше 0 индекса."
        elif element == array[0]:
            return f"Число {element} не входит в диапазон. Равно 0 индексу последовательности."
        else:
            return f"Число {element} не входит в диапазон. Больше максимального числа в последовательности."

    middle = (right+left) // 2

    if array[middle-1] < element <= array[middle]:
        return f"Число {element} входит в диапазон. Индекс позиции меньшего элемента {middle-1}."

    elif element < array[middle]:
        return binary_search(array, element, left, middle-1)
    else:  # иначе в правой
        return binary_search(array, element, middle+1, right)

array_ = init_array()
print("Ваша последовательность: ", array_)
number = init_number()
print(binary_search(array_ , number, left = 0, right= len(array_)-1))


