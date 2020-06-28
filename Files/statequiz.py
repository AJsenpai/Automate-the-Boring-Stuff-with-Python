# this program will create 3 quiz files with their answer sheet
# each file contains 50 quiz with 4 options ofcourse one of them is correct
# all the files will have questions shuffled cuz i know you like to cheat
from pathlib import Path
import random

# 50 states and their capital
capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "NewMexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "WestVirginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

quizdoc = Path("c:/Users/Jai/Desktop/Docs/quiz")
for quizNum in range(5):
    # answerKey = open(f"{quizdoc}/captials_quizAnswer{quizNum}.txt", "w")
    # quizFile = open(f"{quizdoc}/captials_quiz{quizNum}.txt", "w")
    with open(f"{quizdoc}/captials_quizAnswer{quizNum}.txt", "w") as answerKey, open(f"{quizdoc}/captials_quiz{quizNum}.txt", "w") as quizFile:
        quizFile.write("Name:\n\nDate:\n\n")
        quizFile.write((" " * 20) + f"State Capitals Quiz (Form{quizNum + 1})")
        quizFile.write("\n\n")

        # shuffle the order of states
        states = list(capitals.keys())
        random.shuffle(states)
        for questionNum in range(50):
            correct_answer = capitals[states[questionNum]]
            wrong_answers = list(capitals.values())
            del wrong_answers[wrong_answers.index(correct_answer)]
            wrong_answers = random.sample(wrong_answers, 3)
            answer_option = wrong_answers + [correct_answer]
            random.shuffle(answer_option)

            # writing content to files
            quizFile.write(f"{questionNum + 1}. What is the capital of {states[questionNum]}?\n")
            for i in range(4):
                quizFile.write(f" {'ABCD'[i]}. { answer_option[i]}\n")
            quizFile.write("\n\n")
            answerKey.write(f"{questionNum + 1}.{'ABCD'[answer_option.index(correct_answer)]}\n")
    
    # quizFile.close()
    # answerKey.close()
