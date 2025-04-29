import menu as mn
import database as db
import visuals as vis
import login_check as lch
import options_process as optpr

vis.welcome_screen()

with db.Database("parana.db") as db:
    database = db
    main_selection = None
    data, user_id = lch.login_process(database)

    if user_id:
        vis.welcome_screen_post_login(data)

        while main_selection != 7:
            main_selection = mn.main_menu()
            
            # Call user_input func
            # 7 = exit
            if main_selection != 7:
                func = getattr(optpr, 'mn_func_' + str(main_selection))
                func(db, user_id)

    vis.exit_screen()
