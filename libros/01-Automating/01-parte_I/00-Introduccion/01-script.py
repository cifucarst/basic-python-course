password_file = open("secret_password_file.txt")
secret_password = password_file.read()
print("Enter your password")
type_password = input()
if type_password == secret_password:
    print("Access granted")
    if type_password == '12345':
        print('That password is one that an idiot puts on their luggage.')
    else:
        print('Acces denied')