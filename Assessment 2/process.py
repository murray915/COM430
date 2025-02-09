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
            


def login_check(database, user_id):
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





def a():
    print('Success - a called')

def b():
    print('Success - b called')

def c():
    print('Success - c called')

def d():
    print('Success - d called')

def e():
    print('Success - e called')

def f():
    print('Success - f called')