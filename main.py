import subprocess

# External packages
from colored import Fore, Back, Style

def show_menu():
    print(f"{Fore.yellow}{Back.blue}Main Menu")
    print('1. Start Game')
    print('2. Open Dictionary')
    print('3. High Scores')
    print('4. Exit')

def main():
    while True:
        show_menu()
        choice = input('Enter your choice (1-4): ')
        if choice == '1':
            subprocess.run(['python3', 'word.py'])
        elif choice == '2':
            subprocess.run(['python3', 'dictionary.py'])
        elif choice == '3':
            subprocess.run(['python3', 'high_score.py'])
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()