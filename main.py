from src.mascot import TurtleMascot
from src.simulation import run_quiz
from src.tracker import log_bottles_recycled
from src.funfacts import read_eco_facts

def main():
    print("Welcome to Save The Turtles!! :-) ")
    pet_name = input("Give your pet turtle a name: ").strip()
    if not pet_name:
        pet_name = 'Bubbles'
    my_turtle = TurtleMascot(pet_name)
    print(f"{my_turtle.name} the Turtle has hatched! Let's protect our environment")
    while True:
        print("---Main Menu---")
        print(f'Mascot: {my_turtle.name} | Health: {my_turtle.health}/100 | Weight: {my_turtle.weight_grams}g')
        print(f'Current Stage: {my_turtle.get_stage()}')
        print('--------')
        print('[1] Play the Educational Recycling Quiz')
        print('[2] Log Daily Recycled Bottles *Part of the ReturnRight Scheme!*')
        print('[3] Open the Eco Fun Facts Library')
        print('[Q] Save and Exit Game')
        print('--------')
        user_selection = input("What would you like to do today? ").strip().upper()
        if user_selection == '1':
            run_quiz(my_turtle)
        elif user_selection == '2':
            log_bottles_recycled(my_turtle)
        elif user_selection == '3':
            read_eco_facts(my_turtle)
        elif user_selection == 'Q':
            print('Saving Progress.. Thank you for keeping Singapore clean and green!')
            print(f'{my_turtle.name} will miss you! Come back soon :-(')
            break
        else:
            print('Invalid input. Please enter only (1,2,3 or Q)')

if __name__ == "__main__":
    main()