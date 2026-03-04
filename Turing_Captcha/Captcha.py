import random
import string

def generate_captcha(length=6):
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha

print("CAPTCHA VERIFICATION")

captcha = generate_captcha()
print("CAPTCHA:", captcha)

user_input = input("Enter the CAPTCHA: ")

if user_input == captcha:
    print("Verification Successful! You are human.")
else:
    print("Verification Failed! Possible bot detected.")