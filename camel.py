def add_underscore(user_input):
    modified_string = ""

    #for character in the user_input (in this function)
    for char in user_input:
        if char.isupper():
            modified_string += "_" + char
        else:
            modified_string += char
    return modified_string

user_input = input("camelCase: ")
output = add_underscore(user_input)
print ("snake_case:", output.lower())