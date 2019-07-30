question_answer_list = [
    ("What is the band name, known for the phrase:'How much is the fish?' > ", "scooter"),
    ("The answer to the ultimate question of life, the universe and everything. > ", "42"),
    ("The answer is near. > ", "near")]

print("I will ask 3 easy questions, have fun answering. To quit, type 'quit'.")

for question, answer in question_answer_list:
    while True:
        user_answer = input(question)
        if user_answer.lower() == answer:
            print('Correct! Next question.')
            break
        elif user_answer == "quit":
            input('As you wish. Press "Enter" to close the program. Goodbye!')
            quit()
        else:
            print('Incorrect answer. Try again')


