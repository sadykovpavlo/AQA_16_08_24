# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# Create tuple with my data
my_data = ('Pavlo', 'Sadykov', 29, 'QA', 'Malibu')
# Insert my_data to list people_records at 1st position
people_records.insert(0, my_data)

people_records[1], people_records[5] = people_records[5], people_records[1]

print(people_records)

# check age and print condition
if people_records[6][2] and people_records[10][2] and people_records[13][2] >= 30:
    print(True)
else:
    print(False)

# code for memory
# Function to check age
# def people_age_checker(data: list, num1=None, num2=None, num3=None):
#     # Create lists to keep data with people
#     more_than_thirty = []
#     less_than_thirty = []
#     people_final_list = []
#     # check if num1 True
#     if num1:
#         # Try to catch exceptions like incorrect index or type
#         try:
#             if data[num1][2] >= 30:
#                 more_than_thirty.append(data[num1])
#             else:
#                 less_than_thirty.append(data[num1])
#         except ImportError:
#             print(f"Incorrect Index with index {num1}")
#         except TypeError:
#             print(f"Incorrect Type with index {num1}")
#     else:
#         return "Empty index given"
#     if num2:
#         try:
#             if data[num2][2] >= 30:
#                 more_than_thirty.append(data[num2])
#             else:
#                 less_than_thirty.append(data[num2])
#         except ImportError:
#             print(f"Incorrect Index with index {num2}")
#         except TypeError:
#             print(f"Incorrect Type element with index {num2}")
#     else:
#         pass
#     if num3:
#         try:
#             if data[num3][2] >= 30:
#                 more_than_thirty.append(data[num3])
#             else:
#                 less_than_thirty.append(data[num3])
#         except ImportError:
#             print(f"Incorrect Index with index {num3}")
#         except TypeError:
#             print(f"Incorrect Type element with index {num3}")
#     else:
#         pass
#     # if more_than_thirty have some data append that data to final list if not go to next step
#     if more_than_thirty:
#         for people in more_than_thirty:
#             people_final_list.append(f"Have 30 or more:  {people[0]} {people[1]}")
#     if less_than_thirty:
#         for people in less_than_thirty:
#             people_final_list.append(f"Have less than 30 :  {people[0]} {people[1]}")
#
#     return people_final_list
#
#
# # Prepared tuple task 3
# people_indexes = (2, 2, 10)
#
# # Call people_age_checker to get list with people
# checked_people = people_age_checker(people_records, *people_indexes)
# # Print sentences
# for sentence in checked_people:
#     print(sentence)



