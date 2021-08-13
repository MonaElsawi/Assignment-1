#Level 2 -  displays each line in turn, asking the user for a number.
# Print a message at the end giving the sum of what they entered.

total = 0
my_file = open('stocktake2.txt')
for line in my_file.readlines():
    print(line)
    for character in line:
        if character.isdigit():
            number_available = int(character)
    number = input("How many would you like to record? ")
    while int(number) > number_available:
        number = input(f"TOO HIGH! Please enter a number <= {number_available}: ")
    total = total + int(number)
print(f"The total is {total}")