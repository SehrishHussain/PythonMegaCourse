# Coding Exercise 2
#
# ips = ['100.122.133.105', '100.122.133.111']
#
# Copy-paste the ips list in a .py file and extend the program so it:
#
# 1. Prompts the user to input an index (e.g, 0 or 1).
#
# 2. Returns the IP address that has that index.
#
# Here is how the program would behave when executed:

#ips = ['100.122.133.105', '100.122.133.111']

#number = int(input("Enter the index of the IP you want: "))

#print("You chose", ips[number])

################BUG FIXING##################

# menu = ["pasta", "pizza", "salad"]
#
# user_choice = int(input("Enter the index of the item: "))
#
# message = f"You chose {menu[user_choice]}."
# print(message)

#################################################

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    row = f"{i}.{j}"
    print(row)