lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# create some list for str
lst2 = []
for obj in lst1:
    # check type of objects if  str append to lst2
    if type(obj) is str:
        lst2.append(obj)

print(lst2)
