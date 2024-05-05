import os
import subprocess

option = input("Do you want to add the new high score? (yes/no): ").lower()

if option == "yes":
        subprocess.run(['python3', 'new_high_score.py'])
elif option == "no":
        subprocess.run(['python3', 'high_score.py'])