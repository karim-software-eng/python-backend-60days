attempts = 3
correct_password = "secret123"

while attempts > 0:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access Granted")
        break
    
    attempts -= 1
    if attempts > 0:
        print(f"Wrong password. You have {attempts} attempts left.")
    else:
        print("Account Locked")




















