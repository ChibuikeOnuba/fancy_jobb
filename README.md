# Daily Number Incrementer

A Python script that automatically increments a number in a text file, commits the change to Git, and schedules a task to run the script at a new random time daily. Perfect for maintaining a daily commit streak or tracking sequential values with a dynamic schedule.

## Setup

1. Clone this repository:

```bash
git clone https://github.com/ChibuikeOnuba/fancy_jobb.git
cd fancy_jobb
```

2. Run the script manually for the first time to verify it works and to create a .bat file:

```bash
python update_number.py
```

To confirm the script successfully ran, a .bat file named `update_number_tasks.bat` is created.

Run the .bat file to create a schedule for the scripts to run automatically

```bash
update_number_tasks.bat
```

## Usage

The script will increment the number in `number.txt` and commit the change to git n times a day. n is a random number between 0 and 10. 

You can modify the script to increment by any value or use a different file to store the number.

By running this you will be able get a fancy streak on your github profile and get a job.

![How to get a job](get_a_job.jpg)
