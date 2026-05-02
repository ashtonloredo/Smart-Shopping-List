import json

shopping_list = {}
agreement_values = {"yes", "y", "yeah", "yep", "yup", "save"}

#List functions
def clean(text: str): #Done
    return text.lower().strip()

def clean_input(text: str): #Done
    text = clean(text)

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
    item = name.strip()

    return item, quantity

def add_item(item, quantity): #Done
    shopping_list[item] = shopping_list.get(item, 0) + quantity

def remove_item(item, quantity): #Done
    if item not in shopping_list:
        return False
    shopping_list[item] -= quantity
    if shopping_list[item] <= 0:
        shopping_list.pop(item)
    return True
    
def display_list(): #Done
    print("\n Current items:")
    if not shopping_list:
        print("empty")
    else:
        for item, quantity in shopping_list.items():
            print(f'\u2022 {item.lower()} x{quantity}')

def save_list():
    from save_date import formatted_date

    with open("grocery_list.json", 'w') as f:
        json.dump(shopping_list, f, indent=4, sort_keys=True)
        print(f"\nList has been saved.\nLast saved: {formatted_date()}") #Date includes year/month/day hour/minute

def load_list():
    global shopping_list
    try:
        with open("grocery_list.json", 'r') as f:
            shopping_list = json.load(f)
        print("List has been loaded.")

    except FileNotFoundError:
        print("No saved list found.")
     
#Grocery List Logic
while True:

    action = clean(input("What would you like to do? Add? Remove? Load List? Or Finalize? "))

    #Add 
    if action == 'add':
        item, quantity = clean_input(input("What would you like to add? "))
        
        #In case input is blank or just a space
        if item is None:
            print("Invalid item.")
            continue
        
        add_item(item, quantity)
        display_list()

    #Remove 
    elif action == 'remove':
        item, quantity = clean_input(input("What would you like to remove? "))
        
        #In case input is blank or just a space
        if not item:
            print("Invalid item.")
            display_list()
            continue

        successful = remove_item(item, quantity)
        if not successful:
            print("Item not found.")
        display_list()

    elif action == 'finalize':
        display_list()
        
        save_list_question = input("Would you like to save your list? ")
        if clean(save_list_question) in agreement_values:
            save_list()
        
        break
        
    elif action in ('load', 'load list'):
        load_list()
        display_list()

    else:
        print("Invalid option.")
