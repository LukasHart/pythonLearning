# 1. Print all integers from 0 - 150

# for i in range(0,151,1):
#     print(i)

# 2. print all multiples of 5 from 5-1,000

# for i in range(5,1001,5):
#     print(i)

# 3. print integers 1 to 100. if divisble by 5, print 'coding' instead if divisble by 10 print coding dojo

# for i in range(1,101):
#     if i / 5: 
#         print('coding')
#     if i/10:
#         print('coding dojo')
#     print(i)

# 4 add odd integers from 0-500,000 and print the final sum 

# sum=0

# for i in range(0,5000001):
#     if i % 2 !=1:
#         sum += i
# print(sum)
    
# 5. print positive numbers starting at 2018 counting down by 4

# for i in range(2018,0,-4):
#     print(i)

# 6. set three variables lowNum, highNum,mult. starting at lowNum and going thru highNum only print integers that are a multiple of mult
lowNum=2
highNum=9
mult=3

for num in range(lowNum,highNum+1):
    if num % mult ==0:
        print(num)

