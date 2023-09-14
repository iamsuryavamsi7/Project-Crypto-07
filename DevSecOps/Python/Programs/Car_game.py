command = ""
started = False

while command != "quit":
	print("Type 'help' if you dont' know the command's")
	command = input("> ").lower()
	
	if command == "start":
		if started:
			print("Car is already started")
		else:
			started = True
			print("Car is started")
	elif command == "stop":
		if not started:
			print("Car is already stopped")
		else:
			started = False
			print("Car is stopped")
	elif command ==  "quit":
		break
	elif command == "help":
		print("""
			start - To start the car
			stop - To stop the car
			help - To display this
			quit - To quit
		""")
	else:
		print("Sorry we can't able to understand your input")
