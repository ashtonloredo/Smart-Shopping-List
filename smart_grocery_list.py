shopping_list = {}

agreement_values = {"yes", "y", "yeah", "yep", "yup"}

def clean(text: str): #Done
    return text.lower().strip()

def clean_input(text: str): #Done
    text = text.lower().strip()#.replace(" ", "")

    number = ""
    name = ""

    for char in text:
        if char.isdigit():
            number += char
        elif char.isalpha() or char.isspace():
            name += char

    if number:
        quantity = int(number)
    else:
        quantity = 1
    item = name.replace('x', '').strip()

    
    return item, quantity

def add_item(item, quantity): #Done
    shopping_list[item] = shopping_list.get(item, 0) + quantity

def remove_item(item, quantity): #Done
    shopping_list[item] -= quantity
    if shopping_list[item] <= 0:
        shopping_list.pop(item)

def display_list():
    print("\n Current items:")
    if not shopping_list:
        print("empty")
    else:
        for item, quantity in shopping_list.items():
            print(f'\u2022 {item.lower()} x{quantity}')

while True:

    action = clean(input("What would you like to do? Add? Remove? Or Finalize? "))

    #add 
    if action == 'add':
        item, quantity = clean_input(input("What would you like to add? "))
        #In case input is blank or justa space

        if not item:
            print("Invalid item.")
            continue
        
        add_item(item, quantity)


    elif action == 'remove':
        item, quantity = clean_input(input("What would you like to remove? "))
        
        if not item:
            print("Invalid item.")
            continue

        elif item in shopping_list: 
            remove_item(item, quantity)

        else:
            print("item not found.")

    elif action == 'finalize':
        response = input("Would you like to see your finalized list? ")
        if clean(response) in agreement_values:
            display_list()
        else:
            break

    else:
        print("invalid option.")
