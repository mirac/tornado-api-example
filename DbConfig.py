import MySQLdb


class Database:
    def __init__(self):
        pass

    @staticmethod
    def connect():
        return MySQLdb.connect("localhost", "mirac", "123", "sample_db")


