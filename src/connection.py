import sqlite3
import re
import logging

logging.basicConfig(filename="../sample.log", level=logging.INFO)


class Connection:
    def __init__(self):
        self.db = 'new.db'
        self.table_name = 'books_data'

    def create_table(self):
        try:
            sqlite_connection = sqlite3.connect(self.db)

            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS ''' + self.table_name + ''' (
                book_name text,
                number_of_paragraphs int,
                number_of_words int,
                number_of_letters int,
                words_with_capital_letters int,
                words_in_lowercase int
                );'''

            cursor = sqlite_connection.cursor()
            logging.info("Successfully connected to sqlite")

            cursor.execute(sqlite_create_table_query)

            sqlite_connection.commit()
            logging.info("SQLite table {} is created".format(self.table_name))

            cursor.close()

        except sqlite3.Error as error:
            logging.error("Cannot connect to sqlite", error)

        finally:
            sqlite_connection.close()
            logging.info("Connection is closed")

    def insert_table(self, model):
        try:
            sqlite_connection = sqlite3.connect(self.db)
            cursor = sqlite_connection.cursor()
            logging.info("Successfully connected to sqlite")

            columns = tuple(model.get_table())
            cursor.execute('''INSERT OR REPLACE INTO ''' + self.table_name + '''                               
                                          VALUES (?, ?, ?, ?, ?, ?);''', columns)

            sqlite_connection.commit()
            logging.info("Number of records is {}".format(str(cursor.rowcount), self.table_name))

            cursor.close()

        except sqlite3.Error as error:
            logging.error("Failed to insert records into table.", error)

        finally:
            sqlite_connection.close()
            logging.info("Connection is closed")

    def create_second_table(self, model):
        try:
            sqlite_connection = sqlite3.connect(self.db)

            second_table_name = model.get_second_table()[0]
            second_table_name = re.sub("\s+", "_", second_table_name.strip()).lower()
            columns = model.get_second_table()[1]

            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS ''' + second_table_name + ''' (
                   word text,
                   count int,
                   count_uppercase int);'''

            cursor = sqlite_connection.cursor()
            logging.info("Successfully connected to sqlite")

            cursor.execute(sqlite_create_table_query)
            sqlite_connection.commit()

            cursor.executemany('''INSERT OR REPLACE INTO ''' + second_table_name + '''                               
                                          VALUES (?, ?, ?);''', columns)
            sqlite_connection.commit()
            logging.info("1 record is inserted into {} table".format(second_table_name))
            sqlite_connection.commit()
            cursor.close()

        except sqlite3.Error as error:
            logging.error("Failed to insert records into table", error)
        finally:
            sqlite_connection.close()
            logging.info("Connection is closed")

    def for_main(self, model):
        self.create_table()
        self.insert_table(model)
        self.create_second_table(model)
