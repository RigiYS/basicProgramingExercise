products = []
while(True):
    # menu
    print("================================")
    print("Choose the menu:")
    print("1. List Products")
    print("2. Add a product")
    print("3. Remove a product by name")
    print("4. Remove a product by index")
    print("5. Exit")
    print("================================")
    
    choosen_menu = input("Please input a menu(1/2/3/4/5): ")
    
    if choosen_menu == "1":
        print("List products:")
        print(products)
    elif choosen_menu == "2":
        new_product = input("Add a new product: ")
        products.append(new_product)
    elif choosen_menu == "3":
        remove_product = input("Remove a product by name: ")
        products.remove(remove_product)
    elif choosen_menu == "4":
        products.pop(int(input("Remove a product by index: ")))
    elif choosen_menu == "5":
        break
    else:
        print("invalid input!")