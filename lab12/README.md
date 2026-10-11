# Lab 12: Brute-Force Attacks

Performed inside a Docker Ubuntu container against a locally-hosted FastAPI test server (`docker run -it --name lab12 ubuntu bash`), never against any real or remote system.

## Setup: vulnerable test server
- Created a FastAPI app (`main.py`) with a `/login` endpoint checking a hardcoded username/password (`admin` / `12345admin`)
- Ran it locally: `fastapi dev main.py --host 0.0.0.0`
- Verified manually with curl

## Hydra brute-force attack
- Installed Hydra: `apt install -y hydra`
- Created `usernames.txt` and `passwords.txt` wordlists
- Ran: `hydra -f -I -V -L usernames.txt -P passwords.txt -s 8000 localhost http-form-post "/login:username=^USER^&password=^PASS^:F=Invalid"`
- Hydra successfully found the valid credentials:

[8000][http-post-form] host: localhost login: admin password: 12345admin
[STATUS] attack finished for localhost (valid pair found)
1 of 1 target successfully completed, 1 valid password found


## Task: OSINT-based password profiling (CUPP)
- Installed CUPP: `git clone https://github.com/Mebus/cupp.git`
- Ran `python3 cupp.py -i` with sample fictional personal details (name, surname, nickname, birthdate)
- CUPP generated a wordlist of 14,776 candidate passwords combining those details in common patterns
- Ran Hydra against the test server using the CUPP-generated wordlist: `hydra -f -I -V -L usernames.txt -P cupp/john.txt -s 8000 localhost http-form-post "/login:username=^USER^&password=^PASS^:F=Invalid"`
- Demonstrated the attack running through thousands of personalized guesses (stopped manually after confirming it was working correctly)

## Findings
- Hydra automates testing many username/password combinations against a live login endpoint, using the `F=` flag to distinguish failed vs. successful attempts.
- OSINT-based tools like CUPP show why reusing names, birthdates, or other personal details in passwords is risky — knowing basic facts about a target lets an attacker generate a highly targeted wordlist (thousands of likely variants) rather than relying on pure random brute-forcing.
- All testing was performed against a locally-hosted, self-created server — no real-world system or account was targeted.
