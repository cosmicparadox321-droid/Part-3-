# Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2).
upper_limit = int(input("Upper limit: "))
base = int(input("Base: "))
number = 1
while number <= upper_limit:
    print(number)
    number *= base

#what is the difference between the two programs?   
#The main difference between the two programs is that the first program is specifically designed to print powers of 2, while the second program allows the user to input any base for which they want to print powers.