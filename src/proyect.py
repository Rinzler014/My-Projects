from airportDP import *
from airportUI import *

if __name__ == '__main__':

    ui = Menu()
    validate = ValidateInput()
    loader = ExecuteMenus()

    while 1:
        ui.display_menu()
        option = ui.ask_for_input_menu()
        validate_input = validate.validate_input_display_menu(option)

        while validate_input == None:
            option = ui.ask_for_input_menu()
            validate_input = validate.validate_input_display1_menu(option)

        loader.execute_menu(validate_input)

        if option == 5:

            option = ui.ask_for_input_menu()
            validate_input = validate.validate_input_pilot_and_attendant_menu(option)

            while validate_input == None:
                option = ui.ask_for_input_menu()
                validate_input = validate.validate_input_display_menu(option)

            loader.execute_pilot(validate_input)


        elif option == 6:

            option = ui.ask_for_input_menu()
            validate_input = validate.validate_input_pilot_and_attendant_menu(option)

            while validate_input == None:
                option = ui.ask_for_input_menu()
                validate_input = validate.validate_input_display_menu(option)

            loader.execute_attendant(validate_input)

        elif option == 7:

            option = ui.ask_for_input_menu()
            validate_input = validate.validate_input_traveller_menu(option)

            while validate_input == None:
                option = ui.ask_for_input_menu()
                validate_input = validate.validate_input_display_menu(option)

            loader.execute_traveller(validate_input)

        elif option == 8:

            option = ui.ask_for_input_menu()
            validate_input = validate.validate_input_passenger_menu(option)

            while validate_input == None:
                option = ui.ask_for_input_menu()
                validate_input = validate.validate_input_display_menu(option)

            loader.execute_passenger(validate_input)

        elif option == 9:

            option = ui.ask_for_input_menu()
            validate_input = validate.validate_input_flight_menu(option)

            while validate_input == None:
                option = ui.ask_for_input_menu()
                validate_input = validate.validate_input_display_menu(option)

            loader.execute_flight(validate_input)

            if option == 6:

                option = ui.ask_for_input_menu()
                validate_input = validate.validate_input_flight_menu_crew(option)

                while validate_input == None:
                    option = ui.ask_for_input_menu()
                    validate_input = validate.validate_input_display_menu(option)

                loader.execute_crew(validate_input)
