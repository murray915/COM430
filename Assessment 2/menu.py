def display_options(all_options: list, title:str, type: str) -> str | bool:
    """
    query_rows: must consist of two values - id and description i.e. the category_id and category_description.
    title: is some text to put above the list of options to act as a title.
    type: is used to customise the prompt to make it appropriate for what you want the user to select.
    """
    try:
        option_num = 1
        option_list = []

        print("\n",title,"\n")

        for option in all_options:
            code = option[0]
            desc = option[1]

            print("{0}.\t{1}".format(option_num, desc))
            
            option_num = option_num + 1
            option_list.append(code)

        selected_option = 0

        while selected_option > len(option_list) or selected_option == 0:
            prompt = input("\nEnter the number against the "+type+" you want to choose: ")
            
            if not prompt.isnumeric():
                print(f'\n* ERROR * : Please enter only numbers (int)')
                selected_option = 0
            else:
                selected_option = int(prompt)
                
        return option_list[selected_option - 1]
    
    except Exception as err: # Exception Block. Return data to user & False
        print(f"\n\n** Unexpected {err=}, {type(err)=} \n\n **")
        return False
    

def main_menu() -> int:
   """ main menu var """
   
   ouput = display_options([
        [1, 'Display your order history'],
        [2, "Add an item to your basket"],
        [3, "View your basket"],
        [4, "Change the quantity of an item in your basket"],
        [5, "Remove an item from your basket"],
        [6, "Checkout"],
        [7, "Exit"]
        ],'PARANÁ – SHOPPER MAIN MENU','menu options')
   
   return ouput