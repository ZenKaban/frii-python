question_answer_dict = {
    "What is the band name, known for the phrase:'How much is the fish?' > ":       ["scooter",
                                                                                     "Scooter"
                                                                                     ],
    "The answer to the ultimate question of life, the universe and everything. > ": ["42",
                                                                                     "Fouty two",
                                                                                     "forty two",
                                                                                     ],
    "The answer is near. > ":                                                       ["near",
                                                                                     "what?",
                                                                                     ],
    }

print("I will ask 3 easy questions, have fun answering. To quit, type 'quit'.")

for key in question_answer_dict.keys():
    while True:
        user_answer = input(key)
        if user_answer in question_answer_dict.get(key):
            print('Correct! Next question!')
            break
        elif user_answer == "quit":
            input('As you wish. Press "Enter" to close the program. Goodbye!')
            quit()
        else:
            print('Incorrect answer. Try again')
