# Lab 6: Permissions in Linux

## Viewing and changing permissions
- Created file: `touch file.txt`
- Viewed permissions: `ls -la` → `-rw-r--r--`
- Changed permissions: `chmod 754 file.txt` → `-rwxr-xr--`
- Tested permission denial: `chmod 077 file.txt` then `cat file.txt` → Permission denied
- Restored: `chmod 644 file.txt`

## Task: Changing owner and group
- Checked current owner/group: `ls -la file.txt`
- Changed group: `chgrp staff file.txt`
- Changed owner: `sudo chown root file.txt`
- Verified loss of access: `cat file.txt` / `echo "test" >> file.txt` → Permission denied
- Restored ownership: `sudo chown amal file.txt`
- Combined owner+group change: `sudo chown amal:staff file.txt`

### Findings
Changing a file's owner transfers control of the owner-level permission bits to the new user — the original creator loses owner-level access unless they're also in the file's group. This is why `chown` requires elevated privileges (`sudo`), preventing users from arbitrarily taking ownership of files they don't own.
