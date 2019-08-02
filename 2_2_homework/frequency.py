# This is a script to build the frequency list on George Carlin's YOU ARE ALL DISEASED performance transcript
import re
import operator


def get_words_list(filename):
    words_list = []
    with open(filename, "r", encoding = "UTF-8") as text:
        for row in text:
            row = row.strip("\n")
            row = row.lower()
            row = re.sub(r"[^\w\s]", "", row)
            row_word_list = row.split(" ")
            for word in row_word_list:
                words_list.append(word)

    return words_list

def get_frequency_dict(words_list):
    frequency_dict = {}
    for word in words_list:
        count_word = 0
        for word_for_count in words_list:
            if word == word_for_count:
                count_word += 1
        frequency_dict[word] = count_word
        
    return frequency_dict


def get_sorted_frequency_list(frequency_dict):
    frequency_list = []
    for key in frequency_dict:
        frequency_list.append((key, frequency_dict.get(key)))
    frequency_list.sort(key = operator.itemgetter(1), reverse = True)
    return frequency_list


def table_print(frequency_list, top_rows, table_width):
    print("Word", " " * table_width, "Frequency")
    print("-" * (15 + table_width))
    for pair in frequency_list[:top_rows]:
        print(pair[0], " " * (table_width + (4 - len(pair[0]))), pair[1])


words_list = get_words_list("carlin.txt")
frequency_dict = get_frequency_dict(words_list)
frequency_list = get_sorted_frequency_list(frequency_dict)
table_print(frequency_list, top_rows=10, table_width=3)

