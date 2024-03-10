import re

# Matching Email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
text = "Contact us at contact@describeissue.com or support@gmail.com"
emails = re.findall(pattern, text)
print(emails)

# Matching Phone numbers
pattern = r'\d{3}-\d{3}-\d{4}'
text = "Contact us at 123-456-7890 or 987-654-3210"
phones = re.findall(pattern, text)
print(phones)

# Matching URLs
pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
text = "Visit our website at https://www.describeissue.com or https://website.co.uk"
urls = re.findall(pattern, text)
print(urls)

# Matching Hastags
pattern = r'#\w+'
text = "Join the conversation! #Python #Programming"
hashtags = re.findall(pattern, text)
print(hashtags)

# Matching tags
pattern = r'<[^>]+>'
html = "<div class='content'>Hello <strong>world</strong></div>"
tags = re.findall(pattern, html)
print(tags)

# Matching IP addresses
pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
text = "Server IP: 192.168.1.1, Client IP: 10.0.0.1"
ips = re.findall(pattern, text)
print(ips)

# Matching Dates

pattern = r'\b(?:\d{1,2}[-/])?\d{1,2}[-/]\d{2,4}\b'
text = "Meeting scheduled for 12/25/2023 or 01-31-22"
dates = re.findall(pattern, text)
print(dates)
