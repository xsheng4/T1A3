import os

# Function to read the high score from a file
def read_high_score():
    try:
        with open("high_score.txt", "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0
    return high_score

    # Display the high score
high_score = read_high_score()
print("High Score:", high_score)