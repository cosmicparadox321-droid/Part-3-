# Please write a program which asks the user to type in an upper limit. 
# The program then prints out numbers so that each subsequent number is the
#  previous one doubled, 
# starting from the number 1. That is, the program prints out powers of
#  two in order.

# The execution of the program finishes when the next number to be printed wo
# uld be greater than the limit set by the user. No numbers greater than the 
# limit should be printed.
upper_limit = int(input("Please enter an upper limit: "))
number = 1
while number <= upper_limit:
    print(number)
    number *= 2