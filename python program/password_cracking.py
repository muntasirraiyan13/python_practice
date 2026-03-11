user_password=int(input("Enter your four digit password:"))
count=0
for computer_choice in range(1000, 10001):
    count=count+1
    if (computer_choice == user_password):
        print("Your password is cracked!")
        print("Your password is", computer_choice)
        print("Applying loop for", count, "times")
        break
