shopping_list = {}

def clean(text: str):
    return text

def clean_input(text: str):
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

while True:

    action = clean(input("What would you like to do? Add? Remove? Or Finalize? "))

    #add 
    if action == 'add':
        item, quantity = clean_input(input("What would you like to add? "))

        #In case input is blank or justa space
        if not item:
            print("Invalid item.")
            continue

        shopping_list[item] = shopping_list.get(item, 0) + quantity

    elif action == 'remove':
        item = clean(input("What would you like to remove? "))
        if not item:
            print("Invalid item.")
            continue

        if item in shopping_list:
            shopping_list[item] -= 1
            if shopping_list[item] == 0:
                shopping_list.pop(item)
        else:
            print("item not found.")

    elif action == 'finalize':
        break

    else:
        print("invalid option.")

    print("\n Current items:")
    if not shopping_list:
        print("empty")
    else:
        for item, count in shopping_list.items():
            print(f'\u2022 {item.lower()} x{count}')
