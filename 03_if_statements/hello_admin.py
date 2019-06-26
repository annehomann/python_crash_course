# usernames = ['anne', 'somerset', 'admin', 'sally', 'darius']

# for username in usernames:
#     if 'admin' in username:
#         print("Hello " + username.title() + ", would you like to see a status report?")
#     else:
#         print("Hello " + username + ", thank you for logging in today.")




# Using the if statement first allows you to check if the list is empty or not first

usernames = []

if usernames:
    for username in usernames:
        print("Hello " + username + ".")
else:
    print("We need to find some users!")