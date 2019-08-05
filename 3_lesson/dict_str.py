def convert_keys_to_str(dict):
    new_dict = {}
    for key in dict:
        new_key = str(key)
        value = dict[key]
        new_dict[new_key] = value
    return new_dict


dict = {
    1:   "123",
    2:   "loh",
    2.6: "f",
    }
print(dict)
print(convert_keys_to_str(dict))