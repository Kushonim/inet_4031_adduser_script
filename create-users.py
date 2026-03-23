#!/usr/bin/python3

# INET4031
# Austin Lee
# Date Created: 3/23/2026
# Date Last Modified: 3/23/2026

import os      # Used to execute system-level Linux commands
import re      # Used for pattern matching (regular expressions)
import sys     # Used to read input from standard input (stdin)

def main():
    # Loop through each line from the input file
    for line in sys.stdin:
        # Skip commented lines or lines that don't have exactly 5 fields
        match = re.match("^#", line)
        fields = line.strip().split(':')
        if match or len(fields) != 5:
            continue

        # Extract user info from fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split groups list for later assignment
        groups = fields[4].split(',')

        # Print commands instead of executing for dry run
        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        print(cmd)

        print(f"==> Setting the password for {username}...")
        cmd = f"/bin/echo -ne '{password}\\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
        print(cmd)

    for group in groups:
        if group != '-':  # Only assign if a group is listed
            print(f"==> Assigning {username} to the {group} group...")
            cmd = f"/usr/sbin/adduser {username} {group}"
            print(cmd)

if __name__ == '__main__':
    main()
