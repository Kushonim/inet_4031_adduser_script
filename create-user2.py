#!/usr/bin/python3

# INET4031
# Austin Lee
# Date Created: 3/23/2026
# Date Last Modified: 3/23/2026

import os      # Used to execute system-level Linux commands
import re      # Used for pattern matching (regular expressions)
import sys     # Used to handle system-related operations

def main():
    # Prompt user for dry-run or real run
    dry_run = input("Run in dry-run mode? (Y/N): ").strip().upper() == 'Y'

    # Open input file directly (no stdin redirection needed)
    with open('create-users.input') as f:
        for line in f:
            # Skip comment lines or lines that don't have exactly 5 fields
            match = re.match("^#", line)
            fields = line.strip().split(':')
            if match or len(fields) != 5:
                if dry_run:
                    print(f"Skipping invalid line: {line.strip()}")
                continue

            # Extract user info from fields
            username = fields[0]
            password = fields[1]
            gecos = f"{fields[3]} {fields[2]},,,"

            # Split groups for later assignment
            groups = fields[4].split(',')

            # Dry-run: just print what would happen
            print(f"==> Creating account for {username}...")
            cmd_adduser = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
            if dry_run:
                print(cmd_adduser)
            else:
                os.system(cmd_adduser)

            print(f"==> Setting the password for {username}...")
            cmd_passwd = f"/bin/echo -ne '{password}\\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
            if dry_run:
                print(cmd_passwd)
            else:
                os.system(cmd_passwd)

            # Assign groups
            for group in groups:
                if group != '-':  # Only assign if group exists
                    print(f"==> Assigning {username} to the {group} group...")
                    cmd_group = f"/usr/sbin/adduser {username} {group}"
                    if dry_run:
                        print(cmd_group)
                    else:
                        os.system(cmd_group)

if __name__ == '__main__':
    main()
