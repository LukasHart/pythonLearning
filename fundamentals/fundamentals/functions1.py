# 1 - returns 5
# def number_of_food_groups():
#     return 5

# print(number_of_food_groups())


# 2 - returns error because first function is not defined.
# def number_of_military_branches():
#     return 5


# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


# 3 - prints 5 once that first return hits the function exits and 10 is irrelevant. 
# def number_of_books_on_hold():
#     return 5
#     return 10


# print(number_of_books_on_hold())


# 4 prints 5 once the return of 5 hits the following print is irrelevant 
# def number_of_fingers():
#     return 5
#     print(10)


# print(number_of_fingers())


# 5 - will print 5 and then none or error in the function call we print 5 not return it so it has no value then when we call it itll return none or error because number_of_great_lakes has no value. 
# def number_of_great_lakes():
#     print(5)


# x = number_of_great_lakes()
# print(x)


# 6 - ask about this one. Not understood. 
# def add(b, c):
#     print(b+c)


# print(add(1, 2) + add(2, 3))


# 7 concatenates 2 and 5 together making it 25 important to note that no mathematics are hapening and rather string concatenation. 
# def concatenate(b, c):
#     return str(b)+str(c)


# print(concatenate(2, 5))


# 8 - first prints 100 then runs the conditonals where the return ends up being 10 and returns 10. then we print the func and get 10 printed in the terminal. 
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7


# print(number_of_oceans_or_fingers_or_continents())


# 9 prints 7 then prints 14 then prints 21
# def number_of_days_in_a_week_silicon_or_triangle_sides(b, c):
#     if b < c:
#         return 7
#     else:
#         return 14
#     return 3


# print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3) + number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))


# # 10 prints 8
# def addition(b, c):
#     return b+c
#     return 10


# print(addition(3, 5))


# 11 print 500 then 500 again because the function wasn't called yet then 300 because the function is called then 500 
# b = 500
# print(b)


# def foobar():
#     b = 300
#     print(b)


# print(b)
# foobar()
# print(b)


# # 12 prints 500 - prints 500 again - then 300 - then 500 
# b = 500
# print(b)


# def foobar():
#     b = 300
#     print(b)
#     return b


# print(b)
# foobar()
# print(b)

# 13 - prints 500 - prints 500 -prints 300 then 300
# b = 500
# print(b)


# def foobar():
#     b = 300
#     print(b)
#     return b


# print(b)
# b = foobar()
# print(b)


# 14 prints 1 then 3 then 2
# def foo():
#     print(1)
#     bar()
#     print(2)


# def bar():
#     print(3)


# foo()


# # 15  prints 1 prints 3 returns 5 returns 10 
# def foo():
#     print(1)
#     x = bar()
#     print(x)
#     return 10


# def bar():
#     print(3)
#     return 5


# y = foo()
# print(y)
