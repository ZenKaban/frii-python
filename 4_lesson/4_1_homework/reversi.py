from random import randint

def init_number_list():
    field_size = 15
    game_field_list = []
    while len(game_field_list) < field_size:
        random_number = randint(1, field_size)
        while random_number not in game_field_list:
            game_field_list.append(random_number)
            random_number = randint(1, field_size)
    
    return game_field_list

def init_game_field(game_field_list):
    
    # game_field_list.append(" ")
    count = 1
    main_list = []
    intermediate_list = []
    for number in game_field_list:
        intermediate_list.append(number)
        if count == len(game_field_list):
            intermediate_list.append(" ")
            main_list.append(intermediate_list)
            intermediate_list = []
        elif count % 4 == 0:
            main_list.append(intermediate_list)
            intermediate_list = []
            
        count += 1
    
    cursor_pos = [3, 3]
    
    return main_list, cursor_pos


def move_cursor(game_field, cursor_pos):
    x_init, y_init = cursor_pos
    user_input = input("Выберите направление смещения ячейки (left, right, up, down) > ")
    if user_input == "left":
        x_new = x_init
        y_new = y_init - 1
    elif user_input == "right":
        x_new = x_init
        y_new = y_init + 1
    elif user_input == "up":
        x_new = x_init - 1
        y_new = y_init
    elif user_input == "down":
        x_new = x_init + 1
        y_new = y_init
    exchanged_number = game_field[x_new][y_new]
    game_field[x_new][y_new] = "_"
    game_field[x_init][y_init] = exchanged_number
    
    return x_new, y_new
    
def print_game_field(game_field):
    count_row = 1
    for row in game_field:
        count = 1
        for number in row:
            print("{0:^4}".format(number), end="")
            if count % 4 == 0 and count_row != 4:
                print('\n', "-"*17)
            elif count % 4 == 0 and count_row == 4:
                print("\n")
                # print('')
            else:
                print("|", end="")
            count += 1
        count_row += 1
            

game = True
number_list = init_number_list()
game_field, init_cursor_pos = init_game_field(number_list)
sorted_number_list = number_list
sorted_number_list.sort()
sorted_game_field, unused = init_game_field(sorted_number_list)

while game:
    print_game_field(game_field)
    try:
        init_cursor_pos = move_cursor(game_field, init_cursor_pos)
    except Exception:
        print('неправильный ход')
    if game_field == sorted_game_field:
        print('Успех!')
        game = False
        



