adventures_of_tom_sawyer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawyer у завданнях 1-3
## Майже не читабельно перезаписувати змінну, додав останню версію тексту в тасці 3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""


"""
In this homework I follow the task 1-3 steps one by one and change text, each change is a continuation
of the previous one. Final version of text You can find in task 3 variable 'text_final_version' 
"""

# replace end of paragraph  to space
replaced_paragraph_text = adventures_of_tom_sawyer.replace("\n", " ")


# task 02 ==
""" Замініть .... на пробіл
"""

replaced_points_text = replaced_paragraph_text.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
striped_text = replaced_points_text.replace("  ", "")


# added some warning in case of extra space remained
if "  " in striped_text:
    print("Extra space remained, please check it!")

text_final_version = striped_text

# Assign  new value to variable according comments to homework
adventures_of_tom_sawyer = text_final_version

print(f"The final version of text:\n{adventures_of_tom_sawyer}\n")

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

count_h_letter = adventures_of_tom_sawyer.count("h")

print(f"The text have {count_h_letter} 'h' letters\n")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

# use for to count capital letters
counted_capital_letter = 0
for char in text_final_version:
    if char.isupper():
        counted_capital_letter += 1

print(f"The text consist {counted_capital_letter} capital letter")

# task 06

""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

print(f"Word 'Tom' position: {adventures_of_tom_sawyer.find('Tom', 2)}")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
# here no print, result is list and I use variable adventures_of_tom_sawyer_sentences in the next task
adventures_of_tom_sawyer_sentences = text_final_version.split('.')
# KOSTYL after separate text by point at the end list has empty element "" I decided to delete it from list by del()
del(adventures_of_tom_sawyer_sentences[-1])

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

the_forth_sentence = adventures_of_tom_sawyer_sentences[3]
print(f"The fourth sentence is :\n{the_forth_sentence.lower()}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

for sentence in adventures_of_tom_sawyer_sentences:
    # Text has space at the beginning  of each sentence, remove space with strip()
    striped_sentence = sentence.strip()
    if striped_sentence.startswith("By the time"):
        print("Some sentence starts with 'By the time'")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
separate_last_sentence = adventures_of_tom_sawyer_sentences[-1].strip().split(' ')
print("Last sentence has", len(separate_last_sentence), "words")
