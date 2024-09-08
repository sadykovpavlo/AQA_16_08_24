entering_list = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']


def list_numbers_calculation(list_with_values: list):
    result = []
    for values in list_with_values:
        separate_list = values.split(',')
        # Try to make int from string, if exception occurred we will go to exception block
        try:
            value = [int(i) for i in separate_list]
        except ValueError as ve:
            result.append(f"I can't do it, {ve}")
        else:
            result.append(sum(value))
    print(result)


list_numbers_calculation(entering_list)
