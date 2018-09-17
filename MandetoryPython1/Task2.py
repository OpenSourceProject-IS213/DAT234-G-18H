from random import randint

# Create an array to store the 3 digits that the password is made up from.
password = []

# Generate 3 random digits and add them to the password array.
for i in range(3):

    password.append(randint(0, 9))

# Print out the 3 digits in the password so we can see what they are
print("Password consists of the following digits:")
for x in password:
    print(x)

print("\nFinding each digit in the password:")

# For each loop that iterates over each digit in the passowrd.
numberfound = False
for digit in password:
    counter = 0
    # Check if the digit is equal to the counter variable.
    # If it's not increment counter by 1 and check again
    # until a match is found.
    while numberfound == False:
        if counter == digit:
            print("Numer {} found!".format(digit))
            break
        else:
            counter += 1
        # If, for some reason, the loop fails to match a digit
        # print out an error mesaage (This should never happen).
        if counter > 9:
            print("Something went wrong!")
            break