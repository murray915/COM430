

def return_prv_basket(db: object, user_id: int) -> int | bool:
    """ return previous basket if found from today """

    sql = "SELECT basket_id \
            FROM shopper_baskets \
            WHERE shopper_id = (?) \
            AND DATE(basket_created_date_time) = DATE('now') \
            ORDER BY basket_created_date_time DESC \
            LIMIT 1;"
    
    data = db.query(sql, (user_id,))

    # If data returned, return basket_id
    if len(data[1]) > 0:
        return data[1][0][0]
    else:
        return False
            

def check_user_imp_int(text: str, err_reponse: str) -> int:
    """ check if value is above 0 """
    user_input_qty = 0

    while int(user_input_qty) <= 0:
        user_input_qty = input(text)

        if not user_input_qty.isnumeric():
            print(err_reponse)
            user_input_qty = 0
    
    return user_input_qty


def check_user_imp_prd_id(db: object, data: str) -> str:

    try:
        # check basket length, 2+ user choose
        if len(data) >= 2:
            in_list = False

            # check user input is value item no.
            while not in_list:            
                user_promt_itm = 'Enter the basket item no. of the item you want to change: '
                output_user_data = check_user_imp_int(user_promt_itm, '-- Please enter a number not a letter --')

                for data in data:            
                    if data[0] == int(output_user_data):
                        output_itm_des = data[1]
                        in_list = True

                # if found within data/basket
                # break to endpoint else error to user
                if in_list:                
                    break
                else:
                    print('The basket item no. you have entered is invalid')                
        else:
            output_itm_des = data[0][1]

        # get product_id from desc - basket data return
        sql = "SELECT product_id, product_description FROM products WHERE product_Description = (?);"        
        return_prd_id = db.query(sql, (output_itm_des,))

        return return_prd_id[1][0][0]

    except Exception as err: # Exception Block. Return data to user & False
        print(f"\n\n** Unexpected {err=}, {type(err)=} ** \n\n")  