def main(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for user_input in input_string:
        if user_input not in vowels:
            result += user_input
    return result

x = input ("Input: ")
snake_case = main(x)
print ("Output:",snake_case)