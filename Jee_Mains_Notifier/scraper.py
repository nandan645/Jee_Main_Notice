import requests
from bs4 import BeautifulSoup

url = "https://jeemain.nta.nic.in/"

result = requests.get(url)
htmlcontent = result.content

soup = BeautifulSoup(htmlcontent, 'html.parser')

notice_box = soup.find('div', class_="vc_tta-panel-body").find('div', class_="gen-list no-border no-bg padding-20 border-radius-medium default-list").find_all('a')[:3]

print(".")
print()
print("--------------------------")
print("JEE MAINS NOTICE")
print("--------------------------")

for notice in notice_box:
    notices=notice.get_text()
    links=notice.get('href')

    print()
    print(':- ',notices," - ",links)
