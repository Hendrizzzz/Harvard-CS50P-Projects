def main():
    x = input("What time is it? ")
    x = convert(x)
    if 7.00 <= x <= 8.00:
        print ("breakfast time")
    elif 12.00 <= x <= 13.00:
        print("lunch time")
    elif 18.00 <= x <= 19.00:
         print("dinner time")
    else:
    	print("")

def convert(time):
	c, d= time.split(":")
	hour = float(c)
	minute = float(d)
	minutes = minute/60
	decimal = hour + minutes
	return decimal

if __name__ == "__main__":
    main()