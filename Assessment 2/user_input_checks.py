

def check_user_imp_int(text: str, err_reponse: str) -> int:
    """ check if value is above 0 """
    user_input = 0

    while int(user_input_qty) <= 0:
        user_input_qty = input(text)

        if not user_input_qty.isnumeric():
            print(err_reponse)
            user_input_qty = 0