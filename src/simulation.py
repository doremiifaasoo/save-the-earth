import json
def load_questions():
    with open("data/questions.json", "r") as file:
        return json.load(file)
    
def run_quiz(player_turtle):
    questions = load_questions()
    score = 0
    questions_answered = 0
    print("---Starting the Household Recycling Quiz---")

    for q_id, q_data in questions.items():
        print(f"{q_data['text']}")
        for option in q_data['options']:
            print(option)
        while True:
            player_answer = input("Your Answer: (A/B) or Q to Quit : ").strip().upper()
            if player_answer in ['A', 'B', 'Q']:
                questions_answered += 1
                break
            else:
                print("Invalid input! Please enter either A, B or Q.")
        if player_answer == 'Q':
            questions_answered -= 1
            print(f"Exiting the quiz early.. saving current stats...")
            break
        if player_answer == q_data['correct']:
            print("Correct!")
            print(f"Info: {q_data['explanation']}")
            score += 1
            player_turtle.feed_turtle()
        else:
            print("Wrong Answer...")
            print(f"The correct answer is: {q_data['correct']}")
            print(f"Info:{q_data['explanation']}")
            player_turtle.encounter_contamination()
    print(f"Quiz finished!! Your total score: {score}/{questions_answered} points attempted.")
