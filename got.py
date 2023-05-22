import time

def print_delay(text, delay=1.5):
    print(text)
    time.sleep(delay)

def game_over():
    print_delay("Game over! You have met a tragic end.")

def play_game():
    print_delay("Welcome to the world of Game of Thrones!")
    print_delay("You find yourself in the city of King's Landing.")
    print_delay("A great war has just ended, and the city lies in ruins.")
    print_delay("You are faced with a choice:")

    choice = input("Will you support Daenerys (D) or Jon Snow (J)? Enter D or J: ")

    if choice.lower() == "d":
        print_delay("You have chosen to support Daenerys.")
        print_delay("Daenerys has taken control of King's Landing.")
        print_delay("She addresses the crowd and declares herself the queen of the Seven Kingdoms.")
        print_delay("Do you agree with Daenerys' decision? (Y/N)")

        agreement = input("Enter Y or N: ")

        if agreement.lower() == "y":
            print_delay("You support Daenerys' decision and become a loyal follower.")
            print_delay("You live out your days as a trusted advisor in her new regime.")
            print_delay("Congratulations! You win the game!")
        elif agreement.lower() == "n":
            print_delay("You disagree with Daenerys' decision and confront her.")
            print_delay("Daenerys, blinded by power, orders her dragon to burn you alive.")
            game_over()
        else:
            print_delay("Invalid input.")
            play_game()
    elif choice.lower() == "j":
        print_delay("You have chosen to support Jon Snow.")
        print_delay("Jon Snow confronts Daenerys in the throne room.")
        print_delay("Will you try to reason with her or kill her to protect the realm? (R/K)")

        action = input("Enter R or K: ")

        if action.lower() == "r":
            print_delay("You try to reason with Daenerys, but she refuses to listen.")
            print_delay("In a fit of rage, Daenerys orders her dragon to attack you.")
            game_over()
        elif action.lower() == "k":
            print_delay("You decide to protect the realm and kill Daenerys.")
            print_delay("Jon Snow becomes known as the Queenslayer but gains the support of the Unsullied.")
            print_delay("He takes control of the Iron Throne temporarily to restore order.")
            print_delay("Do you accept the responsibility of ruling the Seven Kingdoms? (Y/N)")

            ruling = input("Enter Y or N: ")

            if ruling.lower() == "y":
                print_delay("You accept the responsibility and become the ruler of the Seven Kingdoms.")
                print_delay("Congratulations! You win the game!")
            elif ruling.lower() == "n":
                print_delay("You refuse to rule, and a council is formed to select the new ruler.")
                print_delay("You fade into obscurity but live a peaceful life.")
                print_delay("Congratulations! You win the game!")
            else:
                print_delay("Invalid input.")
                play_game()
        else:
            print_delay("Invalid input.")
            play_game()
    else:
        print_delay("Invalid input.")
        play_game()

play_game()
