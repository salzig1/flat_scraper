import requests
from bs4 import BeautifulSoup

from whatsapp import send_message


page = 1
while True:
    url = (
        f"https://www.immowelt.de/liste/muenchen/wohnungen/mieten?"
        f"ami=30&d=true&pma=900&r=10&sd=DESC&sf=RELEVANCE&sp={page}"
    )

    # get html response
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # estate list
    data = soup.find_all("div", class_="SearchList-22b2e")
    flats = data[0]

    # no more flats on this page
    if (len(flats) == 0):
        break

    # read in already checked ids
    old_ids = []
    file = open("estate_ids.txt", "r+")
    for line in file:
        old_ids.append(line.strip())
        
    
    for flat in flats:
        links = flat.find_all("a", href=True)
        for link in links:
            id = link["id"]
            if id not in old_ids:
                # send message
                send_message(link["href"])
                file.write(f"{str(id)}\n")
                pass
        
    page += 1

