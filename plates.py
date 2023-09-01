def main():
    plate = (input("Plate: "))
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if is_valid1(s) and is_valid2(s) and is_valid4(s) and is_valid5(s):
        return True

def is_valid1(a):
    if a[:2].isalpha():
        return True

def is_valid2(b):
    if 2<=len(b)<=6:
        return True

def is_valid4(d):
    if any(char not in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" for char in d):
        return True

def is_valid5(e):
    if any(char for char in e if char.isdigit):
        first_digit = next((char for char in e if char.isdigit()), None)
        if first_digit != '0' and e[-1].isdigit():
            return True

main()
