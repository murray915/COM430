import visuals as vis

def login_process(db: object) -> str:
    """ 3 Max attampte login func """

    try:
        # First request input
        user_id = input("\nEnter your shopper ID : ")
        data = login_check(db, user_id)
        max_login_count = 3

        # user_id not found / failed login
        if not data[1]:
            login_counter = 1

            # hold user for attempt count or exit input 
            while login_counter < max_login_count or user_id != 'EXIT':
                vis.failed_login()
                user_id = input(f"\nEnter your shopper ID or 'EXIT' : ") 
                data = login_check(db, user_id)
                
                # user_id found, return data
                if not data[1]:
                    login_counter +=1
                else:
                    return data, user_id
                
                if login_counter >= max_login_count or user_id == 'EXIT':
                    vis.exit_screen()

        # user_id found, return data         
        else:
            return data, user_id
        
    except Exception as err: # Exception Block. Return data to user & False
        print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n")
        vis.exit_screen()


def login_check(database: object, user_id: int) -> str | None:
    """ User_id check. DB call to confirm login user exists """
    
    # Setup params. SQL query & return level (query_type). ALL/ONE/MANY
    sql = "SELECT shopper_id, shopper_first_name, shopper_surname \
        FROM shoppers WHERE shopper_id = (?);"    
    data = None
    data = database.query(sql, (user_id,))

    # If data returned, pull first/last nam as data output
    if data is not None:
        for d in data[1]:
            first_nam = d[1]
            second_nam = d[2]
            data = first_nam + ' ' + second_nam

        return data
    return None