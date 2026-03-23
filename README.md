# INET4031 Add Users Script and User List
## Program Description

This program automates the process of creating multiple user accounts and assigning them to groups on a Linux system. Normally, a system administrator would need to manually run commands like adduser to create each user and adduser username groupname to assign users to groups. This process becomes time-consuming and error-prone when managing many users.

This script simplifies that process by reading user information from an input file and automatically executing the necessary system commands. It ensures consistency, reduces manual effort, and speeds up user management tasks by performing all operations in a single run.

## Program User Operation

This program reads a list of users from an input file and processes each line to create user accounts and assign group memberships. The user provides the input file and runs the script, which handles the rest automatically.

After reading this section, the user should understand how to prepare the input file and execute the script. The internal logic and detailed behavior of the script are explained through comments within the code.

## Input File Format

The input file contains one user per line, with each line formatted using colon (:) delimiters. Each line includes five fields in the following order:

username:password:last_name:first_name:groups
username – the login name for the user
password – the user’s password
last_name – the user’s last name
first_name – the user’s first name
groups – a comma-separated list of groups the user should be added to

If a user should not be added to any groups, a - is used in the groups field.

If a line should be skipped, it can be commented out using a # at the beginning of the line. The script will ignore any lines marked this way.

## Command Execution

To run the script, the user must first ensure that the Python file is executable:

chmod +x create-users.py

Then the script can be executed using:

./create-users.py < create-users.input

Alternatively, the script can be run using Python directly:

sudo python3 create-users.py < create-users.input

The < symbol redirects the contents of the input file into the script as standard input.

## Dry Run

The script includes a dry-run mode that allows the user to test the script without making any actual changes to the system. In this mode, the script processes all input and displays the commands that would be executed, but does not create any users or groups.

This is useful for verifying that the input file is correctly formatted and that the script will behave as expected before running it for real.
