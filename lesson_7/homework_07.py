# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number: int):
    # Initialize the appropriate variable
    multiplier = 1
    while_activity_ = True
    while while_activity_:
        result = number * multiplier
        if result > 25:
            while_activity_ = False
        else:
            print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def simple_counter(a: int, b: int) -> int:
    count = a + b
    return count


print(simple_counter(1, 1))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def list_num_arithmetic_mean(list_numbers: list) -> float:
    arithmetic_mean = sum(list_numbers) / len(list_numbers)
    return arithmetic_mean


list_of_numbers = [i for i in range(1, 100)]
print(list_num_arithmetic_mean(list_of_numbers))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def revers_string(text: str):
    reversed_text_list = reversed(text)
    reversed_text = ''.join(reversed_text_list)
    print(reversed_text)


# some test
revers_string('latipac morf olleH')


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(words_list: list):
    dict_len_of_words = {len(k): k for k in words_list}
    sorted_list = sorted(dict_len_of_words, reverse=True)
    print(f"Найдовше слово: {dict_len_of_words[sorted_list[0]]}")


test_text = 'Написати функцію, яка приймає список слів та повертає найдовше слово у списку.'

longest_word(test_text.split())


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    index = str1.find(str2)
    if index:
        return index
    else:
        return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
'''Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
'''


def required_album_pages(all_photos, photos_per_page):
    needed_pages = all_photos / photos_per_page
    return f"Тобі потрібно {needed_pages} сторінок"


print(required_album_pages(22, 1))


# task 8
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""


def cont_sum_of_square(square1, square2):
    return square1 + square2


print(f"Total square: {cont_sum_of_square(436402, 37800)}")


# task 9
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""


def count_total_price(once_payment, month):
    return f"Повна ціна : {once_payment * month}"


print(count_total_price(1179, 18))
# task 10

"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""


def count_product_price(products: list):
    list_prices = [x[1] * x[2] for x in products]
    total_price = sum(list_prices)
    return f"Ціна за продукти:  {total_price}"


some_prod_list = [("Піца велика", 4, 274), ("Піца середня", 2, 218), ("Сік", 4, 35), ("Торт", 1, 350), ("Вода", 3, 21)]


print(count_product_price(some_prod_list))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
