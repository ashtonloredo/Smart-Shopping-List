from shopping_list_functions import ShoppingList
from save_date import formatted_date

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

def display_list(sl):
    print("\nCurrent items:")

    items = sl.get_items()
    if not items:
        print("empty")

    else:
        for item, quantity in items.items():
            print(f'\u2022 {item} x{quantity}')

#Shopping List Logic

print("\nInitializing new list.")
sl = ShoppingList()

while True:
    display_list(sl)
    action = clean(input("""
What would you like to do?

\u2022 Add
\u2022 Remove
\u2022 Load List
\u2022 Finalize
> """))

    #Add 
    if action == 'add':
        item, quantity = clean_input(input("What would you like to add? "))

        #In case input is blank or just a space
        if not item:
            print("\nInvalid item.")
            continue

        sl.add_item(item, quantity)

    #Remove 
    elif action == 'remove':
        item, quantity = clean_input(input("What would you like to remove? "))

        #In case input is blank or just a space
        if not item:
            print("\nInvalid item.")
            continue

        successful = sl.remove_item(item, quantity)
        if not successful:
            print("\nItem not found.")

    elif action == 'finalize':
        save_list_question = input("Would you like to save your list? ")
        if clean(save_list_question) in agreement_values:

            if not sl.save_list():
                print("\nFile could not be saved")

            else:
                print(f"\nList has been saved.\nLast saved: {formatted_date()}") #Date includes year/month/day hour/minute
        break

    elif action in ('load', 'load list'):
        if not sl.load_list():
            print("\nNo saved list found.")
        else:
            print("\nList loaded.")
    else:
        print("\nInvalid option.")
