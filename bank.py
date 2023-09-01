def main():
	y = input("Greeting: ")
	x = y.strip().lower()
	if hello(x):
		print ("$0")
	elif h(x):
		print ("$20")
	else:
		print ("$100")

def hello(a):
	if a.startswith ("hello"):
		return True
	else:
		return False

def h(a):
	if a.startswith("h"):
		return True
	else:
		return False

main()
