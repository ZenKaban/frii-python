image = [r"""
 _________
| /
|/
|
|
|
|
|
|
|
|
|________________""",
         r"""
 ________
| /   ___|___
|/   | o   o |
|    |___-___|
|
|
|
|
|
|
|
|________________""",
         r"""
 ________
| /   ___|___
|/   | o   o |
|    |___-___|
|        |
|        |
|        |
|        |
|
|
|
|________________""",
         r"""
 ________
| /   ___|___
|/   | o   o |
|    |___-___|
|       /|
|      / |
|     /  |
|        |
|
|
|
|________________""",
         r"""
 ________
| /   ___|___
|/   | o   o |
|    |___-___|
|       /|\
|      / | \
|     /  |  \
|        |
|
|
|
|________________""",
         r"""
 ________
| /   ___|___
|/   | o   o |
|    |___-___|
|       /|\
|      / | \
|     /  |  \
|        |
|       /
|      /
|
|________________""",
         r"""
 ________
| /   ___|___
|/   | x   x |
|    |___-___|
|       /|\
|      / | \
|     /  |  \
|        |
|       / \
|      /   \
|
|________________"""
         ]


def create_word_object(word):
    word_dict = {}
    char_count = 0
    for _ in word:
        word_dict[char_count] = "_"
        char_count += 1
    return word_dict


def check_char_in_word(input_char, used_chars_list, word, false_tries):
    if input_char in used_chars_list:
        print("Такую букву уже называли!")
    else:
        used_chars_list.append(input_char)
        if input_char in word:
            print("Есть такая буква!")
        else:
            print("Нет такой буквы!")
            false_tries += 1
    
    return false_tries


def return_char_position(input_char, word):
    char_count = 0
    char_position_list = []
    for char in word:
        if input_char == char:
            char_position = char_count
            char_position_list.append(char_position)
        char_count += 1
    
    return char_position_list


def change_game_status(input_char, word_dict, char_position_list):
    for position in char_position_list:
        word_dict[position] = input_char


def print_game_status(word_dict, false_tries, image):
    print(image[false_tries])
    word_chars_list = []
    for key in word_dict:
        word_chars_list.append(word_dict[key])
    for char in word_chars_list:
        print(char, end = " ")
    print("")


def check_if_game_complete(word_dict, false_tries):
    game_won = True
    game_lost = False
    for key in word_dict:
        if word_dict[key] == "_":
            game_won = False
            break
    
    if false_tries >5:
        game_lost = True
    
    if game_won and not game_lost:
        game_complete = "Вы победили"
    elif not game_won and not game_lost:
        game_complete = None
    else:
        game_complete = "Вы проиграли"
    
    return game_complete



print("Добро пожаловать в Виселицу!")

word = ("виселица")
print(image[0])
print("_ " * len(word))
word_dict = create_word_object(word)
used_chars_list = []
game_complete = None
false_tries = 0

while game_complete is None:
    input_char = input("Введите букву: ")
    false_tries = check_char_in_word(input_char = input_char, used_chars_list = used_chars_list, word = word, false_tries=false_tries)
    char_position_list = return_char_position(input_char = input_char, word = word)
    change_game_status(input_char = input_char, word_dict = word_dict, char_position_list = char_position_list)
    print_game_status(word_dict = word_dict, image=image, false_tries=false_tries)
    # print("Ошибочных попыток:", false_tries, "/6")
    game_complete = check_if_game_complete(word_dict = word_dict, false_tries = false_tries)
    if game_complete:
        print(game_complete)