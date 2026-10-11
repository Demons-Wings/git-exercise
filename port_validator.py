

raw = input("Enter the port number between 0 and 65535: ")

try: 
	port = int(raw)

	if 0 <= port <= 65535 :
		print(f"{port} is valid port")

	else: 
		print("You entered wrong port number!")
except ValueError:
	print("You entered invalid value. Kindly enter a number between 0 and 65535")