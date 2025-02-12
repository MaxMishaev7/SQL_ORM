import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:hecQWk1974Gmr@localhost:5432/test'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)


def get_shops(session, publisher_nameid):
    result = None
    # with Session(bind=engine) as session:
    q = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Shop). \
        join(Stock). \
        join(Book). \
        join(Publisher). \
        join(Sale)

    if publisher_nameid.isdigit():
        publisher_digit = int(publisher_nameid)
        print(type(publisher_digit), publisher_digit)
        result = q.filter(Publisher.id == publisher_digit).all()
        print(result)


with Session(bind=engine) as session:
    publisher = Publisher()
    publishers = [
        ('Астрель-СПб',),  # 1
        ('Эксмо',),  # 2
        ('АСТ',),  # 3
        ('Манн, Иванов и Фарбер (МИФ)',),  # 4
        ('Азбука-Аттикус',)  # 5
    ]

    publishers_dicts = [{'name': name[0]} for name in publishers]
    print(publishers_dicts)

    session.bulk_insert_mappings(publisher, publishers_dicts)
    for val in session.query(Publisher).all():
        print(val)

    book = Book()
    books = [
        ('Убийство в заброшенном поместье', 2),  # 1
        ('Ключ к убийству', 2),  # 2
        ('Огненный воздух', 2),  # 3
        ('Леонардо да Винчи: гений на все времена', 1),  # 4
        ('Гордость и предубеждение', 1),  # 5
        ('Голодная луна', 1),  # 6
        ('Капитанская дочка', 1),  # 7
        ('Смелость быть счастливым', 3),  # 8
        ('Ленин и мы', 3),  # 9
        ('Простое рисование на пленэре', 4),  # 10
        ('История библиотек России', 4),  # 11
        ('Древние цивилизации. Детская энциклопедия', 4),  # 12
        ('Иммунитет к выгоранию', 4),  # 13
        ('Интерстеллар. Наука за кадром', 4),  # 14
        ('Два капитана', 5),  # 15
        ('Прокляты и убиты', 5),  # 16
        ('Жизнь и судьба', 5),  # 17
        ('Семнадцать мгновений весны', 5),  # 18
        ('Бесы', 5)  # 19
    ]

    books_dicts = [{'title': title, 'id_publisher': id_publisher} for title, id_publisher in books]
    print(books_dicts)
    session.bulk_insert_mappings(book, books_dicts)
    for val in session.query(Book).all():
        print(val)

    shop = Shop()
    shops = [
        ('X`libris',),  # 1
        ('Лабиринт',),  # 2
        ('Циолковский',),  # 3
        ('Гиперион',),  # 4
        ('Чук и Гик',),  # 5
        ('Фаланстер',),  # 6
        ('Самокат',)  # 7
    ]

    shops_dicts = [{'name': name[0]} for name in shops]
    print(shops_dicts)
    session.bulk_insert_mappings(shop, shops_dicts)
    for val in session.query(Shop).all():
        print(val)

    stock = Stock()
    stocks = [
        (1, 1, 50),  # 1
        (10, 6, 100),  # 2
        (2, 2, 70),  # 3
        (15, 7, 25),  # 4
        (19, 6, 40),  # 5
        (17, 6, 30),  # 6
        (17, 7, 35),  # 7
        (19, 2, 60),  # 8
        (13, 7, 50),  # 9
        (14, 3, 20),  # 10
        (18, 4, 30),  # 11
        (2, 4, 30),  # 12
        (3, 5, 40),  # 13
        (4, 6, 50),  # 14
        (5, 1, 100),  # 15
        (6, 1, 100),  # 16
        (7, 6, 33),  # 17
        (9, 3, 20),  # 18
        (10, 3, 55),  # 19
        (12, 5, 45),  # 20
        (13, 4, 24),  # 21
        (11, 7, 40),  # 22
        (8, 1, 100),  # 23
        (5, 6, 50),  # 24
        (3, 7, 38),  # 25
        (16, 4, 22)  # 26
    ]

    stocks_dicts = [{'id_book': id_book, 'id_shop': id_shop, 'count': count} for id_book, id_shop, count in stocks]
    print(stocks_dicts)
    session.bulk_insert_mappings(stock, stocks_dicts)
    for val in session.query(Stock).all():
        print(val)

    sale = Sale()
    sales = [
        (155, '2024-12-11', 17, 20),
        (55, '2024-11-18', 23, 10),
        (467, '2024-10-02', 26, 100),
        (890, '2025-01-10', 8, 200),
        (3000, '2024-07-09', 1, 18),
        (1200, '2024-07-10', 15, 300),
        (500, '2024-08-12', 2, 800),
        (2300, '2024-09-01', 8, 200),
        (1500, '2024-07-02', 9, 124),
        (800, '2024-07-02', 10, 25),
        (1800, '2024-08-08', 12, 76),
        (2800, '2025-02-01', 11, 90),
        (1150, '2025-01-07', 20, 234),
        (675, '2025-01-02', 24, 141),
        (900, '2025-01-06', 4, 200),
        (267, '2025-01-05', 2, 245),
        (450, '2025-01-03', 1, 345),
        (580, '2024-11-02', 26, 170),
        (600, '2024-10-29', 13, 200)
    ]

    sales_dicts = [{'price': price, 'date_sale': date_sale, 'id_stock': id_stock, 'count': count}
                   for price, date_sale, id_stock, count in sales]
    print(sales_dicts)
    session.bulk_insert_mappings(sale, sales_dicts)
    for val in session.query(Sale).all():
        print(val)

    publisher_name = input("Введите: ")
    get_shops(session, publisher_name)