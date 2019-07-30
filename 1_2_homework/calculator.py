def convert_to_number(number):
    e = True
    while e:
        try:
            first_number = float(number)
            e = False
            break
        except Exception:
            print("U enta text, enta numba")
    
    return first_number

def operation_converter(input_string, first_number, second_number):
    if input_string == "+":
        result = first_number + second_number
    elif input_string == "-":
        result = first_number - second_number
    elif input_string == "*":
        result = first_number * second_number
    elif input_string == "/":
        while second_number == 0.0:
            second_number_str = input(
                "U can't divide by zero, u fool. Try again. > ")
            second_number = convert_to_number(second_number_str)
        result = first_number / second_number
        

    return result


print('Dis is da calculata.')

first_number_str = input("Enta your first numba. > ")
first_number = convert_to_number(first_number_str)

while True:
    second_number = None
    operator = None
    drop_loop = False
    while second_number == None or operator == None:
        operator_or_number = input("Enta next numba or operata. > ")
        if operator_or_number not in "+-*/" and operator_or_number != "":
            second_number = convert_to_number(operator_or_number)
        elif operator_or_number in "+-*/":
            operator = operator_or_number
        if operator_or_number == "":
                print("Total: ", first_number)
                drop_loop = True
                break
    
    if not drop_loop:
        intermediate_result = operation_converter(
            operator, first_number, second_number)
        print("Intermediate result: ", intermediate_result)
        first_number = intermediate_result
    else:
        break

    


    

    
