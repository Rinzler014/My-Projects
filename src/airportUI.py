class Menu:

    def display_menu(self):

        print("-"*50)
        print("Welcome!")
        print("-"*50)

        print("Please select an option:")
        print("1. Generate Statistics")
        print("2. Add Flight")
        print("3. Add Traveller")
        print("4. Add Passenger")
        print("5. Edit Pilot")
        print("6. Edit Attendant")
        print("7. Edit Traveller")
        print("8. Edit Passenger")
        print("9. Edit Flight")
        print("0. Exit")

    def pilot_menu(self):
        print("What would you like to modify?")
        print("1. Marital status")
        print("0. Back")

    def attendant_menu(self):
        print("What would you like to modify?")
        print("1. Marital status")
        print("0. Back")

    def traveller_menu(self):
        print("What would you like to modify?")
        print("1. Marital status")
        print("2. Gender")
        print("3. Birth date")
        print("4. Forename")
        print("5. Surname")
        print("0. Back")

    def passenger_menu(self):
        print("What would you like to modify?")
        print("1. Seat")
        print("2. Flight class")
        print("3. Check-point location")
        print("0. Back")

    def flight_menu(self):
        print("What would you like to modify?")
        print("1. Flight status")
        print("2. Departure gate")
        print("3. Arrival gate")
        print("4. Take off track")
        print("5. Landing track")
        print("6. Crew")
        print("0. Back")

    def crew_menu(self):
        print("What part of the flight crew would you like to modify?")
        print("1. Pilot")
        print("2. Copilot")
        print("3. Attendants")
        print("0. Back")

    def ask_for_input_menu(self):

        option = int(input("-->"))
        return option

class ValidateInput:

    def validate_input_display_menu(self, _option):

        if _option < 0 or _option > 9:
            print("Opción inválida")
            return None
        else:
            return _option

    def validate_input_pilot_and_attendant_menu(self, _option):

        if _option < 0 or _option > 1:
            print("Opción inválida")
            return None
        else:
            return _option

    def validate_input_traveller_menu(self, _option):

        if _option < 0 or _option > 5:
            print("Opción inválida")
            return None
        else:
            return _option

    def validate_input_passenger_menu(self, _option):

        if _option < 0 or _option > 3:
            print("Opción inválida")
            return None
        else:
            return _option

    def validate_input_flight_menu(self, _option):

        if _option < 0 or _option > 6:
            print("Opción inválida")
            return None
        else:
            return _option

    def validate_input_flight_menu_crew(self, _option):

        if _option < 0 or _option > 3:
            print("Opción inválida")
            return None
        else:
            return _option

class UserTimes:

    def ask_for_date(self):

        print("Please enter the desired date in YYMMDD format to generate the report.")
        date_in_YYMMDD = int(input())
        return date_in_YYMMDD

    def ask_for_time(self):

        print("Please enter the desired time in HHMM format to generate the report.")
        time_in_HHMM = int(input())
        return time_in_HHMM

class UserAdd:

    def ask_for_flight_info(self):

        print("Please give the following information in order to add the flight:")
        flight_id = str(input("Input the ID:"))
        plate = str(input("Input the plate:"))
        origin = str(input("Input the origin in the following format \"CITY - COUNTRY\":"))
        destiny = str(input("Input the destiny in the following format \"CITY - COUNTRY\":"))
        departure = str(input("Input the destiny in the following format \"YYMMDD_HHMM_CONTINENT/COUNTRY\":"))
        arriving = str(input("Input the arrival in the following format \"YYMMDD_HHMM_CONTINENT/COUNTRY\":"))
        status = str(input("Input the status:"))
        departure_gate = str(input("Input the departure gate:"))
        take_off_track = str(input("Input the take off track:"))
        arriving_gate = str(input("Input the arrival gate:"))
        landing_track = str(input("Input the landing track:"))
        pilot = str(input("Input the pilot for this flight:"))
        copilot = str(input("Input the copilot for this flight:"))
        attendants = str(input("Input the attendants in the following format \"AA1234\;BB5678\;CC9101\;...\":"))

        flight = [flight_id, plate, origin, destiny, departure, arriving, status, departure_gate, take_off_track, arriving_gate, landing_track, pilot, copilot, attendants]

        return flight

    def ask_for_traveller_info(self):

        print("Please give the following information in order to add the traveller:")
        passport = str(input("Input the passport:"))
        forename = str(input("Input the forename:"))
        surname = str(input("Input the surname:"))
        date_of_birth = str(input("Input the date of birth:"))
        country = str(input("Input the country:"))
        gender = str(input("Input the gender:"))
        marital_status = str(input("Input the marital status:"))

        traveller = [passport, forename, surname, date_of_birth, country, gender, marital_status]

        return traveller

    def ask_for_passenger_info(self):

        print("Please give the following information in order to add the passenger:")
        flight = str(input("Input the flight ID:"))
        passport = str(input("Input the passport:"))
        passenger_class = str(input("Input the class of the passenger:"))
        seat = str(input("Input the seat:"))
        location = str(input("Input the check point location at which the passenger is:"))

        passenger = [flight, passport, passenger_class, seat, location]

        return passenger

class UserInfoPilot:

    def ask_for_pilot_info_marital_status(self):

        print("Please give the following information in order to modify the pilot's marital status.")
        pilot_passport = str(input("Input the pilot's passport:"))
        marital_status = str(input("Input the pilot's new marital status:"))

        while marital_status not in ["Married", "Widowed", "Single", "Divorced"]:
            print("This marital status is not valid. Please input the pilot's marital status again:")
            marital_status = str(input("Input the pilot's new marital status:"))

        return pilot_passport, marital_status

class UserInfoAttendant:

    def ask_for_attendant_info_marital_status(self):

        print("Please give the following information in order to modify the attendant's marital status.")
        attendant_passport = str(input("Input the attendant's passport:"))
        marital_status = str(input("Input the attendant's new marital status:"))

        while marital_status not in ["Married", "Widowed", "Single", "Divorced"]:
            print("This marital status is not valid. Please input the attendant's marital status again:")
            marital_status = str(input("Input the attendant's new marital status:"))

        return attendant_passport, marital_status

class UserInfoTraveller:

    def ask_for_traveller_info_marital_status(self):

        print("Please give the following information in order to modify the traveller's marital status.")
        traveller_passport = str(input("Input the traveller's passport:"))
        marital_status = str(input("Input the traveller's new marital status:"))

        while marital_status not in ["Married", "Widowed", "Single", "Divorced"]:
            print("This marital status is not valid. Please input the traveller's marital status again:")
            marital_status = str(input("Input the traveller's new marital status:"))

        return traveller_passport, marital_status

    def ask_for_traveller_info_gender(self):

        print("Please give the following information in order to modify the traveller's gender.")
        traveller_passport = str(input("Input the traveller's passport:"))
        gender = str(input("Input the traveller's gender:"))

        while gender not in ["Male", "Female", "NA"]:
            print("This gender is not valid. Please input the traveller's gender again:")
            gender = str(input("Input the traveller's gender:"))

        return traveller_passport, gender

    def ask_for_traveller_info_birth_date(self):

        print("Please give the following information in order to modify the traveller's birth date.")
        traveller_passport = str(input("Input the traveller's passport:"))
        date_of_birth = str(input("Input the traveller's new birth date in \"YYMMDD\" format:"))

        return traveller_passport, date_of_birth

    def ask_for_traveller_info_forename(self):

        print("Please give the following information in order to modify the traveller's forename.")
        traveller_passport = str(input("Input the traveller's passport:"))
        forename = str(input("Input the traveller's forename:"))

        return traveller_passport, forename

    def ask_for_traveller_info_surname(self):
        print("Please give the following information in order to modify the traveller's surname.")
        traveller_passport = str(input("Input the traveller's passport:"))
        surname = str(input("Input the traveller's surname:"))

        return traveller_passport, surname

class UserInfoPassenger:

    def ask_for_passenger_info_seat(self):

        print("Please give the following information in order to modify the passenger's seat.")
        passenger_flight = str(input("Input the passenger flight's ID:"))
        passenger_passport = str(input("Input the passenger's passport:"))
        seat = str(input("Input the passenger's seat:"))
        
        return passenger_flight, passenger_passport, seat

    def ask_for_passenger_info_flight_class(self):

        print("Please give the following information in order to modify the passenger's flight class.")
        passenger_flight = str(input("Input the passenger flight's ID:"))
        passenger_passport = str(input("Input the passenger's passport:"))
        flight_class = str(input("Input the passenger's flight class:"))

        while flight_class not in ["First", "Business", "Economy", "premier"]:
            print("This flight class is not valid. Please input a valid flight class:")
            flight_class = str(input("Input the passenger's flight class:"))

        return passenger_flight, passenger_passport, flight_class

    def ask_for_passenger_info_check_point(self):

        print("Please give the following information in order to modify the passenger's check point location.")
        passenger_flight = str(input("Input the passenger flight's ID:"))
        passenger_passport = str(input("Input the passenger's passport:"))
        check_point = str(input("Input the passenger's new check point location:"))

        while check_point not in ["check-in", "security", "boarded"]:
            print("This check point location is not valid. Please input a valid check point location:")
            check_point = str(input("Input the passenger's check point location:"))

        return passenger_flight, passenger_passport, check_point

class UserInfoFlight:

    def ask_for_flight_info_status(self):

        print("Please give the following information in order to modify the flight's status.")
        flight_id = str(input("Input the flight's ID:"))
        flight_plate = str(input("Input the flight's plate:"))
        flight_status = str(input("Input the flight's new status:"))

        while flight_status not in ["boarded", "boarding", "in-transit", "landing", "landed", "waiting"]:
            print("This flight status is not valid. Please input a valid flight status:")
            check_point = str(input("Input the flight's new status:"))

        return flight_id, flight_plate, flight_status

    def ask_for_flight_info_departure_gate(self):

        print("Please give the following information in order to modify the flight's departure gate.")
        flight_id = str(input("Input the flight's ID:"))
        flight_plate = str(input("Input the flight's plate:"))
        flight_departure_gate = str(input("Input the flight's new departure gate:"))

        return flight_id, flight_plate, flight_departure_gate

    def ask_for_flight_info_arrival_gate(self):

        print("Please give the following information in order to modify the flight's arrival gate.")
        flight_id = str(input("Input the flight's ID:"))
        flight_plate = str(input("Input the flight's plate:"))
        flight_arrival_gate = str(input("Input the flight's new arrival gate:"))

        return flight_id, flight_plate, flight_arrival_gate

    def ask_for_flight_info_take_off_track(self):

        print("Please give the following information in order to modify the flight's take off track.")
        flight_id = str(input("Input the flight's ID:"))
        flight_plate = str(input("Input the flight's plate:"))
        flight_take_off_track = str(input("Input the flight's new take off track:"))

        return flight_id, flight_plate, flight_take_off_track

    def ask_for_flight_info_landing_track(self):

        print("Please give the following information in order to modify the flight's landing track.")
        flight_id = str(input("Input the flight's ID:"))
        flight_plate = str(input("Input the flight's plate:"))
        flight_landing_track = str(input("Input the flight's new landing track:"))

        return flight_id, flight_plate, flight_landing_track

    def ask_for_flight_info_pilot(self):

        print("Please give the following information in order to modify the flight's pilot.")
        flight_id = str(input("Input the flight's ID:"))
        flight_plate = str(input("Input the flight's plate:"))
        flight_pilot = str(input("Input the flight's new pilot:"))

        return flight_id, flight_plate, flight_pilot

    def ask_for_flight_info_copilot(self):

        print("Please give the following information in order to modify the flight's copilot.")
        flight_id = str(input("Input the flight's ID:"))
        flight_plate = str(input("Input the flight's plate:"))
        flight_copilot = str(input("Input the flight's new copilot:"))

        return flight_id, flight_plate, flight_copilot

    def ask_for_flight_info_attendants(self):

        print("Please give the following information in order to modify the flight's attendants.")
        flight_id = str(input("Input the flight's ID:"))
        flight_plate = str(input("Input the flight's plate:"))
        flight_attendants = str(input("Input the attendants in the following format \"AA1234\;BB5678\;CC9101\;...\":"))

        return flight_id, flight_plate, flight_attendants
