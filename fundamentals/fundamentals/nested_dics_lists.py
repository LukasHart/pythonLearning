# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]

# x[1][0] = 15

# students[0]['last_name'] = 'Bryant'

# sports_directory['soccer'][0] = 'Andres'

# z[0]['y'] = 30

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


# def iterateDict(students):
#     for student in students:
#         print(student)

# iterateDict(students)

# little stuck here with being able to pass in a key name and have it print that. 
# def iterateDict2(key_name,students):
#     for key_name in students:
#         print(key_name['first_name'])
#         print(key_name['last_name'])

# iterateDict2('last_name',students)
# iterateDict2('first_name',students)
def iterateDict2(key_name, students):
    for student in range(0, len(students)):
        for key,val in students[student].items():
            if key == key_name:
                print(val)

iterateDict2('first_name',students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# also stuck here with being able to print the len like in the example 
# def printInfo(some_list):
#     for key in some_list.keys():
#         for val in some_list.get(key):
#             print(f'{val} {key}')
            
# printInfo(dojo)


# def printInfo(some_list):
#     for key,val in some_list.items():
#         print(f'{len(val)} {key.upper()}')
#         for i in range(0,len(val)):
#             print(val[i])
            
# printInfo(dojo)