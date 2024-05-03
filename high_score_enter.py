import os
import subprocess

answer = input("Do you want to add the new high score? (yes/no): ").lower()

if answer == "yes":
        subprocess.run(['python3', 'new_high_score.py'])
elif answer == "no":
    subprocess.run(['python3', 'high_score.py'])