
# Challenge 1-2-1

'''
Write a program to accept a password as input. If the password input is "secret" display "access granted" else say "invalid password"
repeat the above up to 5 times. when the correct password is entered, stop looping when 5 loops have exhaused print "you are locked out"

# Stores the correct password in a variable
# Runs a loop 5 times, allowing 5 password attempts. 
# Prompts the user to enter a password.
    #If the password matches "secret":
        #Prints "access granted"
        #break exits the loop 
    #If the password is incorrect:
        
# The loop continues to the next attempt.
# Should the user fail to enter the correct password in 5 attempts, the loop ends.
# Print "too many failed attempts" if the user did not enter the password correctly in 5 tries.
'''

valid_pw = "secret"

for i in range(5):
    pw = input("Enter the password: ")
    if pw == valid_pw:
        print("access granted")
        break
    else:
        print("invalid password")
else:
    print("you are locked out")
