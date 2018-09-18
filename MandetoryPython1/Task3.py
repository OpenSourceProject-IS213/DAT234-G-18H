password_list = {"chris":"helloworld", "john":"passw1", "nelly":"2hell1", "wendy":"1Passw"}


has_capital_letter = False
#for index, key in enumerate(password_list):
for key in password_list:
    password = [password_list[key]]
    print(password)
    if password[0].isdigit():
        for index, letter in enumerate(password, start=1):
            print("xD")
            if letter.isupper():
                print("yay")