
import sys
import requests

URLlist = [
    "https://tatu.edu.gh",
    "https://police.gov.gh",
    "https://app.tatu.edu.gh",
    "https://apply.tatu.edu.gh",
    "https://vclass.tatu.edu.gh"
]
response = requests.get(url)


for url in URLlist:
    print(response.status_code)
    print(response.text)
