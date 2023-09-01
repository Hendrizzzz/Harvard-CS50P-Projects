def main():
	y = input("File name: ")
	x = y.strip().lower()
	if gif(x):
		print ("image/gif")
	elif jpg(x) or jpeg(x):
		print ("image/jpeg")
	elif png(x):
		print ("image/png")
	elif pdf(x):
		print ("application/pdf")
	elif txt(x):
		print ("text/plain")
	elif zip(x):
		print ("application/zip")
	else:
		print ("application/octet-stream")

def gif(a):
	return a.endswith (".gif")

def jpg(a):
	return a.endswith(".jpg")

def jpeg(a):
	return a.endswith(".jpeg")

def png(a):
	return a.endswith(".png")

def pdf(a):
	return a.endswith(".pdf")

def txt(a):
	return a.endswith(".txt")

def zip(a):
    return a.endswith(".zip")

main()
