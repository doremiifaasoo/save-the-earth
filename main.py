from src.mascot import TurtleMascot
from src.simulation import run_quiz

def main():
    print("Welcome to Save The Earth Game!! :-) ")
    pet_name = input("Give your pet turtle a name: ")
    my_turtle = TurtleMascot(pet_name)
    run_quiz(my_turtle)
    