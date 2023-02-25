# input: three integers from the user
# processing: find the sum of the three integers and the largest of the three
# output: largest and total
#
# References:
#   https://www.w3schools.com/python/python_user_input.asp
#   https://www.w3schools.com/python/python_conditions.asp
#   https://www.w3schools.com/python/ref_func_max.asp
#   https://www.w3schools.com/python/ref_func_sum.asp

print("\nRoss's Largest of Three Program")

# input three integers from the user.
num1 = int(input("\nEnter your first number: "))
num2 = int(input("\nEnter your second number: "))
num3 = int(input("\nEnter your final number: "))

# print user selections
print("Your numbers are: " + str(num1) + ", " + str(num2) + ", " + str(num3))

# determine largest number and print result
largest = max(num1, num2, num3)
print("\n The largest of these numbers is: " + str(largest))

# determine sum and print result
numTotal = num1 + num2 + num3
print("\n The sum of these numbers is: " + str(numTotal))

