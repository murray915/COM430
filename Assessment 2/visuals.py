def welcome_screen(data: str):
    """Input data, first name / surname printout"""
    print(
            '\n'
            '-------------------------------------'
            '\n'
            '        Welcome to Paraná            '
            '\n'
            '-------------------------------------'
            '\n'
            '-------------------------------------'
            '\n'
            f' Login User :   {data}              '
            '\n'
            '-------------------------------------'
            '\n'
            )


def failed_login():
    """"Failed login, printout"""
    print(
        '-------------------------------------'
        '\n'
        '            ERROR                    '
        '\n'
        '   Shopper ID has not been found     '
        '\n'
        '   Please input a valid shopper ID.  '
        '\n'
        '-------------------------------------'
        )