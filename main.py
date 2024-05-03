import subprocess

def show_menu():
    print('Main Menu')
    print('1. Start Game')
    print('2. Open Dictionary')
    print('3. Exit')

def main():
    while True:
        show_menu()
        choice = input('Enter your choice (1-3): ')
        if choice == '1':
            subprocess.run(['python3', 'word.py'])
        elif choice == '2':
            subprocess.run(['python3', 'dictionary.py'])
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()