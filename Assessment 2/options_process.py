import visuals as vis
import database as dab
import user_input_checks as usimp

def mn_return_prv_basket(db: object, user_id: int) -> str | bool:
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


def mn_func_1(db: object, user_id: int) -> None:
    """ Display your order history """

    # sql query, single var input
    sql = "SELECT \
                shopper_orders.order_id AS [Order ID] \
                ,STRFTIME('%d-%m-%Y', shopper_orders.order_date) AS [Order Date] \
                ,prod.product_description AS [Product Description] \
                ,sel.seller_name AS [Seller Name] \
                ,CONCAT('£', ROUND(ordered_products.price, 2)) AS [Price] \
                ,ordered_products.quantity AS [Qty Ordered] \
                ,shopper_orders.order_status AS [Order Status] \
                \
            FROM shopper_orders \
                INNER JOIN shoppers ON shoppers.shopper_id = shopper_orders.shopper_id \
                INNER JOIN ordered_products ON ordered_products.order_id = shopper_orders.order_id \
                INNER JOIN products prod ON prod.product_id = ordered_products.product_id \
                INNER JOIN sellers sel ON sel.seller_id = ordered_products.seller_id \
                \
            WHERE shopper_orders.shopper_id = (?) \
            \
            ORDER BY shopper_orders.order_date DESC;"
    
    data = db.query(sql, (user_id,))
    
    # data check
    if data[1]:
        header_list = data[0]
        data_list = data[1]

        vis.print_sql_data(header_list,data_list)
    else:
        print('No orders placed by this customer')


def mn_func_2(db: object, user_id: int) -> bool:
    """ add item to your basket """

    try:
        # sql query, not var input, run open
        sql = "SELECT category_description \
                FROM categories \
                ORDER BY category_description;"  
        
        data = db.query(sql,None)
        prd_list = []

        # Pull cat value & enumirate list for options func
        # display results & request userinput
        for i in range(len(data[1])):
            prd_list.append((i+1,data[1][i][0]))

        user_input = vis.display_options(prd_list,'Product Categories','product category')

        # sql query, var input from above return
        sql = "SELECT product_description \
                ,product_id \
                FROM products \
                WHERE category_id = (?) \
                ORDER BY product_description;" 
        
        data = db.query(sql,(user_input,))
        prd_list = []

        # Pull cat value & enumirate list for options func
        # display results & request userinput
        # end var = userinput index return from selection
        for i in range(len(data[1])):
            prd_list.append((i+1,data[1][i][0]))

        user_input_prd = vis.display_options(prd_list,'Products','product')
        
        # get prd nam
        for i in range(len(prd_list[i])):
            if prd_list[i][0] == user_input_prd:
                user_input_prd = prd_list[i][1]

        # get actual product_id
        for i in range(len(data[1])):
            if data[1][i][0] == user_input_prd:
                user_input_prd_id = data[1][i][1]

        # sql query, not var input from above return
        sql = "SELECT \
                concat(sel.seller_name,' (',PRINTF('£%9.2f',prcsel.price),')') \
                ,prcsel.price \
                ,sel.seller_id \
                FROM product_sellers prcsel \
                INNER JOIN products prd ON prd.product_id = prcsel.product_id \
                INNER JOIN sellers sel ON sel.seller_id = prcsel.seller_id \
                WHERE prd.product_description = (?) \
                ORDER BY sel.seller_name;"
        
        data = db.query(sql,(user_input_prd,))
        prd_list = []

        # Pull cat value & enumirate list for options func
        # display results & request userinput
        # end var = userinput index return from selection
        for i in range(len(data[1])):
            prd_list.append((i+1,data[1][i][0]))

        user_input_sel = vis.display_options(prd_list,'Sellers who sell this product','seller')
        
        # get sel nam
        for i in range(len(prd_list[i])):
            if prd_list[i][0] == user_input_sel:
                user_input_sel = prd_list[i][1]

        # get actual price, seller_id
        for i in range(len(data[1])):
            if data[1][i][0] == user_input_sel:
                user_input_price = data[1][i][1]
                user_input_seller = data[1][i][2]

        # User qty input data validation
        user_input_qty = 0

        while int(user_input_qty) <= 0:
            user_input_qty = input("Enter the quantity of the selected product you want to buy: ")

            if not user_input_qty.isnumeric():
                print(f'\n -- Please enter a number greater than 0 -- \n')
                user_input_qty = 0
      
        user_input_qty = int(user_input_qty) 

        # get backet id if exist
        # else, create backet id, get and insert into basket_contents
        basket_id = mn_return_prv_basket(db, user_id)
        
        if not basket_id:
            # create new basket
            sql = "INSERT INTO shopper_baskets (shopper_id, basket_created_date_time) VALUES((?),DATE('now'));"
            db.insert(sql,(user_id,))
            db.commit()
            basket_id = mn_return_prv_basket(db, user_id)
        
        # with basket_id, add values to the basket_contents
        sql = "SELECT basket_id \
                FROM basket_contents \
                WHERE basket_id = (?) \
                AND product_id = (?) \
                LIMIT 1;"
        
        data = db.query(sql, (basket_id,user_input_prd_id))

        # If data returned, return basket_id
        if len(data[1]) > 0:
            print(f"\nItem '{user_input_prd}' is already within basket, to update/remove item. Please use the options from main menu\n")

        else:
            sql = "INSERT INTO basket_contents (basket_id,product_id,seller_id,quantity,price) VALUES((?),(?),(?),(?),(?));"            
            db.insert(sql,(basket_id,user_input_prd_id,user_input_seller,user_input_qty,user_input_price))
            db.commit()
            print('Item added to your basket')


    except Exception as err: # Exception Block. Return data to user & False
        print(f"\n\n** Unexpected {err=}, {type(err)=} ** \n\n")
        db.rollback()
        return False


def mn_func_3(db: object, user_id: int) -> tuple | bool:
    """ Display current basket """

    basket_id = mn_return_prv_basket(db, user_id)
    
    # with basket_id, add values to the basket_contents
    sql = "SELECT \
            prd.product_description as 'Product Description'\
            ,sel.seller_name as 'Seller Name' \
            ,bsk.quantity \
            ,PRINTF('£%9.2f',bsk.price) as 'Price' \
            ,PRINTF('£%9.2f',bsk.price * bsk.quantity) as 'Total' \
            FROM basket_contents bsk \
            JOIN product_sellers prcsel ON prcsel.product_id = bsk.product_id AND prcsel.seller_id = bsk.seller_id \
            JOIN products prd ON prd.product_id = prcsel.product_id \
            JOIN sellers sel ON sel.seller_id = prcsel.seller_id \
            WHERE bsk.basket_id = (?);"
    
    data = db.query(sql, (basket_id,))

    sql = "SELECT \
            PRINTF('£%9.2f',SUM(bsk.price * bsk.quantity)) as 'total' \
            FROM basket_contents bsk \
            JOIN product_sellers prcsel ON prcsel.product_id = bsk.product_id AND prcsel.seller_id = bsk.seller_id \
            JOIN products prd ON prd.product_id = prcsel.product_id \
            JOIN sellers sel ON sel.seller_id = prcsel.seller_id \
            WHERE bsk.basket_id = (?);"

    backet_data = db.query(sql, (basket_id,))

    # data check
    if data[1]:
        header_list = data[0]
        data_list = data[1]
        out_list = []
        num = 1        
        header_list.insert(0,'Basket Item Num')

        for data_val in data_list:
            new_data_list = [num]

            for val in data_val:
                new_data_list.append(val)

            num += 1
            out_list.append(tuple(new_data_list))

        out_list_ret = tuple(out_list)
        out_list.append(['', '', '', '', '', ''])
        out_list.append(['', '', "Basket Total", '', '', backet_data[1][0][0]])
        data_list = tuple(out_list)

        print('Basket Contents')
        print('----------------')
        vis.print_sql_data(header_list,data_list)
    else:
        print('Your basket is empty')
    
    if out_list_ret:
        return out_list_ret
    else:
        return False


def mn_func_4(db: object, user_id: int) -> None:
    """ change qty within user basket """

    # print basket, return values in tuple
    # No data returned. return to main menu (None)
    output_data = mn_func_3(db, user_id)

    if not output_data:
        return None

    # check basket length, 2+ user choose
    if len(output_data) >= 2:
        in_list = False

        # check user input is value item no.
        while in_list:            
            user_promt_itm = 'Enter the basket item no. of the item you want to change: '
            output_itm = usimp.check_user_imp_int(user_promt_itm, '-- Please enter a number not a letter --')

            for data in output_data:            
                if data[0] == output_itm:
                    in_list = True   

            # if found within data/basket
            # break to endpoint else error to user
            if in_list:                
                break
            else:
                print('The basket item no. you have entered is invalid')                
    else:
        user_promt_itm = 1

    # Get user input qty as var for sql query
    user_promt_qty = 'Enter the basket item no. of the item you want to change: '
    output_qty = usimp.check_user_imp_int(user_promt_qty, 'The quantity must be greater then zero')


    print('Do update -- ASK QTY ')


    # Reprint basket post update
    mn_func_3(db, user_id)



def mn_func_5(db: object, user_id: int):
    print('\n\nSuccess - 6 called\n\n')


def mn_func_6(db: object, user_id: int):
    print('\n\nSuccess - 7 called\n\n')