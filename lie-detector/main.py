import random

# define a list of questions

questions = [

    "Did you eat breakfast this mroning?",
    "Ddid you go to bed before midnight last night?",
    "Have you ever cheated on a test?",
    "Do you like your boss?",
    "Have you ever lied to your parents?",
    "Have you ever stonlen something?",
    "Do you believe in ghosts?",
    "Have you ever broekn the law?",
    "Do you think you're a good person?",

]

# Loop through each question and ask user for response
for question in questions:
    response = input(question + "(yes or no):").lower()

    if response == "yes":
        user_answer = True
    else:
        user_answer = False

    # Randomly generate a response and compare it to the user response
    random_answer = bool(random.getrandbits(1))  # readme
