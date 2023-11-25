# import string
# import random

# length = int(input("Enter password length: "))

# print('''Choose character set for password from these :
# 		1. Letters
# 		2. Digits
# 		3. Special characters
# 		4. Exit''')

# characterList = ""

# while(True):
# 	choice = int(input("Pick a number "))
# 	if(choice == 1):
		
# 		characterList += string.ascii_letters
# 	elif(choice == 2):
		
# 		characterList += string.digits
# 	elif(choice == 3):
		
# 		characterList += string.punctuation
# 	elif(choice == 4):
# 		break
# 	else:
# 		print("Please pick a valid option!")

# password = []

# for i in range(length):

# 	randomchar = random.choice(characterList)
	
# 	password.append(randomchar)

# print("The random password is " + "".join(password))


import string
import random

while True:
    try:
        length = int(input("Enter password length: "))
        if length > 0:
            break
        else:
            print("Please enter a positive integer for password length.")
    except ValueError:
        print("Please enter a valid integer for password length.")

print('''Choose character set for the password from these:
        1. Letters
        2. Digits
        3. Special characters
        4. Exit''')

characterList = ""

while True:
    choice = int(input("Pick a number "))
    if choice == 1:
        characterList += string.ascii_letters
    elif choice == 2:
        characterList += string.digits
    elif choice == 3:
        characterList += string.punctuation
    elif choice == 4:
        break
    else:
        print("Please pick a valid option!")

print("Selected character set:", characterList)

password = random.choices(characterList, k=length)

print(f"The random password is {''.join(password)}")
