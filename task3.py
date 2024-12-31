import requests
from bs4 import BeautifulSoup

url = 'https://www.ibm.com/think/topics/artificial-intelligence'
resp = requests.get(url)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, 'html.parser')
    page_text = soup.get_text()
    links = [a['href']for a in soup.find_all('a', href = True)]
    images = [img['src'] for img in soup.find_all('img', src = True)]
    print("Page Text: ", page_text)
    print("\nLinks: ")
    for link in links:
        print(link)
    print("\nImages: ")
    for image in images:
        print(image)
else:
    print(f"Failed to retrieve webpage. \nStatus Code : {resp.status_code}")






