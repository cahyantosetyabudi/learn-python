import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'

params = {
    'q': 'Python Developer',
    'l': 'New York State',
    'vjk': '9f78e01b2c7bfd95'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

res = requests.get(url, params=params, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())