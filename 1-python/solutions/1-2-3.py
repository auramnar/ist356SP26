#Challenge 1-2-3¶
'''
Write a sentinel controlled loop to input a color until "quit" is entered. add each color to a list 
only when the color is not already in the list print the list each time in the loop.
'''

# Create an empty list. This list will store the colors entered by the user.
# Start an indefnite loop. The program will run break is entered
# Prompt the user to enter a color
# If the user enters "exit", break the loop
# Otherwise, add the color to the list
# Check if the color is already in the list
# If the color is not in the list, add it to the list
# Include a message that says the color was added to the list
# If the color is already in the list, include a message that says the color is already in the list
# Print the list of colors entered by the user


colors = []
while True:
    color = input("Enter a color (or 'quit' to exit): ")
    if color == "quit":
        print("Exiting the program.")
        break
    if color not in colors:
        colors.append(color)
        print(f"{color} added to the list.")
    else:
        print(f"{color} is already in the list.")
print("Final list of colors entered:", colors)
