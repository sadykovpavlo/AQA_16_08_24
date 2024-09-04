# create some list
some_list = []
# add range() because  did not find list in task 6.4
for i in range(0, 101):
    # find even num and add to list
    if i % 2 == 0:
        some_list.append(i)
# Count sum with sum()
total_sum = sum(some_list)
print(total_sum)

