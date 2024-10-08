alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n' \
                      '"That depends a good deal on where you want to get to," said the Cat.\n' \
                      '"I don\'t much care where ——" said Alice.\n"' \
                      'Then it doesn\'t matter which way you go," said the Cat.\n"' \
                      '—— so long as I get somewhere," Alice added as an explanation.\n' \
                      '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_square = 436402
azov_sea_square = 37800
total_square = black_sea_square + azov_sea_square
answer_text = f"\nПлоща Чорного моря: {black_sea_square} км2,\n" \
              f"Площа Азовського моря: {azov_sea_square} км2\n" \
              f"Загальна площа обох морів: {total_square} км2\n"
print(answer_text)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total = 375291
first_and_second = 250449
second_and_third = 222950

# Позначемо кількісить товарів через х y z
# Знайдемо товари на 3-му складі через z

z = total - first_and_second

# знайдемо товари на другому складі через y

y = second_and_third - z

# Знайдемо товари на першому складі через x

x = first_and_second - y

text_answer = f"На першому скаладі {x} кількість товарів.\n" \
              f"На другому складі {y} кількість товарів.\n" \
              f"На третьому {z} кількість товарів.\n"
print(text_answer)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
# Будемо вважати що перший платіж 1179 був саме в першому місяці із 18

computer_price = 1179 * 18
print(f"Повна вартість становить {computer_price} грн\n")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

text_answer = f"8019 : 8 залишок = {a}\n9907 : 9 залишок = {b}\n2789 : 5 залишок = {c}\n7248 : 6 залишок = {d}\n" \
              f"7128 : 5 залишок = {e}\n19224 : 9 залишок = {f}\n"
print(text_answer)

# task 08
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
# Щоб не плодити змінні пійдемо шляхом обчислити одразу кінцеву ціну на товари

all_big_pizza_price = 274 * 4
all_medium_pizza_price = 218 * 2
all_juice_price = 35 * 4
cake_price = 350
all_water_price = 21 * 3

total_price = all_big_pizza_price + all_medium_pizza_price + all_juice_price + cake_price + all_water_price

print(f"Іринка має заплатити {total_price} грн\n")
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
max_photo_on_page = 8
needed_pages = all_photos / max_photo_on_page
print(f"Ігорю потрібно {int(needed_pages)} сторінок\n")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
# Знайдемо скільки літрів бензину знадобиться для такої подорожі
dist = 1600
fuel_consumption = 9
tank_capacity = 48
fuel_needed = (dist / 100) * fuel_consumption
print(f"Для поїздки знадобиться  {fuel_needed} літрів бензину.")

# Знайдемо скільки щонайменше разів родині необхідно заїхати на заправку
ref_needed = fuel_needed / tank_capacity
ref_needed = int(ref_needed)
print(f"Потрібно заправитись  {ref_needed} разів.")
