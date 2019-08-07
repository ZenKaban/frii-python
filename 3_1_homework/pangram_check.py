def get_character_frequency(string):
    alphabet_dict = {"а": 0,
                     "б": 0,
                     "в": 0,
                     "г": 0,
                     "д": 0,
                     "е": 0,
                     "ё": 0,
                     "ж": 0,
                     "з": 0,
                     "и": 0,
                     "й": 0,
                     "к": 0,
                     "л": 0,
                     "м": 0,
                     "н": 0,
                     "о": 0,
                     "п": 0,
                     "р": 0,
                     "с": 0,
                     "т": 0,
                     "у": 0,
                     "ф": 0,
                     "х": 0,
                     "ц": 0,
                     "ч": 0,
                     "ш": 0,
                     "щ": 0,
                     "ъ": 0,
                     "ы": 0,
                     "ь": 0,
                     "э": 0,
                     "ю": 0,
                     "я": 0
}

    for char in string:
        char = char.lower()
        if char not in " ,.!?":
            alphabet_dict[char] = alphabet_dict[char] + 1

    return alphabet_dict

def check_if_pangram(alphabet_dict):
    missing_char_list = []
    for char in alphabet_dict:
        if alphabet_dict[char] == 0:
            missing_char_list.append(char)
    
    if len(missing_char_list) > 1:
        print("Это не панграмма, не хватает букв: ", missing_char_list)

    else:
        print("Успех, это панграмма")

        
while True:
    string = input("Введите строку для проверки: ")
    alphabet_dict = get_character_frequency(string)
    check_if_pangram(alphabet_dict)
    stop = input("Хотите попробовать еще раз? Введите 'да' или 'нет': ")
    if stop.lower() == "нет":
        break
