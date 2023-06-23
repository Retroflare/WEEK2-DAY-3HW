# ### 1) Build a Shopping Cart <br>
# <p><b>You can use either lists or dictionaries. The program should have the following capabilities:</b><br><br>
# #1) Takes in input <br>
# 2) Stores user input into a dictionary or list <br>
# 3) The User can add or delete items <br>
# 4) The User can see current shopping list <br>
# 5) The program Loops until user 'quits' <br>
# 6) Upon quiting the program, print out all items in the user's list <br>
# </p>

def shopping_cart ():
    cart ={}
    while True: 
        print('1.shopping Cart menu')
        print("2. Add item")
        print("3.delete item")
        print("4.Quit")

        choice = input("Enter your choice(1-4):")

        if choice == "2":
            item = input("enter the item: ") 
            quantity  = input("enter the quantity: ") 
            cart[item] = quantity 
            print(f"added.{quantity} {item} in the cart.")

        if choice == "3":
            item = input("enter the item to delete: ") 
            if item in cart:
                del cart[item]
                print(f"{item} not in the cart.")


        if choice == "1":
            print("shopping cart list:")
            for item, quantity in cart.items():
                print(f"{item}:{quantity}")
           

        if choice == "4":
              print("pritinig all items in the shopping cart:")
              for items, quantity in cart.items():
                    print(f"{item}: {quantity}")
                    break
              
              else:
               print("Invalid option")
            
            
