x = 50
while x > 0:
    accepted_cents = [50,25,10,5]
    n = int(input (f"Amount Due: {x}\nInsert Coin: "))
    #to verify if n is 50,25,10 . if not then just print x
    if n in accepted_cents:
        amount_left = x - n
        x = amount_left
if x <= 0:
    x = abs(x)
    print((f"Change Owed: {x}"))