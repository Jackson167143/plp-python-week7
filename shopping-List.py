# Part B - Shopping List Manager

shopping_list = []

while True:
    print("\nMenu: add / remove / show / done")
    choice = input("What do you want to do? ").strip().lower()

    if choice == "add":
        item = input("Enter the item to add: ").strip()

        if item:
            shopping_list.append(item)
            print(f"{item} has been added.")
        else:
            print("Please enter an item.")

    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if shopping_list:
            print("\nYour shopping list:")
            for item in shopping_list:
                print("-", item)
        else:
            print("Your shopping list is empty.")

    elif choice == "done":
        print("Goodbye! Thank you for using the Shopping List Manager.")
        break

    else:
        print("Invalid choice. Please choose add, remove, show, or done.")