import os

# Function to read the high score from a file
def read_high_score():
    try:
        with open("high_score.txt", "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0
    return high_score

# Function to update the high score
def update_high_score(score):
    high_score = read_high_score()
    if score > high_score:
        with open("high_score.txt", "w") as file:
            file.write(str(score))

# Example usage
def main():
    # Simulating a game where the player achieves a score
    # player_score = 1000
    # update_high_score(player_score)

    # Display the high score
    high_score = read_high_score()
    print("High Score:", high_score)

if __name__ == "__main__":
    main()
