numbers = [2, 2, 3, 4, 5, 5, 5, 6, 7, 7]
uniques = []

for number in numbers:
	if number not in uniques:
		uniques.append(number)
print(uniques)
