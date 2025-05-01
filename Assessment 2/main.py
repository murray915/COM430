import database as dab
import visuals as vis
import login_check as lch
import options_process as optpr
import user_input_checks as usimp

vis.welcome_screen()

with dab.Database("parana.db") as db:
    database = db
    main_selection = None
    data, user_id = lch.login_process(database)

    if user_id:
        vis.welcome_screen_post_login(data)
        
        while main_selection != 7:
            main_selection = vis.main_menu()
            basket_id = usimp.return_prv_basket(db, user_id) 

            # Call user_input func 7 = exit
            if main_selection != 7:
                func = getattr(optpr, 'mn_func_' + str(main_selection))
                output = func(db, user_id, basket_id)

    vis.exit_screen()