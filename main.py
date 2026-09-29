import random

choice = True

while choice==True:

    print("Welcome to our number guessing game.")
    num_comp = random.randint(1,100)
    print(num_comp)
    num_get=int(input("Enter a number between 1 and 100: "))

    if num_get == num_comp:        
        print("Congratulations! You guessed the correct number.")
        get_choice = str(input("Do you want to play again? (y/n): "))
        if get_choice == "y":
            print("Starting a new game...")
            continue
        else:
            choice = False
            print("Thank you for playing! Goodbye.")
            break

    elif num_get < num_comp:
        print("Your guess is lower than the computer's number. Try again!")
        num_get=int(input("Enter a number between 1 and 100: "))

    elif num_get > num_comp:
        print("Your guess is higher than the computer's number. Try again!")
        num_get=int(input("Enter a number between 1 and 100: "))

    elif num_get < num_comp:
        print("Your guess is higher than the number. Try again")
        num_get=int(input("Enter a number between 1 and 100: "))
        
            