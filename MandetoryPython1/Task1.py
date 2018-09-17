# Generate a list of usernames.
username_list = ["sannitie", "sickvng", "insaniac", "endralos", "alek", "peli", "estrella"]

# Generate a list of names.
name_list = ["Snorre Tunge", "Gregor Inkovich", "Rafael Mingorno", "Jacob Kang",
             "Isak Kristiansen", "Trond Skorpen", "Nathalia Morrison"]

# Set a counter we can use to retriece the n-th item from each list
# while iterating through them
counter = 0

# For each loop that prints out all the items in both lists simultaniously.
# This requires the lists to have a 1 to 1 correspondence with username
# and name and the username that belongs together in the same position in both lists.
for uname in username_list:
    temp_u_name = name_list[counter]
    temp_name = username_list[counter]
    print("{}: {}".format(name_list[counter], username_list[counter]))
    counter += 1