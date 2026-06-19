Save The Turtles: Gamifying household recycling for young children (ages 7 to 12)

Title and Description:
Save The Turtles is a modular, text-based educational game designed to gamify household recycling for children aged 7 to 12 years old, by tying digital habits to a digital pet turtle. Built with the United Nations Sustainable Development Goal 12 (Responsible Consumption and Production) in mind, this project plans to reverse low recycling rates by turning abstract concepts into immediate, simple feedback.  

Table of Contents:
1. Features
2. How to Run  
3. File Structure & Design Justification
4. Reflection & References 

## 1. Features 
-Tamagotchi-inspired Mascot Loop: Utilised OOP for its progression system, where proper recycling habits directly increase the turtle's mascot health and weight, while plastic contamination inflicts penalties.
-ReturnRight Tracker Calculator: Translates beverage containers carrying the BCRS Deposit Mark into real-world monetary savings, specifically tailored for kid-friendly goals (e.g. a $0.50 IKEA ice-cream)
-Eco fun-facts terminal: Displays local environmental trivia that players read to unlock advanced evolution stages for their mascot. 

## 2. How to Run
Prerequisites:
-Make sure you have Python 3 installed 
Installation & Execution:
-Download the repository (click on the green code button on the top right of this page and download zip.)
-Open the project (launch your terminal and open the unzipped folder)
-Start the program (type py main.py into the terminal to get started)

## 3. File Structure & Design Justification 
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

-.gitignore: Keeps local cache out of the cloud repository (e.g. __pycache__)

-requirements.txt: ensures a consistent developer environment (we need this later on for the tele bot)

## 4. Reflection
* Challenges Faced:
As this is our very first python project, we faced 2 massive hurdles:
-We spent a significant amount of time learning how to properly organise my code across different folders, and understanding the standard naming conventions. 
-This project forced us to move past writing small code to long-detailed scripts, and linking fundamental python concepts together to make a functional running program. 

* If we have 2 more weeks:
We will migrate this terminal game logic into a live telegram bot interface! As of now, we only understand how to generate a unique API token using Telegram's botfather... we plan to port this whole command loop over. We plan to leverage telebot event-driven decorators such that users can just trigger /quiz, /tracker, /ecofacts actions right from their phones. 
Additionally, we plan to figure out how to save users' game history via FileIO. 

* References:
https://dev.to/pwd9000/github-repository-best-practices-23ck 
https://github.com/worldbank/template 
https://worldbank.github.io/template/docs/folders-and-naming.html 
https://www.geeksforgeeks.org/python/overview-of-requirementstxt-and-direct-github-sources/ 


