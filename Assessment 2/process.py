import os.path
import sqlite3


class Database:
    def __init__(self, name):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.fullpath = os.path.join(self.path, name)
        self._conn = sqlite3.connect(self.fullpath)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql):
        self.cursor.execute(sql)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
            


def login_check(database, user_id) -> str:
    """ User_id check. DB call to confirm login user exists """
    
    # Setup params. SQL query & return level (query_type). ALL/ONE/MANY
    sql = "SELECT shopper_id, shopper_first_name, shopper_surname \
        FROM shoppers WHERE shopper_id = (?);"    
    data = None
    data = database.query(sql, (user_id,))

    # If data returned, pull first/last nam as data output
    if data is not None:
        for d in data:
            first_nam = d[1]
            second_nam = d[2]
            data = first_nam + ' ' + second_nam

        return data
    return

def a(database, user_id) -> str:
    """ Display your order history """

    sql = "SELECT basket_id \
            FROM shopper_baskets \
            WHERE shopper_id = (?) \
            AND DATE(basket_created_date_time) = DATE('now') \
            ORDER BY basket_created_date_time DESC \
            LIMIT 1;"
    
    data = None
    data = database.query(sql, (user_id,))

    # If data returned, pull first/last nam as data output
    if data is not None:
        for d in data:
            first_nam = d[1]
            second_nam = d[2]
            data = first_nam + ' ' + second_nam

        return data
    return

def b(user_id):
    print('\n\nSuccess - b called\n\n')

def c(user_id):
    print('\n\nSuccess - c called\n\n')

def d(user_id):
    print('\n\nSuccess - d called\n\n')

def e(user_id):
    print('\n\nSuccess - e called\n\n')

def f(user_id):
    print('\n\nSuccess - f called\n\n')