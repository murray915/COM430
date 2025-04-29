from tabulate import tabulate


def welcome_screen() -> None:
    """Input data, first name / surname printout"""
    print(
            '\n'
            '-------------------------------------'
            '\n'
            '        Welcome to Paraná            '
            '\n'
            '-------------------------------------'
            )


def welcome_screen_post_login(user_id: str) -> None:
    """Input data, first name / surname printout"""
    print(
            '\n'
            '-------------------------------------'
            '\n'
            '----------- Login Successful --------'
            '\n'
            '-------------------------------------'
            '\n'
            f' Login User :   {user_id}              '
            '\n'
            '-------------------------------------'
            '\n'
            )


def failed_login() -> None:
    """"Failed login, printout"""
    print(
        '-------------------------------------'
        '\n'
        '            ERROR                    '
        '\n'
        '   Shopper ID has not been found     '
        '\n'
        '   Please input a valid shopper ID   '
        '\n'
        '  or input "exit", to close program  '
        '\n'
        '-------------------------------------'
        )
    

def exit_screen() -> None:
    """"exit screen, printout"""
    print(
        '\n'
        '-------------------------------------'
        '\n'
        '----- Thank you for shopping at -----'
        '\n'
        '-------------------------------------'
        '\n'
        '-------------- Paraná ---------------'
        '\n'
        '-------------------------------------'
        '\n'
        )
    
    quit()


def print_sql_data(sql_headers: list, data: list) -> None:
    """
    headers: str(s) within list
    data: sql returned raw data
    """   
    output = []

    for i in data:
        output.append(list(i))

    print(tabulate(
        output, 
        headers=sql_headers
        ))