def create_word_object(word):
    word_dict = {}
    char_count = 0
    for char in word:
        word_dict[char_count] = "_"
        char_count += 1
    return word_dict


def check_char_in_word(input_char, used_chars_list, word):
    if input_char in used_chars_list:
        print("Такую букву уже называли!")
    else:
        used_chars_list.append(input_char)
        if input_char in word:
            print("Есть такая буква!", end=" ")
        else:
            print("Нет такой буквы!", end=" ")
    
       
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
    

def print_game_status(word_dict):
    word_chars_list = []
    for key in word_dict:
        word_chars_list.append(word_dict[key])
    for char in word_chars_list:
        print(char, end=" ")
    print("")


def check_if_game_complete(word_dict):
    game_complete = True
    for key in word_dict:
        if word_dict[key] == "_":
            game_complete = False
            break
    return game_complete


print("Добро пожаловать в Поле Чудес!")

word = ("python")
print("Это змея:","_ "*len(word))
word_dict = create_word_object(word)
used_chars_list = []
game_complete = False

while game_complete is False:
    input_char = input("Введите букву: ")
    check_char_in_word(input_char=input_char, used_chars_list=used_chars_list, word=word)
    char_position_list=return_char_position(input_char=input_char, word=word)
    change_game_status(input_char=input_char, word_dict=word_dict, char_position_list=char_position_list)
    print_game_status(word_dict=word_dict)
    game_complete = check_if_game_complete(word_dict=word_dict)
    if game_complete:
        print("Поздравляем, вы отгадали слово!: ", word)
    




