Save The Turtles: Gamifying household recycling for young children (ages 7 to 12)

Table of Contents:
Save The Turtles: An Overview
Project Structure

1. Save The Turtles: An Overview
Save The Turtles was created with the United Nations Sustainable Development Goals (SDGs) in mind-specifically SDG 12: Responsible Consumption and Production. Despite Singapore's strong recycling infrastructure, household recycling rates remain low due to limited visibility, motivation, and immediate feedback at the individual household level.

Save The Turtles bridges this gap by cultivating green habits from an early age. We target young children (ages 7 to 12), leveraging a digital turtle mascot inspired by the classic Tamagotchi loop. Because abstract concepts like "landfill capacity" are hard for children to comprehend, we give their habits a physical form. Proper recycling keeps their pet turtle healthy and growing, while plastic contamination makes their pet weak. This instantly internalises the real-world consequences of their choices.

To keep children excited and engaged, we feature a Recycling Tracker Calculator, which serves as a youth-friendly extension of Singapore's ReturnRight Scheme. Children log their physical recycling to watch their real-world 10-cent deposits add up. We translate these monetary rewards into tangible, kid-friendly milestones—showing them how close they are to securing a $0.50 IKEA ice-cream treat!

Finally, we have integrated a dedicated Eco Fun Facts terminal. This section introduces children to national initiatives (like the NEA Bloobox) and educational trivia. By housing these inside a gamified platform, children are naturally incentivised to explore the reading sections to help unlock new evolution stages for their turtle.

2. Project Structure
The project is organised in a modular, clean directory structure to separate data from our core game logic:

📁 data/
-data/questions.json: A structured JSON dictionary containing game scenarios, options, correct answers, and error-handling strings for the quiz.

-data/facts.json: A text database storing Singapore recycling facts and trivia.

-data/save_file.json: A local database utilising File I/O to securely save user profile states and mascot progression when the game closes.

📁 src/
-src/__init__.py: Initializer script that registers our src directory as a clean Python package.

-src/mascot.py: The Object-Oriented Blueprint (TurtleMascot class) defining attributes like health, weight, and dynamic growth stages.

-src/simulation.py: The quiz simulation engine that loops through data files and evaluates user responses.

-src/tracker.py: The mathematical calculation engine processing the Beverage Return Scheme deposits and Semakau landfill data.

-src/funfacts.py: The control loop allowing users to browse through recycling facts seamlessly.

Root
-main.py: The primary script and execution entry point for the entire game.