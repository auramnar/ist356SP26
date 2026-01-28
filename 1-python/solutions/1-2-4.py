#Challenge 1-2-4¶
'''
Write a program to create a shopping list.

loop until "quit" is entered. input a grocery item input a quantity save the item as the key in the dictionary 
and quantity as the value if the item is in the dictionary already, add the quantity to the existing value.

'''

# Create an empty dictionary. Remember it stores data in key : value pairs.
# Start an indefinite loop to prompt the user to enter the data.
# Prompt the user for the item.
# If the user enters "quit", break the loop.
# Otherwise, prompt the user for the quantity.
# Convert the quantity to an integer.
# Check if the item already exists in the dictionary
# If it does, update the quantity by adding the new quantity to the existing quantity.
# If the iten already exist add the new quantity to the existing quantity.
# If the item does not exist, add the item to the dictionary with the quantity.
# Print the updated dictionary after each entry.
# Print the final dictionary after the loop ends.



items = {} 

while True:
    item = input("Enter an item")
    if item == "quit":
        print("Exiting the program.")
        break
    
    qty = int(input("Enter the quantity:"))
    if item in items.keys(): # check if in dictionary
        print(f"{item} found in list, updating quantity")
        items[item] = items[item] + qty # update quantity
    else:
        items[item] = qty # item not found so add new key:value pair
        print(f"{item} added to the list with quantity {qty}")
    print("ITEMS:", items ) #print after update
print("Final shopping list:", items) # print after exiting 

