import re

email_addresses = [
    "alice@example.com",
    "bob@example.com",
    "charlie@example.com",
    "dave@example.com",
    "eve@xmple.com",
    "frakexample.com",
    "grace@example.com",
    "hannahexamplecom",
    "ivan@example.com",
    "@@@julia@example.com"
]

def match_valid(email):
    return re.search(r'^[^@][A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z0-9]+', email) or None

for email in email_addresses:
    if match_valid(email):
        print(email)