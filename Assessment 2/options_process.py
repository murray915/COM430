import visuals as vis


def mn_return_prv_basket(db: object, user_id: int) -> str:
    """ return previous basket if found from today """

    sql = "SELECT basket_id \
            FROM shopper_baskets \
            WHERE shopper_id = (?) \
            AND DATE(basket_created_date_time) = DATE('now') \
            ORDER BY basket_created_date_time DESC \
            LIMIT 1;"
    
    data = None
    data = db.query(sql, (user_id,))

    # If data returned, pull first/last nam as data output
    if data is not None:
        for d in data:
            first_nam = d[1]
            second_nam = d[2]
            data = first_nam + ' ' + second_nam

        return data
    return


def mn_func_1(db: object, user_id: int) -> None:
    """ Display your order history """

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
    
    data = None
    data = db.query(sql, (user_id,))
    
    # data check
    if data:
        header_list = data[0]
        data_list = data[1]

        vis.print_sql_data(header_list,data_list)
    else:
        print('No orders placed by this customer')


def mn_func_2(user_id):
    print('\n\nSuccess - 2 called\n\n')


def mn_func_3(user_id):
    print('\n\nSuccess - 3 called\n\n')


def mn_func_4(user_id):
    print('\n\nSuccess - 4 called\n\n')


def mn_func_4(user_id):
    print('\n\nSuccess - 5 called\n\n')


def mn_func_5(user_id):
    print('\n\nSuccess - 6 called\n\n')


def mn_func_6(user_id):
    print('\n\nSuccess - 7 called\n\n')