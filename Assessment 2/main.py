import menu as mn
import process as prc
import visuals as vis


user_id = input("\nEnter your shopper ID : ")

with prc.Database("parana.db") as db:
    database = db
    data = prc.login_check(db, user_id)
    
    if data:    
        vis.welcome_screen(data)

        while mn.main_menu.exit != True:
            mn.main_menu.menu_navigation()
             
            if mn.main_menu.exit != True:
                 mn.main_menu.call_fuction()
    else:
        vis.failed_login()


