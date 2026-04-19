shopping_list = {}

yes_values = {'yes', 'y', 'yeah', 'yep'}
no_values = {'no', 'n', 'nah', 'nope'}

def clean(text):
    return text.strip().lower()

while True:

    if not shopping_list:
        response = clean(input("Would you like to add an item? "))
        if response in no_values:
            break

        item = clean(input("What would you like to add? "))
        shopping_list[item] = 1

    else:
        action = clean(input("What would you like to do? Add? Or remove? "))

        if action == 'add':
            item = clean(input("What would you like to add? "))
            if item in shopping_list:
                shopping_list[item] += 1
            else:
                shopping_list[item] = 1

        elif action == 'remove':
            item = clean(input("What would you like to remove? "))
            if item in shopping_list:
                shopping_list[item] -= 1
                if shopping_list[item] == 0:
                    shopping_list.pop(item)
            else:
                print("item not found.")

        elif action == 'finalize':
            confirm = clean(input("Finalize list? "))
            if confirm in yes_values:
                break

        else:
            print("invalid option.")
    
    for item, count in shopping_list.items():
        print(f'{item} x{count}.')
                    
