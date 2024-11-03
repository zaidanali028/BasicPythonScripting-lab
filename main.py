# 0. created a virtual environment to isolate my dependencies within just this project
# using these commands:
# $ python3 -m venv venv (for creation)
# $ source venv/bin/activate (for activation)
# $ deactivate (can optionally deactivate using this command)

# 1. importation of required libraries
import requests
import os
import shutil
from datetime import datetime as dt
from simple_chalk import chalk  # Importing chalk for colored output

# 2. cleaning up previous dir if it exists
my_name = 'ali_zaidan'

try:
    if os.path.exists(my_name):
        shutil.rmtree(my_name)  # Remove the existing directory
        print(chalk.green(f"Directory '{my_name}' has been removed successfully."))
except Exception as e:
    print(chalk.red(f"Error while removing directory '{my_name}': {e}"))

# 3. creating the new directory
download_folder = my_name
try:
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)  # Create the new directory
        print(chalk.green(f"Directory: {download_folder} created."))  # Success message in green
except Exception as e:
    print(chalk.red(f"Error while creating directory '{download_folder}': {e}"))

# 4. Defining local file path I want to store my downloaded file
try:
    local_file_path = os.path.join(download_folder, f"{download_folder}.txt")
    print(chalk.blue(f"Local file path: {local_file_path}"))  # Informational message in blue
except Exception as e:
    print(chalk.red(f"Error while defining file path: {e}"))

# 5. Defining the URL of the file I want to download
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(chalk.green("File successfully downloaded."))  # Success message in green

        with open(local_file_path, "wb") as file:
            file.write(response.content)  # Write content to the local file
            print(chalk.green("File saved successfully."))  # Success message for file save
    else:
        print(chalk.red(f"Failed to download file. Status code: {response.status_code}"))  # Error message in red
except Exception as e:
    print(chalk.red(f"Error while downloading file from URL '{url}': {e}"))

# Getting the current time for logging
now = dt.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

while True:
    # 6. Getting user input, time and writing them to a file
    try:
        user_input = input("Describe what you have learned so far in a sentence (or type 'exit', 'quit', or 'q' to quit): ")

        # Exit condition to break the loop
        if user_input.lower() in ["exit", "quit", "q"]:
            print(chalk.yellow("Exiting the program..."))  # Exit message in yellow
            break

        # Check if user_input is not None or empty
        if user_input:
            current_time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(local_file_path, "w") as file:  # Open the file to write
                file.write(user_input + "\n\n")
                file.write(f"Last modified on: {current_time}")  # Save last modified time
            print(chalk.green("File successfully modified."))  # Success message for file modification

            # Displaying the updated content of the file
            with open(local_file_path, "r") as file:
                print("\nYou Entered: ", end=' ')
                print(chalk.cyan.bold(file.read()))  # Display the file content in cyan
        else:
            print(chalk.red("No [EXPERIENCE!] provided."))  # Error message if input is empty
    except Exception as e:
        print(chalk.red(f"Error while handling user input or file modification: {e}"))
