need_enter_word = True
# This verible need for comment in case if user add some word(s) without h letter
need_comment = False
while need_enter_word:
    if need_comment:
        print("No 'h' letter here, Try again =) ")
    word = input("Enter some word witch consist h: ")
    if 'h' in word.lower():
        print("Nice job")
        need_enter_word = False
        break
    else:
        need_comment = True



