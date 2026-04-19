user_list = []

yes_values = {'yes', 'y', 'yeah', 'yep'}
no_values = {'no', 'n', 'nah', 'nope'}

remove_values = {}
items_string = ""

while True:

    if not user_list:
        response = input("Would you like to add an item? ").strip().lower()
        if response in no_values:
            break

        item = input("What would you like to add? ")
        user_list.append(item)

    else:
        action = input("What would you like to do? Add? Or remove? ").strip().lower()

        if action == 'add':
            item = input("What would you like to add? ")
            user_list.append(item)

        elif action == 'remove':
            item = input("What would you like to remove? ")
            if item in user_list:
                user_list.remove(item)
            else:
                print("item not found.")

        elif action == 'finalize':
            confirm = input("Finalize list? ").strip().lower()
            if confirm in yes_values:
                break

        else:
            print("invalid option.")
    
    print("Current items:", " ".join(user_list), ",")
                    