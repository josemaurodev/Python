''' def adventure_game():

        print("Welcome to the dungeon! Your goal is to find the treasure.")
        print("Choose your actions carefully to avoid traps and mistakes.")

        try:
            print("\nYou are standing before three doors: [1, 2, 3]")
            door = int(input("Which door do you choose? "))

            if door == 1:
                print("You encountered a monster! It attacks you, but you manage to escape.")
            elif door == 2:
                print("Congratulations! You found the treasure!")
                return
            elif door == 3:
                print("Oops, you fell into a hole and lost the game.")
            else:
                print("That door doesn't exist!")
        except ValueError:
            print("Error: You must enter a number.")
        finally:
            print("End of this round.")
        
        try:
            print("\nYou find a locked chest.")
            print("Choose what to do: [1] Open it with a key, [2] Try to force the lock")
            choice = int(input("What do you do? "))

            if choice == 1:
                print("You opened the chest and found a trap! Be more careful next time.")
            elif choice == 2:
                print("You broke the lock and found a magic potion!")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Error: You must enter a number.")
        finally:
            print("End of the game!")
            
adventure_game() '''

import random

def business_fair():
    print("Welcome to the Business Fair!")
    print("Your goal is to earn $200 by managing your purchases and sales.\n")

    balance = 100
    products = {"apple": 2, "banana": 1, "orange": 3}

    while balance > 0:
        print(f"Current balance: ${balance}")
        balance = lightning_draw(balance)
        print("Available products for purchase:")
        for product, price in products.items():
            print(f"- {product.capitalize()}: ${price} each")
        
        try:
            action = input("\nDo you want to [buy/sell/exit]? ").strip().lower()

            if action == "buy":
                product = input("Enter the name of the product you want to buy: ").strip().lower()
                if product not in products:
                    print("Error: Product not available.")
                    continue
            
                quantity = int(input(f"How many {product}s do you want to buy? "))
                cost = products[product] * quantity
                
                if cost > balance:
                    print("Error: Insufficient balance for this purchase.")
                else:
                    balance -= cost
                    print(f"You bought {quantity} {product}(s) for ${cost}.")
            elif action == "sell":
                product = input("Enter the name of the product you want to sell: ").strip().lower()
                if product not in products:
                    print("Error: You don't have this product to sell.")
                    continue

                sale_price = products[product] + random.randint(1, 3)
                print(f"The customer is offering ${sale_price} per unit of {product}.")

                quantity = int(input(f"How many {product}s do you want to sell? "))
                profit = sale_price * quantity
                balance += profit
                print(f"You sold {quantity} {product}(s) and earned ${profit}.")
            elif action == "exit":
                print("You ended the game.")
                break
            else:
                print("Error: Invalid action. Choose [buy/sell/exit].")
        except ValueError:
            print("Error: Invalid input. Make sure to enter numbers for quantities.")
        
        print("\n---\n")

        if balance >= 200:
            print("Congratulations! You reached the expected profit and won the game!")
            break
        elif balance <= 0:
            print("Game over! You lost all your money. Try again.")
            break

def lightning_draw(balance):
    if random.randint(1, 10) == 1:
        print("Congratulations! You won $10 in the lightning draw!")
        balance += 10
    return balance

business_fair()