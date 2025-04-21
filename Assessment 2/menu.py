import process as prs
from prettytable import PrettyTable

class Menu:
    def __init__(self, headers: list, options: list):
        """ Menu Attributes"""
        self.headers = headers
        self.options = options
        self.exit = False

    def menu_navigation(self):        
        """ Menu print & user selection """        
        self.user_input = None
        self.select_option = None

        try:
            self.print_table()
            self.user_input = input() 

            #Force user to input required option/list only. Loop until accepted            
            if self.user_input is None:
                while self.select_option is None:
                    self.user_input = input('Invalid user choice. Please re-enter.\n')

                    for i in self.options:
                        for j in i:
                            if j == self.user_input.upper():
                                self.select_option = i[1]
            
            #Return user input value (from list), then return to main
            print(f'You have chosen option {self.user_input.upper()} - {self.select_option}')
            
            if self.user_input.upper() == "X":
                self.exit = True

            self.user_input = self.user_input
            return self.user_input.upper()

        except Exception as err: # Exception Block. Return data to user & input
            print(f"Unexpected {err=}, {type(err)=}. From user input ; {self.user_input}")
    

    def print_table(self):
        table = PrettyTable()
        table.field_names = self.headers
        table.add_rows(self.options)

        print(table)


    def call_fuction(self):
        """ User input from Menu. Nav to call next func """ 
        if self.user_input is not None:
            func = getattr(prs, self.user_input)
            func(self.user_input)


main_menu = Menu(["Option", "Description"],[
    ["A","Display your order history"],
    ["B", "Add an item to your basket"],
    ["C", "View your basket"],
    ["D", "Change the quantity of an item in your basket"],
    ["E", "Remove an item from your basket"],
    ["F", "Checkout"],
    ["X", "Exit"]
    ])
