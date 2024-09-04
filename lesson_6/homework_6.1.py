user_input_text = input("Enter your text: ")
input_text_list = {x for x in user_input_text}
if len(input_text_list) > 10:
    print(True)
else:
    print(False)

# I can add while for loop, no  break until len > 10, but it's not about task 6.1
