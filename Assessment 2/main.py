import menu as mn
import process as prc




prc.login_check(10023)
prc.login_check(1231321)



while mn.main_menu.exit != True:
        mn.main_menu.menu_navigation()        
        
        if mn.main_menu.exit != True:
            mn.main_menu.call_fuction()