current_users = ['anne', 'cathy', 'mike', 'eli', 'laura', 'shane']
new_users = ['doris', 'jane', 'DAVE', 'eli', 'ash', 'cathy']

for new_user in new_users:
    if new_user in current_users:
        print(new_user + " has already been taken. Select another username.")
    elif new_user != new_user.lower():
        print("Caps not accepted. Please try again")
    else:
        print("Thank you for joining " + new_user.title() + "!")

