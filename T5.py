# Tamrin
library = {}


def add_book():
    x = str(input("do you want to start ? (y / n) :"))
    while x == "y" or x == "Y":
        category = str(input("please import category of book : "))
        y = input(str("do you want to add book for this category ? "))
        while y == "y" or y == "Y":
            if category not in library:
                book_name = str(input("please enter name of book : "))
                book_list = []
                book_list.append(book_name)
                library[category] = book_list
                book_list = []
            elif category in library:
                book_name = str(input("please enter name of book : "))
                library[category].append(book_name)
            y = input(str("do you want to add book for this category ? "))
        x = str(input("do you want to contineu ? (y / n) "))
    print(library)


def show(cat):
    c = 0
    for i in library:
        if i == cat:
            c = 1
            print(library[cat])
    if c == 0:
        print("not found for this category")


def search(book, cate):
    c = 0
    for i in library:
        if i == cate:
            if book in library[i]:
                c = 1
                return True
        if c == 0:
            return False


s = str(input("do you want to start the program ? (y / n) "))
while s == "y" or s == "Y":
    e = int(input("""
1 for add books
2 for show books
3 for search books
your input is : """))
    if e == 1:
        add_book()
    if e == 2:
        cat = input("please enter the category : ")
        show(cat)
    if e == 3:
        book = input("enter name of book : ")
        cate = input("enter category of book : ")
        if search(book, cate):
            print("found")
        elif search(book, cate) == False:
            print("not found")
