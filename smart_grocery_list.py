shopping_list = {}

yes_values = {'yes', 'y', 'yeah', 'yep'}

def clean(text):
    return text.strip().lower()

while True:

    action = clean(input("What would you like to do? Add? Remove? Or Finalize? "))

    if action == 'add':
        item = clean(input("What would you like to add? "))
        if not item:
            print("Invalid item.")
            continue

        if item in shopping_list:
            shopping_list[item] += 1
        else:
            shopping_list[item] = 1

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
            print(f'\u2022 {item.title()} x{count}')
                    
