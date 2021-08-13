#Level 1 - to read the numbers in a file called "Stocktake1.txt and add them all, then print the total

total = 0
my_file = open('stocktake1.txt')
for line in my_file.readlines():
	total = total + int(line)
print(f"The total of the numbers in the file is {total}")