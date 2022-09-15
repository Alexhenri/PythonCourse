import bs4
import requests


authors = set()
qtoscrape_url = 'http://quotes.toscrape.com/page/{}/'
i = 0
while True:
    i += 1
    quotes_to_scrape = requests.get(qtoscrape_url.format(i))
    soup_quotes_to_scrape = bs4.BeautifulSoup(quotes_to_scrape.text, "lxml")
        
    quotes_item = soup_quotes_to_scrape.select('.quote')

    if len(quotes_item) == 0:
        break

    for quote_item in quotes_item:
        author = quote_item.find('small')
        authors.add(author.getText()) 

print(authors)
print('\n')
print(len(authors))
