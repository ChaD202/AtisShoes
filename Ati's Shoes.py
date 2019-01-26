import sqlite3

connection = sqlite3.connect("atiDB.db")

cursor = connection.cursor()

data = cursor.execute("SELECT * FROM Stock")

Customers = list(data)

# fields = id, Brand, Shoename, Size, Price

# record class


class Record:
    def __init__(self, i, brand, shoename, size, price):
        self.id = i
        self.brand = brand
        self.shoename = shoename
        self.size = size
        self.price = price

# functions


def find_size(size):
    global Customers

    size_list = []

    for r in Customers:
        if r[3] == int(size):
            size_list.append(r)

    print("\n >> {length} SEARCH RESULTS".format(length=len(size_list)))

    for r in size_list:
        print(" >> ID: " + str(r[0]))
        print(" >> Brand: " + str(r[1]))
        print(" >> Shoename: " + str(r[2]))
        print(" >> Size: " + str(r[3]))
        print(" >> Price: " + str(r[4]) + "\n")


def find_brand(brand):
    global Customers

    size_list = []

    for r in Customers:
        if r[1] == brand:
            size_list.append(r)

    print("\n >> {length} SEARCH RESULTS".format(length=len(size_list)))

    for r in size_list:
        print(" >> ID: " + str(r[0]))
        print(" >> Brand: " + str(r[1]))
        print(" >> Shoename: " + str(r[2]))
        print(" >> Size: " + str(r[3]))
        print(" >> Price: " + str(r[4]) + "\n")


def search(field, t):
    global Customers

    dc = True

    field_def = {"id": 0, "ID": 0,
                 "brand": 1, "Brand": 1,
                 "shoename": 2, "Shoename": 2,
                 "size": 3, "Size": 3,
                 "price": 4, "Price": 4}

    size_list = []

    for r in Customers:

        try:
            if r[field_def[field]] == t and field_def[field] not in [0, 3, 4]:
                size_list.append(r)

            if field_def[field] in [0, 3, 4] and r[field_def[field]] == int(t):
                size_list.append(r)

        except KeyError:
            print("\n >> INVALID")
            dc = False
            break

    if dc:
        print("\n >> {length} SEARCH RESULTS".format(length=len(size_list)))

        for r in size_list:
            print("\n >> ID: " + str(r[0]))
            print(" >> Brand: " + str(r[1]))
            print(" >> Shoename: " + str(r[2]))
            print(" >> Size: " + str(r[3]))
            print(" >> Price: " + str(r[4]) + "\n")


def remove(i):
    global Customers

    d = 0

    for r in Customers:
        if r[0] == i:
            cursor.execute("DELETE FROM Stock WHERE id = {ID}".format(ID=i))
            connection.commit()
            d += 1

            print("\n >> Stock with ID {si} has been removed.".format(si=i))

            print("\n >> Details: ")

            print("\n >> ID: " + str(r[0]))
            print(" >> Brand: " + str(r[1]))
            print(" >> Shoename: " + str(r[2]))
            print(" >> Size: " + str(r[3]))
            print(" >> Price: " + str(r[4]) + "\n")

    if d == 0:
        print("\n >> No such stock with ID {si}".format(si=i))


def menu():
    print("\n >> DATABASE OPTIONS <<")
    print(" >> 1: Search for stock.")
    print(" >> 2: Search for stock based on shoe size.")
    print(" >> 3: Search for stock based on brand.")
    print(" >> 4: Remove stock.")

    opt = str(input("\n >> "))

    if opt == "1":
        f = input("\n >> Field name: ")
        q = input(" >> Query: ")

        search(f, q)

    if opt == "2":
        s = input("\n >> Enter size: ")
        find_size(s)

    if opt == "3":
        b = input("\n >> Enter brand: ")
        find_brand(b)

    if opt == "4":
        si = input("\n >> Enter stock ID: ")

        try:
            remove(int(si))

        except ValueError:
            print(" >> INVALID")

    if opt not in ["1", "2", "3", "4"]:
        print("\n >> INVALID")


while True:
    menu()
