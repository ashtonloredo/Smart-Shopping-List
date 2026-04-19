shopping_list = {}

yes_values = {'yes', 'y', 'yeah', 'yep'}
no_values = {'no', 'n', 'nah', 'nope'}

while True:

    if not shopping_list:
        response = input("Would you like to add an item? ").strip().lower()
        if response in no_values:
            break

        item = input("What would you like to add? ")
        shopping_list[item] = 1

    else:
        action = input("What would you like to do? Add? Or remove? ").strip().lower()

        if action == 'add':
            item = input("What would you like to add? ")
            if item in shopping_list:
                shopping_list[item] += 1
            else:
                shopping_list[item] = 1

        elif action == 'remove':
            item = input("What would you like to remove? ")
            if item in shopping_list:
                shopping_list[item] -= 1
                if shopping_list[item] == 0:
                    shopping_list.pop(item)
            else:
                print("item not found.")

        elif action == 'finalize':
            confirm = input("Finalize list? ").strip().lower()
            if confirm in yes_values:
                break

        else:
            print("invalid option.")
    
    for item, count in shopping_list.items():
        print(f'{item} x{count}.')
                    
