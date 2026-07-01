import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter Password Length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password = password + random.choice(characters)

print("Generated Password is:")
print(password)