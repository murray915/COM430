import sqlite3 as sql3
import os.path

def db_connect_sql_select(sql_query: str, query_type: str):
    """func. to select sql query. input quer and query type, fetch ALL/ONE/MANY"""
    
    try:        
        # Get absolut path from file, return path & join to db name
        # Setup db connection var with path
        db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parana.db")
        db = sql3.connect(db_path)
        
        # Action input sql with db var
        with db:
            curser = db.cursor()
            curser.execute(sql_query)

            if query_type == 'ALL':
                pull_data = curser.fetchall()
            elif query_type == 'ONE':
                pull_data = curser.fetchone()
            else:
                pull_data = curser.fetchmany()

        return pull_data
    
    except Exception as err: # Exception Block. Return data to user & input
        print(f"Unexpected {err=}, {type(err)=}")


def login_check(user_id):
    """ User_id check. DB call to confirm login user exists """
    
    # Setup params. SQL query & return level (query_type). ALL/ONE/MANY
    user_exists = False
    sql_query = "SELECT shopper_id FROM shoppers;"
    query_type = "ALL"
 
    data = db_connect_sql_select(sql_query, query_type)
        
    for x, y in data:
        if y == user_id:       
            user_exists = True

    return user_exists





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