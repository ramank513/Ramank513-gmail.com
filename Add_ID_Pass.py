def insert_user(name, email, phone, password):
    user = {
        "name": name,
        "email": email,
        "phone": phone,
        "password": password  
    }
    return user


# Testing
name = input("Enter your name: ")
email = input("Enter your email: ")
phone = input("Enter your phone: ")
password = input("Enter your password: ")

user_data = insert_user(name, email, phone, password)
print("User inserted successfully:", user_data)
