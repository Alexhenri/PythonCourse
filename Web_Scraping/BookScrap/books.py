'''
This is the Book class book.

Every book has:
    rank - Number of Stars (1 ... 5)
    title
    image
    price
    available - Its available? ( True or False)
'''


class BookToScrap():

    def __init__(self, title, image, price, rank):
        self.title = title
        self.image = image
        self.price = price
        self.rank = rank

    def __str__(self):
        return ("{}".format(self.title))

    def show_books_info(self):
        print('Title: {}\nImage: {}\nPrice: {}\nRank: {}\nAvailable:{}'.format(self.title, self.image, self.price,
                                                                               self.rank))
