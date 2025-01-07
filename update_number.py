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

def update_cron_with_random_times():
    # Generate random times for the day
    num_times = random.randint(2, 10)
    times = set()
    
    while len(times) < num_times:
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        times.add((hour, minute))
    
    # Define cron jobs
    cron_file = "/tmp/current_cron"
    os.system(f"crontab -l > {cron_file} 2>/dev/null || true")
    
    with open(cron_file, "r") as file:
        lines = file.readlines()
    
    with open(cron_file, "w") as file:
        for line in lines:
            if "update_number.py" not in line:
                file.write(line)
        
        for hour, minute in sorted(times):
            cron_command = f"{minute} {hour} * * * cd {script_dir} && python3 {os.path.join(script_dir, 'update_number.py')}\n"
            file.write(cron_command)
    
    os.system(f"crontab {cron_file}")
    os.remove(cron_file)
    print(f"Cron jobs updated to run {num_times} times today at the following times: {sorted(times)}")

def main():
    try:
        current_number = read_number()
        new_number = current_number + 1
        write_number(new_number)

        git_commit()
        git_push()

        update_cron_with_random_times()

    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()