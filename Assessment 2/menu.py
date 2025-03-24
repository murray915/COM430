import process as prs


class Menu:
    def __init__(self, options: dict):
        """ Menu Attributes"""
        self.options = options
        self.user_input = 0
        self.exit = False


    def menu_navigation(self):
        """ Menu print & user selection """
        try:             
            for key in self.options.keys():
                print(f'    [{key}] {self.options[key]}') #Keys and resepective values
            
            user_input = input()
            
            #Force user to input required option/list only. Loop until accepted      
            while user_input.upper() not in self.options:        
                user_input = input('Invalid user choice. Please re-enter.\n')
            
            #Return user input value (from dictionary), then return main
            print(f'You have chosen option {user_input.upper()} - {self.options[user_input.upper()]}')
            
            if user_input.upper() == "X":
                self.exit = True

            self.user_input = user_input
            return user_input.upper()

        except Exception as err: # Exception Block. Return data to user & input
            print(f"Unexpected {err=}, {type(err)=}. From user input ; {user_input}")
    

    def call_fuction(self):
        """ User input from Menu. Nav to call next func """ 
        func = getattr(prs, self.user_input)
        func(self.user_input)


main_menu = Menu({
    "A": "Display your order history",
    "B": "Add an item to your basket",
    "C": "View your basket",
    "D": "Change the quantity of an item in your basket",
    "E": "Remove an item from your basket",
    "F": "Checkout",
    "X": "Exit"})