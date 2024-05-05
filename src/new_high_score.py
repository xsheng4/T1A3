def read_high_score():
    try:
        with open("high_score.txt", "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0
    return high_score

def update_high_score(score):
    high_score = read_high_score()
    if score > high_score:
        with open("high_score.txt", "w") as file:
            file.write(str(score))
        print("Congratulations! New high score recorded.")
        high_score = read_high_score()
        print("High Score:", high_score)
    else:
        print("Your score is not higher than the current high score.")

def erase_high_score():
    try:
        with open("high_score.txt", "w") as file:
            file.write("0")
        print("High score erased.")
    except Exception as e:
        print(f"Error erasing high score: {e}")

def main():
    option = input("Enter 'N' to enter a new high score, 'E' to erase the high score, or 'Q' to quit: ").upper()
    
    if option == "N":
        current_score = int(input("Enter your score: "))
        update_high_score(current_score)
    elif option == "E":
        erase_high_score()
    elif option == "Q":
        print("Exiting program.")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()