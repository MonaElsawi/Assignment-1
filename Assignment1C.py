#Level 3 -   lets the user specify a filename (such as “stocktake2.txt”) and a fruit. 
#It should read the file, look for the fruit appearing anywhere in the line, 
#and then add up the number at the start of the line.


# total = 0
# file_name = input("Which file would you like to open? ")
# fruit = input("which fruit would you like to look for? ")
# my_file = open(file_name)

# for line in my_file.readlines():
    # if fruit in line:
        # for character in line:
            # if character.isdigit():
                # total = total + int(character)
        # print(f"There are {total} {fruit}")

  
        # print(f"Sorry, we dont have this fruit")


import inflect
p = inflect.engine()

def look_for_fruit(fruit):
    my_file = open(file_name)
    total = 0
    found_fruit = 0
    for line in my_file.readlines():
        if fruit in line or p.plural(fruit) in line:
            found_fruit = 1
            fruit = fruit.title()
            for character in line:
                if character.isdigit():
                    total = total + int(character)
    if found_fruit == 1 and total == 1 and fruit.endswith('s'):
        fruit = p.plural(fruit)
        print(f"\nThere is {total} {fruit}.")
    elif found_fruit == 1 and total != 1 and fruit.endswith('s'):
        print(f"\nThere are {total} {fruit}.")
    elif found_fruit == 1 and total == 1 and fruit.endswith('s') == False:
        print(f"\nThere is {total} {fruit}.")
    elif found_fruit == 1 and total != 1 and fruit.endswith('s') == False:
        fruit = p.plural(fruit)
        print(f"\nThere are {total} {fruit}.")
    else:
        print(f"\nSorry, this fruit is not found.")
  
#fruit.endswith('s')  

file_name = input("\nWhich file would you like to open? ")
while True:
    fruit = input("\nwhich fruit would you like to look for? ")
    if fruit == '':
        break
    fruit = fruit.lower()    
    look_for_fruit(fruit)    