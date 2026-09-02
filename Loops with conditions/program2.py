#In the following loop we have the condition number < 10. 
# The block within the loop is executed only if the variable number is less than 10.
number = int(input("Please type in a number: "))

while number < 10:
    print(number)
    number += 1

print("Execution finished.")