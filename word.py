import random
import subprocess

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

    answer = input("Do you want to open the dictionary? (yes/no): ").lower()
    
    if answer == "yes":
        subprocess.run(['python3', 'dictionary.py'])
    elif answer == "no":
        answer2 = input("Is there a new high score? (yes/no): ").lower()
        if answer2 == "yes":
            subprocess.run(['python3', 'high_score_enter.py'])
        elif answer2 == "no":
            subprocess.run(['python3', 'main.py'])
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")   

if __name__ == "__main__":
    main()
