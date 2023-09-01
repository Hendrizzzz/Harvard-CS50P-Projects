def main():
    expression = (input("Expression: "))
    x, y, z = (expression.split(" "))

    a = float(x)
    b = (y)
    c = float (z)
    if b == "+":
        print (round(a + c, 1))
    elif b == "-":
        print (round(a - c, 1))
    elif b == "*":
        print (round(a * c, 1))
    else:
        print (round(a / c, 1))
main()
