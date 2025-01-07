#!/usr/bin/env python3
import os
import random
import subprocess
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def read_number():
    with open('number.txt', 'r') as f:
        return int(f.read().strip())

def write_number(num):
    with open('number.txt', 'w') as f:
        f.write(str(num))

def git_commit():
    subprocess.run(['git', 'add', 'number.txt'])
    date = datetime.now().strftime('%Y-%m-%d')
    commit_message = f"Update number: {date}"
    subprocess.run(['git', 'commit', '-m', commit_message])

def git_push():
    result = subprocess.run(['git', 'push'], capture_output=True, text=True)
    if result.returncode == 0:
        print("Changes pushed to GitHub successfully.")
    else:
        print("Error pushing to GitHub:")
        print(result.stderr)

def update_scheduler_with_random_times():
    # Generate random times for the day
    num_times = random.randint(2, 10)
    times = set()

    while len(times) < num_times:
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        times.add((hour, minute))

    # Path to the batch file
    bat_file_path = os.path.join(script_dir, "update_number_tasks.bat")

    # Write commands to the batch file
    with open(bat_file_path, "w") as bat_file:
        for hour, minute in sorted(times):
            time_string = f"{hour:02d}:{minute:02d}"
            command = (
                f'schtasks /create /tn "UpdateNumber_{hour}_{minute}" '
                f'/tr "{os.path.join(script_dir, "update_number.py")}" /sc ONCE /st {time_string}\n'
            )
            bat_file.write(command)

    print(f"Task Scheduler commands written to {bat_file_path}. Run this file to schedule tasks.")

def main():
    try:
        current_number = read_number()
        new_number = current_number + 1
        write_number(new_number)

        git_commit()
        git_push()

        update_scheduler_with_random_times()

    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()