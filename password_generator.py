import string
import secrets

def CryptPasswordGenerator(PasswdLength :int):
    if PasswdLength < 8:
        print("\033[31mError! Minimum password length is 8 characters.\033[0m")
        exit(-1)
    elif PasswdLength > 127:
        print("\033[31mError! Maximum password length is 127 characters.\033[0m") 
        exit(-1)

    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = """!@#$%^&*()_+-=[]{}|;:,.<>?~/"""

    all_characters = lower_case + upper_case + digits + symbols

    password_tiles = [
        secrets.choice(lower_case),
        secrets.choice(upper_case),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]
    remaining_length = PasswdLength - 4

    for _ in range(remaining_length):
        password_tiles.append(secrets.choice(all_characters))

    secure_shuffler = secrets.SystemRandom()
    secure_shuffler.shuffle(password_tiles)

    return "".join(password_tiles)