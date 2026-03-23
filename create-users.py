#!/usr/bin/python3

# INET4031
# Austin Lee
# Date Created: 3/23/2026
# Date Last Modified: 3/23/2026

import os      # Used to execute system-level Linux commands
import re      # Used for pattern matching (regular expressions)
import sys     # Used to read input from standard input (stdin)

def main():
    for line in sys.stdin:

        # Skip lines that start with "#" (used for comments in the input file)
        match = re.match("^#", line)

        # Remove whitespace/newlines and split the line into fields using ":" as a delimiter
        fields = line.strip().split(':')

        # Ignore invalid lines:
        # - If the line is a comment
        # - If it does not contain exactly 5 required fields
        # This ensures only properly formatted user entries are processed
        if match or len(fields) != 5:
            continue

        # Extract user account information from the input fields
        username = fields[0]
        password = fields[1]

        # Format user information for the GECOS field (Full Name and additional info)
        # This is stored in /etc/passwd and typically contains user details
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split group names into a list (comma-separated in input file)
        groups = fields[4].split(',')

        # Inform the user that account creation is starting
        print("==> Creating account for %s..." % (username))

        # Build the Linux command to create a user with no password initially
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # Uncomment to actually execute user creation (dry run leaves this commented)
        # print(cmd)
        # os.system(cmd)

        # Inform the user that password setup is starting
        print("==> Setting the password for %s..." % (username))

        # Build command to set the user's password automatically using echo + passwd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # Uncomment to actually execute password assignment
        # print(cmd)
        # os.system(cmd)

        # Loop through each group and assign user to valid groups
        for group in groups:
            # Skip "-" which indicates no group assignment
            # If valid group, user is added to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                # Uncomment to execute group assignment
                # print(cmd)
                # os.system(cmd)

if __name__ == '__main__':
    main()
