from random import randrange


WEAPONS = {1: "Rock", 2: "Paper", 3: "Scissors"}

def get_user_weapon():
    
    while True:
        print("SELECT YOUR WEAPON (1-3)")
        print("*" *30)
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        try:
            choice = int(input("Enter your Weapon: "))
            if choice in WEAPONS:
                return choice
            else:
                print("Invalid choice, please enter 1, 2, or 3.\n")
        except ValueError:
            print("Please enter a number!\n")

def get_opponent_weapon():
    
    return randrange(1, 4)

def determine_winner(user, opp):
   
    if user == opp:
       
        print("It's a tie!")
    elif (user == 1 and opp == 3):
        print("You win, rock crushes scissors!")
    elif (user == 2 and opp == 1):
        print("You win, paper covers rock!")
    elif (user == 3 and opp == 2):
        print("You win, scissors cut paper!")
    elif (opp == 1 and user == 3):
        print("You lose, rock crushes scissors!")
    elif (opp == 2 and user == 1):
        print("You lose, paper covers rock!")
    elif (opp == 3 and user == 2):
        print("You lose, scissors cut paper!")
        

def main():
    
    play_again = "y"

    while play_again.lower() == "y":
        user_weapon = get_user_weapon()
        opp_weapon = get_opponent_weapon()
        determine_winner(user_weapon, opp_weapon)
        play_again = input("Want to play again (y/n): ")

if __name__ == "__main__":
    main()
    print("_" *50)
    print("\nThanks for playing! Completed by Shivang Dhamecha")
    print("_" *50)
