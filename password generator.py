
import random
import string

def generate_password(length):
    if length < 5:
        raise ValueError("Password length should be at least 5  characters")


    characters = string.ascii_letters + string.digits + string.punctuation

    
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    
    password += random.choices(characters, k=length - 5)

    
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
