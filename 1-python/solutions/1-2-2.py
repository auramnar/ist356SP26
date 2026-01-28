#Challenge 1-2-2¶
'''
Write a program to accept numbers until the user enters: 0

The program should count the number of positive and negative numbers entered, 
and print those values after the 0 is entered.
'''

# Count the numbers entered
# Count the positive numbers entered
# Count the negative numbers entered
# Create an indefinite loop that include a break statement to exit when 0 is inputted
# Prompt the user to enter numbers until they enter 0
# If the user enters 0, the loop stops immediately.
# Increments a count to keep track of how many numbers have been entered (excluding 0).
# If the user enters a positive number, increment a positive count.
# If the user enters a negative number, increment a negative count.
# After exiting the loop, print the total count of numbers entered, the count of positive numbers


count = 0
pos = 0
neg = 0


while True:
    number = float(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    count = count +1
    if number > 0:
        pos = pos +1
    else:
        neg = neg +1
        
print("You entered", count, "numbers")
print("Positive numbers:", pos) 
print("Negative numbers:", neg)
    