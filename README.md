# INET 4031 – Interactive User Management Automation

**Author**: Austin Lee

**Date Created**: 3/23/2026

**Last Modified**: 3/23/2026

## Program Description

This repository contains a Python script that automates the creation of users and groups on an Ubuntu system. The goal is to reduce the time and errors associated with manually creating multiple user accounts, assigning passwords, and adding users to groups.

The script processes a colon-delimited input file (create-users.input) that contains user information, including username, password, first and last name, and group membership. It is representative of typical configuration scripts used by system administrators.

## Files in this Repository
create-users.py – Original script for adding users and groups.
create-user2.py – Updated script with interactive dry-run option.
create-users.input – Input file containing the list of users and their details.
README.md – Documentation for this repository.
## How to Use the Script

1. Navigate to the script directory:
- cd ~/inet_4031_adduser_script

2. Make the script executable (if not already):
- chmod +x create-user2.py

3. Run the script:
- sudo ./create-user2.py

4. Dry-run or actual execution - You will be prompted:
- Run in dry-run mode? (Y/N):
- Type Y → Script prints the commands it would run without making any changes.
- Type N → Script executes commands and creates users/groups on the system.

## Example Dry-Run Output
==> Creating account for user04...
/usr/sbin/adduser --disabled-password --gecos 'First04 Last04,,,' user04
==> Setting the password for user04...
/bin/echo -ne 'pass04\npass04' | /usr/bin/sudo /usr/bin/passwd user04
==> Assigning user04 to the group01 group...
/usr/sbin/adduser user04 group01
==> Creating account for user05...
/usr/sbin/adduser --disabled-password --gecos 'First05 Last05,,,' user05
==> Setting the password for user05...
/bin/echo -ne 'pass05\npass05' | /usr/bin/sudo /usr/bin/passwd user05
==> Assigning user05 to the group02 group...
/usr/sbin/adduser user05 group02

- This output shows the commands the script would run without modifying the system.

## How the Code Works:
- Prompts the user for dry-run mode.
- Reads each line from the create-users.input file.
- Skips commented or invalid lines.
- Extracts user information: username, password, first/last name, and groups.
- Prints or executes the commands to:
- Create users
- Set passwords
- Assign to groups
- Supports multiple groups per user and safely handles errors.

## Notes
- Running the script without sudo will fail to add users/groups or assign passwords.
- The dry-run feature allows safe testing before making system changes.
- The script handles invalid input gracefully and skips lines with missing fields.
