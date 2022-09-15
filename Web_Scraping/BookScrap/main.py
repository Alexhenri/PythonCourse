'''

This is the main.py of Book To Scrap project.
A project that helps me to study web scraping in Python.

'''

import requests
import bs4
import re
from books import BookToScrap

import soupsieve


def get_the_number_of_pages():

    site_info = requests.get('https://books.toscrape.com/')
    site_soup = bs4.BeautifulSoup(site_info.text, 'lxml')

    page_counter = site_soup.select('.current')
    page_counter_text = page_counter[0].getText()

    numbers = re.findall(r'\d+', page_counter_text)
    number = int(numbers[-1])

    return number

def get_book_content_page(n):
    base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
    site_info = requests.get(base_url.format(n))
    site_soup = bs4.BeautifulSoup(site_info.text, 'lxml')
    products = site_soup.select('.product_pod')

    return products


def get_book_info(list_books_soup):

    inner_list_books = []

    # For every book:
    for book_soup in list_books_soup:
        # Getting book name
        name = book_soup.select('a')[1]['title']

        # Getting book image
        image = 'https://books.toscrape.com/' + book_soup.select('.thumbnail')[0]['src']

        # Getting Price
        price = book_soup.select('.price_color')[0].getText()

        # Getting Rank
        if book_soup.select('.star-rating.One'):
            rank = 1
        elif book_soup.select('.star-rating.Two'):
            rank = 2
        elif book_soup.select('.star-rating.Three'):
            rank = 3
        elif book_soup.select('.star-rating.Four'):
            rank = 4
        elif book_soup.select('.star-rating.Five'):
            rank = 5
        else:
            rank = 0

        inner_book = BookToScrap(title=name, image=image, price=price, rank=rank)
        inner_list_books.append(inner_book)

    return inner_list_books


if __name__ == '__main__':

    list_books = []
    num_pages = get_the_number_of_pages()

    for n in range(1, num_pages):
        books_soup = get_book_content_page(n)
        books = get_book_info(books_soup)
        list_books += books

    for book in list_books:
        if book.rank == 2:
            print(book)

