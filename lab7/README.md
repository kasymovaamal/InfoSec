# Lab 7: Crontab in Linux

## Basic cron example
- Created `write_line.sh` to append a timestamped line to `file.txt`
- Scheduled via `crontab -e`: `* * * * * /Users/amal/unix-lab/lab7/write_line.sh`
- Verified with `crontab -l` and `cat file.txt` — confirmed new timestamped lines appeared automatically every minute

## Task: Cron job running a Python script to send email
- Created `notify.py` using `smtplib` to send an automated status notification email via Gmail SMTP (using a Gmail App Password)
- Tested manually: `python3 notify.py` → "Email sent successfully!"
- Scheduled via `crontab -e`: `*/2 * * * * /usr/bin/python3 /Users/amal/unix-lab/lab7/notify.py`
- Verified with `crontab -l`, then confirmed the email arrived automatically in the inbox (see `screenshots/`)
- Removed the schedule afterward to stop recurring emails: `crontab -e` → deleted the line

## Notes
On macOS, the first `crontab -e` triggered a system permission prompt ("Terminal would like to administer your computer") under Privacy & Security — this needed to be allowed for cron to run scheduled tasks.
