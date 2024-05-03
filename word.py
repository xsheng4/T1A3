import random

def generate_letter(choice):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    if choice.lower() == 'vowel':
        return random.choice(vowels)
    elif choice.lower() == 'consonant':
        return random.choice(consonants)
    else:
        return 'Invalid choice. Please choose either "vowel" or "consonant".'

def main():
    for _ in range(9):  # Loop 9 times
        choice = input("Choose between 'vowel' or 'consonant': ")
        letter = generate_letter(choice)
        print(f"Random letter: {letter}")

if __name__ == "__main__":
    main()
