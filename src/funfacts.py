import json
def load_facts():
    with open("data/facts.json", "r") as file:
        return json.load(file)
def read_eco_facts(player_turtle):
    facts = load_facts()
    read_this_session = set()
    while True:
        print("Welcome to the Eco Fun Facts Library!")
        print("Learn a new fact to BOOST your turtle's wellness")
        for num, data in facts.items():
            status = 'COMPLETED' if num in read_this_session else 'LOCKED'
            print(f'[{num}] {data['title']} ({status})')
        print('[Q] Quit and return to main menu')
        user_choice = input(f'Select a topic from 1 to {len(facts)} or Q to exit: ').strip().upper()
        if user_choice == 'Q':
            print('Leaving the fact library... Remember to put your green facts to use!')
            break
        if user_choice in facts:
            selected_fact = facts[user_choice]
            print(f'{selected_fact['title'].upper()}')
            print(selected_fact['fact'])
            if user_choice not in read_this_session:
                read_this_session.add(user_choice)
                player_turtle.health = min(100, player_turtle.health + 2)
                player_turtle.weight_grams += 5
                print(f'Knowledge is power! {player_turtle.name} feels wiser :p')
            else:
                print('You have already unlocked this fact in this session.')
            input('Press ENTER to return to the fact library...')
        else:
            print(f'Oops! Please enter a valid number between 1 and {len(facts)} or Q to Quit.')
