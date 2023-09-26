def shopping_cart():
    # Define the available items and their prices
    items = {'apple': 50.00, 'banana': 40.00,
             'orange': 30.00, 'bread': 15.00, 'milk': 10.00,'khari':23.00,'biscuit': 5.00, 'book': 32.00,'laptop': 1000.00}
    cart = []
    while True:
        print("Available Items : ")
        for item, price in items.items():
            print(f"{item.capitalize()} : ${price:.2f}")
        choice = input(
            "Enter Items to add your carts, or type 'checkout' to finish Shopping. : ")
        if choice.lower() == 'checkout':
            break
        elif choice.lower() not in items:
            print("Invalid input. Please Try Again.")
        else:
            cart.append(choice.lower())
            print(f"{choice.capitalize()} added to your cart.")
    total = sum([items[item] for item in cart])
    print(f"Your total cost is ${total:.2f}")

print(shopping_cart())