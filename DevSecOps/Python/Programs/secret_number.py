secret_number = 7
initial_count = 0
initial_limit = 3

while initial_count < initial_limit:
	guess = int(input("Guess the secret number:- "))
	initial_count += 1

	if guess == secret_number:
		print("You won!")
		break
else:
	print("Sorry try again")
