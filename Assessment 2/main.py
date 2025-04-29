import database as dab
import visuals as vis
import login_check as lch
import options_process as optpr

vis.welcome_screen()

with dab.Database("parana.db") as db:
    database = db
    main_selection = None
    data, user_id = lch.login_process(database)

    if user_id:
        vis.welcome_screen_post_login(data)

        while main_selection != 7:
            main_selection = vis.main_menu()
            
            # Call user_input func
            # 7 = exit
            if main_selection != 7:
                func = getattr(optpr, 'mn_func_' + str(main_selection))
                output = func(db, user_id)

                if output == False:
                    print(f'Error occured : Rollback completed. \n')
                    main_selection = 7

    vis.exit_screen()
