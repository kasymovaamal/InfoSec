# Lab 5: User Management in Linux

Performed inside a Docker Ubuntu container (`docker run -it --name lab5 ubuntu bash`).

## Creating a user
- Installed `adduser` package: `apt install -y adduser`
- Created user: `adduser user1`
- Verified in `/etc/passwd`: `user1:x:1001:1001:,,,:/home/user1:/bin/bash`

## Login and verification
- Logged in: `su - user1`
- Verified: `whoami` → `user1`

## Changing personal info
- Ran `chfn`, set Room Number, Work Phone, Home Phone
- Verified updated line in `/etc/passwd`:
  `user1:x:1001:1001:,1,0700143132,0700678956:/home/user1:/bin/bash`

## Deleting the user
- Killed session: `pkill -KILL -u user1`
- Installed `perl` (required for `--remove-home`): `apt install -y perl`
- Deleted user: `deluser --remove-home user1`
- Verified `user1` no longer in `/etc/passwd`

## Task: Groups
- Discovered existing groups: `cat /etc/group`
- Created new group: `groupadd devteam`
- Assigned user2 to the group: `usermod -g devteam user2`
- Verified membership: `groups user2` → `user2 : devteam users`
