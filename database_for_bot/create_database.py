import sqlite3
import datetime

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()

    query_tab_persons = """ CREATE TABLE IF NOT EXISTS persons(
                id_person INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
                surname TEXT,
                name TEXT,
                patronymic TEXT,
                rate_id INTEGER NOT NULL,
                date_id INTEGER NOT NULL,
                phone_id INTEGER NOT NULL,
                mail_id INTEGER NOT NULL,
                FOREIGN KEY (rate_id) REFERENCES rates (id_rate),
                FOREIGN KEY (date_id) REFERENCES dates (id_date),
                FOREIGN KEY (phone_id) REFERENCES phone_persons (id_phone),
                FOREIGN KEY (mail_id) REFERENCES mail_persons (id_mail)) """

    query_tab_rates = """ CREATE TABLE IF NOT EXISTS rates(
                id_rate INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
                rate TEXT) """

    query_tab_dates = """ CREATE TABLE IF NOT EXISTS dates(
                id_date INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                open_date INTEGER,
                person_id INTEGER NOT NULL, 
                FOREIGN KEY (person_id) REFERENCES persons (id_person)) """

    query_tab_phone_persons = """ CREATE TABLE IF NOT EXISTS phone_persons(
                id_phone INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                phone_number INTEGER,
                person_id INTEGER NOT NULL, 
                FOREIGN KEY (person_id) REFERENCES persons (id_person)) """


    query_tab_mail_persons = """ CREATE TABLE IF NOT EXISTS mail_persons(
                id_mail INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                mail TEXT,
                person_id INTEGER NOT NULL, 
                FOREIGN KEY (person_id) REFERENCES persons (id_person)) """

    query_tab_price_rates = """ CREATE TABLE IF NOT EXISTS price_rates(
                id_price INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                price INTEGER,
                rate_id INTEGER NOT NULL,
                FOREIGN KEY (rate_id) REFERENCES rates (id_rate)) """
    

    cursor.execute(query_tab_persons)
    cursor.execute(query_tab_rates)
    cursor.execute(query_tab_dates)
    cursor.execute(query_tab_phone_persons)
    cursor.execute(query_tab_mail_persons)
    cursor.execute(query_tab_price_rates)

    db.commit()


def get_timestamp(y, m, d):
    return datetime.datetime.timestamp(datetime.datetime(y, m, d))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()


insert_persons = [
    (1, 'Сидорова', 'Марина', 'Викторовна', 1, 1, 1, 1),
    (2, 'Петрова', 'Наталья', 'Петровна', 2, 2, 2, 2)
]

insert_rates = [
    (1, 'Basic'),
    (2, 'Full')
]

insert_dates = [
    (1, get_timestamp(2022, 12, 20), 1),
    (2, get_timestamp(2022, 12, 10), 2)
]


insert_phone_persons = [
    (1, 89991119898, 1),
    (2, 86661235665, 2)
]

insert_mail_person = [
    (1, 'marina@mail.ru', 1),
    (2, 'nataly@mail.ru', 2)
]

insert_price_rates = [
    (1, 5000, 1),
    (2, 6000, 2)
]

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()

    query_persons = """ INSERT INTO persons(id_person, surname,
                                            name, patronymic,
                                            rate_id, date_id,
                                            phone_id, mail_id)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?);"""

    query_rates = """ INSERT INTO rates(id_rate, rate)
        VALUES(?, ?); """

    query_dates = """ INSERT INTO dates(id_date, open_date, 
                                          person_id)
        VALUES(?, ?, ?); """

    query_phone_persons = """ INSERT INTO phone_persons(id_phone, 
                                                        phone_number,
                                                        person_id)
        VALUES(?, ?, ?); """

    query_mail_persons = """INSERT INTO mail_persons(id_mail, 
                                                     mail,
                                                     person_id)
        VALUES(?, ?, ?);"""

    query_price_rates = """INSERT INTO price_rates(id_price, 
                                                    price,
                                                    rate_id)
        VALUES(?, ?, ?);"""

    cursor.executemany(query_persons, insert_persons)
    cursor.executemany(query_rates, insert_rates)
    cursor.executemany(query_dates, insert_dates)
    cursor.executemany(query_phone_persons, insert_phone_persons)
    cursor.executemany(query_mail_persons, insert_mail_person)
    cursor.executemany(query_price_rates, insert_price_rates)

    db.commit()