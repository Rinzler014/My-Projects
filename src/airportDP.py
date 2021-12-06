import csv
import sys
from airportUI import *

class Airport:

    def __init__(self):
        self.tracks = None
        self.airplanes = None
        self.passengers = None
        self.pilots = None
        self.attendants = None
        self.travellers = None


    def populate_airport(self):
        populate_airport = AirportAD()
        self.attendants = populate_airport.read_attendants_file()
        self.flights = populate_airport.read_flights_file()
        self.passengers = populate_airport.read_passengers_file()
        self.pilots = populate_airport.read_pilots_file()
        self.planes = populate_airport.read_planes_file()
        self.travellers = populate_airport.read_travellers_file()

class Flights:

    def __init__(self, _id, _plate, _origin, _destiny, _departure, _arriving, _status, _departure_gate, _take_off_track, _arriving_gate, _landing_track, _pilot, _copilot, _attendants):
        self.id = _id
        self.plate = _plate
        self.origin = _origin
        self.destiny = _destiny
        self.departure = _departure
        self.arriving = _arriving
        self.status = _status
        self.departure_gate = _departure_gate
        self.take_off_track = _take_off_track
        self.arriving_gate = _arriving_gate
        self.landing_track = _landing_track
        self.pilot = _pilot
        self.copilot = _copilot
        self.attendants = _attendants

class Crew:

    def __init__(self, _passport, _forename, _surname, _date_of_birth, _country, _gender, _marital_status):
        self.passport = _passport
        self.forename = _forename
        self.surname = _surname
        self.date_of_birth = _date_of_birth
        self.country = _country
        self.gender = _gender
        self.marital_status = _marital_status

class Travellers(Crew):
    pass

class Attendant(Crew):
    pass

class Pilot(Crew):
    pass

class Passengers:

    def __init__(self, _flight, _passport, _flight_class, _seat, _location):
        self.flight = _flight
        self.passport = _passport
        self.flight_class = _flight_class
        self.seat = _seat
        self.location = _location

class Planes:

    def __init__(self, _plate, _manufacturer, _model, _passengers_capacity, _luggage_capacity, _max_speed):
        self.plate = _plate
        self.manufacturer = _manufacturer
        self.model = _model
        self.passengers_capacity = _passengers_capacity
        self.luggage_capacity = _luggage_capacity
        self.max_speed = _max_speed

class AirportAD:

    def read_pilots_file(self):

        pilots_file = open("data/pilots.csv", "r")
        lines = pilots_file.readlines()
        pilots_file.close()
        lines.pop(0)

        pilots = {}

        for line in lines:
                fields = line.split(",")
                passport = fields[0]
                forename = fields[1]
                surname = fields[2]
                date_of_birth = fields[3]
                country = fields[4]
                gender = fields[5]
                marital_status = fields[6]

                pilot = Pilot(passport, forename, surname, date_of_birth, country, gender, marital_status)

                pilots[passport] = pilot

        return pilots

    def read_attendants_file(self):

        attendants_file = open("data/attendants.csv", "r")
        lines = attendants_file.readlines()
        attendants_file.close()
        lines.pop(0)

        attendants = {}

        for line in lines:
                fields = line.split(",")
                passport = fields[0]
                forename = fields[1]
                surname = fields[2]
                date_of_birth = fields[3]
                country = fields[4]
                gender = fields[5]
                marital_status = fields[6]

                attendant = Attendant(passport, forename, surname, date_of_birth, country, gender, marital_status)

                attendants[passport] = attendant

        return attendants

    def read_travellers_file(self):

        travellers_file = open("data/travellers.csv", "r")
        lines = travellers_file.readlines()
        travellers_file.close()
        lines.pop(0)

        travellers = {}

        for line in lines:
                fields = line.split(",")
                passport = fields[0]
                forename = fields[1]
                surname = fields[2]
                date_of_birth = fields[3]
                country = fields[4]
                gender = fields[5]
                marital_status = fields[6]

                traveller = Travellers(passport, forename, surname, date_of_birth, country, gender, marital_status)

                travellers[passport] = traveller

        return travellers

    def read_flights_file(self):

        flights_file = open("data/flights.csv", "r")
        lines = flights_file.readlines()
        flights_file.close()
        lines.pop(0)

        flights = {}

        for line in lines:
                fields = line.split(",")
                id = fields[0]
                plate = fields[1]
                origin = fields[2]
                destiny = fields[3]
                departure = fields[4]
                arriving = fields[5]
                status = fields[6]
                departure_gate = fields[7]
                take_off_track = fields[8]
                arriving_gate = fields[9]
                landing_track = fields[10]
                pilot = fields[11]
                copilot = fields[12]
                attendants = fields[13]

                flight = Flights(id, plate, origin, destiny, departure, arriving, status, departure_gate, take_off_track, arriving_gate, landing_track, pilot, copilot, attendants)

                flights[id + plate] = flight

        return flights

    def read_passengers_file(self):

        passengers_file = open("data/passengers.csv", "r")
        lines = passengers_file.readlines()
        passengers_file.close()
        lines.pop(0)

        passengers = {}

        for line in lines:
                fields = line.split(",")
                flight = fields[0]
                passport = fields[1]
                flight_class = fields[2]
                seat = fields[3]
                location = fields[4]

                passenger = Passengers(flight, passport, flight_class, seat, location)

                passengers[flight + passport] = passenger

        return passengers

    def read_planes_file(self):

        planes_file = open("data/planes.csv", "r")
        lines = planes_file.readlines()
        planes_file.close()
        lines.pop(0)

        planes = {}

        for line in lines:
                fields = line.split(",")
                plate = fields[0]
                manufacturer = fields[1]
                model = fields[2]
                passengers_capacity = fields[3]
                luggage_capacity = fields[4]
                max_speed = fields[5]

                plane = Planes(plate, manufacturer, model, passengers_capacity, luggage_capacity, max_speed)

                planes[plate] = plane

        return planes

class Check:

    def number_of_empty_tracks(self, _YYMMDD, _HHMM):

        flights_by_plate = {}
        count = 3

        for flight in AirportAD().read_flights_file().values():
                departure = flight.departure
                arrival = flight.arriving
                id = flight.id
                plate = flight.plate
                destiny = flight.destiny
                origin = flight.origin

                departure_time = departure.split("_")
                arrival_time = arrival.split("_")
                flights_by_plate[id + plate] = [departure_time[0], departure_time[1], arrival_time[0], arrival_time[1]]

        for flight in flights_by_plate.values():
                if destiny == "Ciudad de Mexico - MEXICO":
                        if int(flight[2]) == _YYMMDD and int(flight[3]) == _HHMM:
                                count -= 1

                elif origin == "Ciudad de Mexico - MEXICO":
                        if int(flight[0]) == _YYMMDD and int(flight[1]) == _HHMM:
                                count -= 1

        return count, flights_by_plate

    def number_of_busy_tracks(self, count):
            number_of_busy_tracks =  3 - count

            return number_of_busy_tracks

    def find_flights(self, _flights_by_plate, _date_in_YYMMDD, _time_in_HHMM):

        cut = []

        for flight in _flights_by_plate.values():
                if int(flight[0]) == _date_in_YYMMDD:
                        if int(flight[1]) <= _time_in_HHMM:
                                cut.append(list(_flights_by_plate.keys())[list(_flights_by_plate.values()).index(flight)])

                elif flight[2] == _date_in_YYMMDD:
                        if int(flight[3]) <= _time_in_HHMM:
                                cut.append(list(_flights_by_plate.keys())[list(_flights_by_plate.values()).index(flight)])

        return cut

    def count_check_in(self, _cut):

        check_in = 0

        for passenger_info in AirportAD().read_passengers_file().values():
                flight = passenger_info.flight
                location = passenger_info.location
                for plate in _cut:
                        if flight == plate[0:5] and str(location) == "check-in\n":
                                        check_in += 1

        return check_in

    def count_security(self, _cut):

        security = 0

        for passenger_info in AirportAD().read_passengers_file().values():
                flight = passenger_info.flight
                location = passenger_info.location
                for plate in _cut:
                        if flight == plate[0:5] and str(location) == "security\n":
                                        security += 1

        return security

    def count_boarded(self, _cut):

        boarded = 0

        for passenger_info in AirportAD().read_passengers_file().values():
                flight = passenger_info.flight
                location = passenger_info.location
                for plate in _cut:
                        if flight == plate[0:5] and str(location) == "boarded\n":
                                        boarded += 1

        return boarded

    def count_flights_off(self, _cut):

        flights_taken_off = 0

        for flight_info in AirportAD().read_flights_file().values():
                destiny = flight_info.destiny
                id = flight_info.id
                for plates in _cut:
                        if destiny == "Ciudad de Mexico - MEXICO" and plates[0:5] == id:
                                flights_taken_off += 1

        return flights_taken_off

    def count_flights_taken_in(self, _cut):

        flights_taken_in = 0

        for flight_info in AirportAD().read_flights_file().values():
                origin = flight_info.origin
                id = flight_info.id
                for plates in _cut:
                        if origin == "Ciudad de Mexico - MEXICO" and plates[0:5] == id:
                                flights_taken_in += 1

        return flights_taken_in

    def count_available_and_busy_gates(self, _date_in_YYMMDD, _time_in_HHMM):

        available_gate_list = []
        busy_gate_list = []

        for flight_info in AirportAD().read_flights_file().values():
                arriving_gate = flight_info.arriving_gate
                departure_gate = flight_info.departure_gate
                destiny = flight_info.destiny
                origin = flight_info.origin
                departure = flight_info.departure
                arrival = flight_info.arriving

                departure_time = departure.split("_")
                arrival_time = arrival.split("_")

                if destiny == "Ciudad de Mexico - MEXICO" and str(arriving_gate) not in available_gate_list:
                                available_gate_list.append(str(arriving_gate))

                                if str(arrival_time[0]) == str(_date_in_YYMMDD) and str(arrival_time[1]) == str(_time_in_HHMM):
                                        busy_gate_list.append(str(arriving_gate))

                elif origin == "Ciudad de Mexico - MEXICO" and str(departure_gate) not in available_gate_list:
                                available_gate_list.append(str(departure_gate))

                                if str(departure_time[2]) == str(_date_in_YYMMDD) and str(departure_time[3]) == str(_time_in_HHMM):
                                        busy_gate_list.append(str(departure_gate))

        for gate in busy_gate_list:
                available_gate_list.remove(gate)

        return available_gate_list, busy_gate_list

    def count_available_seats(self):

        seats_by_plate = {}
        seats = []

        for data in AirportAD().read_passengers_file().values():
            flight = data.flight
            seat = data.seat

            if flight not in seats_by_plate.keys():
                if seat not in seats_by_plate.values():
                    seats_by_plate[flight] = [seat]

            elif flight in seats_by_plate.keys():
                if seat not in seats_by_plate.values():
                    seats_by_plate[flight] += [seat]

        return seats_by_plate

class Add:

    def add_flight(self):

        flight_file = open("data/flights.csv", "a")
        flight_data = UserAdd().ask_for_flight_info()

        for data in flight_data:
                flight_file.write(data + ",")

        flight_file.write("\n")
        flight_file.close()

    def add_traveller(self):

        traveller_file = open("data/travellers.csv", "a")
        traveller_data = UserAdd().ask_for_traveller_info()

        for data in traveller_data:
                traveller_file.write(data + ",")

        traveller_file.write("\n")
        traveller_file.close()

    def add_passenger(self):

        passenger_file = open("data/passengers.csv", "a")
        passenger_data = UserAdd().ask_for_passenger_info()

        for data in passenger_data:
                passenger_file.write(data + ",")

        passenger_file.write("\n")
        passenger_file.close()

class ModifyPilot:

    def modify_pilot_marital_status(self):

        pilot_passport, marital_status = UserInfoPilot().ask_for_pilot_info_marital_status()
        loader = AirportAD().read_pilots_file()

        try:
            passport = loader[pilot_passport].passport
            forename = loader[pilot_passport].forename
            surname = loader[pilot_passport].surname
            date_of_birth = loader[pilot_passport].date_of_birth
            country = loader[pilot_passport].country
            gender = loader[pilot_passport].gender

            my_airport = AirportAD().read_pilots_file()
            my_airport[pilot_passport].marital_status = marital_status

            pilot = Pilot(passport, forename, surname, date_of_birth, country, gender, marital_status+"\n")

            modify_pilot = {pilot_passport:pilot}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/pilots.csv", "w")
            file.write("passport,forename,surname,date of birth,country,gender,marital status\n")

            for data in data_load:
                file.write(data.passport + "," + data.forename + "," + data.surname + "," + data.date_of_birth + "," + data.country + "," + data.gender + "," + data.marital_status)
            file.close()

            print("\nPilot's marital status successfully changed!\n")

        except:
            print("\nPilot not found in file!\n")

    def go_back(self):

        pass

class ModifyAttendant:

    def modify_attendant_marital_status(self):

        attendant_passport, marital_status = UserInfoAttendant().ask_for_attendant_info_marital_status()
        loader = AirportAD().read_attendants_file()

        try:
            passport = loader[attendant_passport].passport
            forename = loader[attendant_passport].forename
            surname = loader[attendant_passport].surname
            date_of_birth = loader[attendant_passport].date_of_birth
            country = loader[attendant_passport].country
            gender = loader[attendant_passport].gender

            my_airport = AirportAD().read_attendants_file()
            my_airport[attendant_passport].marital_status = marital_status

            attendant = Attendant(passport, forename, surname, date_of_birth, country, gender, marital_status+"\n")

            modify_pilot = {attendant_passport:attendant}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/attendants.csv", "w")
            file.write("passport,forename,surname,date of birth,country,gender,marital status\n")

            for data in data_load:
                file.write(data.passport + "," + data.forename + "," + data.surname + "," + data.date_of_birth + "," + data.country + "," + data.gender + "," + data.marital_status)
            file.close()

            print("\nAttendant's marital status successfully changed!\n")

        except:
            print("\nAttendant not found in file!\n")

    def go_back(self):

        pass

class ModifyTraveller:

    def modify_traveller_marital_status(self):

        traveller_passport, marital_status = UserInfoTraveller().ask_for_traveller_info_marital_status()
        loader = AirportAD().read_travellers_file()

        try:
            passport = loader[traveller_passport].passport
            forename = loader[traveller_passport].forename
            surname = loader[traveller_passport].surname
            date_of_birth = loader[traveller_passport].date_of_birth
            country = loader[traveller_passport].country
            gender = loader[traveller_passport].gender

            my_airport = AirportAD().read_travellers_file()
            my_airport[traveller_passport].marital_status = marital_status

            traveller = Travellers(passport, forename, surname, date_of_birth, country, gender, marital_status+"\n")

            modify_pilot = {traveller_passport:traveller}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/travellers.csv", "w")
            file.write("passport,forename,surname,date of birth,country,gender,marital status\n")

            for data in data_load:
                file.write(data.passport + "," + data.forename + "," + data.surname + "," + data.date_of_birth + "," + data.country + "," + data.gender + "," + data.marital_status)
            file.close()

            print("\nTraveller's marital status successfully changed!\n")

        except:
            print("\nTraveller not found in file!\n")

    def modify_traveller_gender(self):

        traveller_passport, gender = UserInfoTraveller().ask_for_traveller_info_gender()
        loader = AirportAD().read_travellers_file()

        try:
            passport = loader[traveller_passport].passport
            forename = loader[traveller_passport].forename
            surname = loader[traveller_passport].surname
            date_of_birth = loader[traveller_passport].date_of_birth
            country = loader[traveller_passport].country
            marital_status = loader[traveller_passport].marital_status

            my_airport = AirportAD().read_travellers_file()
            my_airport[traveller_passport].gender = gender

            traveller = Travellers(passport, forename, surname, date_of_birth, country, gender, marital_status)

            modify_pilot = {traveller_passport:traveller}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/travellers.csv", "w")
            file.write("passport,forename,surname,date of birth,country,gender,marital status\n")

            for data in data_load:
                file.write(data.passport + "," + data.forename + "," + data.surname + "," + data.date_of_birth + "," + data.country + "," + data.gender + "," + data.marital_status)
            file.close()

            print("\nTraveller's gender successfully changed!\n")

        except:
            print("\nTraveller not found in file!\n")

    def modify_traveller_birth_date(self):

        traveller_passport, date_of_birth = UserInfoTraveller().ask_for_traveller_info_birth_date()
        loader = AirportAD().read_travellers_file()

        try:
            passport = loader[traveller_passport].passport
            forename = loader[traveller_passport].forename
            surname = loader[traveller_passport].surname
            country = loader[traveller_passport].country
            gender = loader[traveller_passport].gender
            marital_status = loader[traveller_passport].marital_status

            my_airport = AirportAD().read_travellers_file()
            my_airport[traveller_passport].date_of_birth = date_of_birth

            traveller = Travellers(passport, forename, surname, date_of_birth, country, gender, marital_status)

            modify_pilot = {traveller_passport:traveller}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/travellers.csv", "w")
            file.write("passport,forename,surname,date of birth,country,gender,marital status\n")

            for data in data_load:
                file.write(data.passport + "," + data.forename + "," + data.surname + "," + data.date_of_birth + "," + data.country + "," + data.gender + "," + data.marital_status)
            file.close()

            print("\nTraveller's forename successfully changed!\n")

        except:
            print("\nTraveller not found in file!\n")

    def modify_traveller_forename(self):

        traveller_passport, forename = UserInfoTraveller().ask_for_traveller_info_forename()
        loader = AirportAD().read_travellers_file()

        try:
            passport = loader[traveller_passport].passport
            surname = loader[traveller_passport].surname
            date_of_birth = loader[traveller_passport].date_of_birth
            country = loader[traveller_passport].country
            gender = loader[traveller_passport].gender
            marital_status = loader[traveller_passport].marital_status

            my_airport = AirportAD().read_travellers_file()
            my_airport[traveller_passport].forename = forename

            traveller = Travellers(passport, forename, surname, date_of_birth, country, gender, marital_status)

            modify_pilot = {traveller_passport:traveller}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/travellers.csv", "w")
            file.write("passport,forename,surname,date of birth,country,gender,marital status\n")

            for data in data_load:
                file.write(data.passport + "," + data.forename + "," + data.surname + "," + data.date_of_birth + "," + data.country + "," + data.gender + "," + data.marital_status)
            file.close()

            print("\nTraveller's forename successfully changed!\n")

        except:
            print("\nTraveller not found in file!\n")

    def modify_traveller_surname(self):

        traveller_passport, surname = UserInfoTraveller().ask_for_traveller_info_surname()
        loader = AirportAD().read_travellers_file()

        try:
            passport = loader[traveller_passport].passport
            forename = loader[traveller_passport].forename
            date_of_birth = loader[traveller_passport].date_of_birth
            country = loader[traveller_passport].country
            gender = loader[traveller_passport].gender
            marital_status = loader[traveller_passport].marital_status

            my_airport = AirportAD().read_travellers_file()
            my_airport[traveller_passport].surname = surname

            traveller = Travellers(passport, forename, surname, date_of_birth, country, gender, marital_status)

            modify_pilot = {traveller_passport:traveller}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/travellers.csv", "w")
            file.write("passport,forename,surname,date of birth,country,gender,marital status\n")

            for data in data_load:
                file.write(data.passport + "," + data.forename + "," + data.surname + "," + data.date_of_birth + "," + data.country + "," + data.gender + "," + data.marital_status)
            file.close()

            print("\nTraveller's surname successfully changed!\n")

        except:
            print("\nTraveller not found in file!\n")

    def go_back(self):

        pass

class ModifyPassenger:

    def modify_passenger_seat(self):

        passenger_flight, passenger_passport, seat = UserInfoPassenger().ask_for_passenger_info_seat()
        seats_by_plate = Check().count_available_seats()
        loader = AirportAD().read_passengers_file()

        if seat not in seats_by_plate[passenger_flight]:

            try:
                flight = loader[passenger_flight + passenger_passport].flight
                passport = loader[passenger_flight + passenger_passport].passport
                flight_class = loader[passenger_flight + passenger_passport].flight_class
                location = loader[passenger_flight + passenger_passport].location

                my_airport = AirportAD().read_passengers_file()
                my_airport[passenger_flight + passenger_passport].seat = seat

                passenger = Passengers(flight, passport, flight_class, seat, location)

                modify_pilot = {passenger_flight + passenger_passport:passenger}
                data_modify = my_airport
                data_modify.update(modify_pilot)
                data_load = data_modify.values()

                file = open("data/passengers.csv", "w")
                file.write("flight,passport,class,seat,location\n")

                for data in data_load:
                    file.write(data.flight + "," + data.passport + "," + data.flight_class + "," + data.seat + "," + data.location)
                file.close()

                print("\nPassenger's seat successfully changed!\n")

            except:
                print("\nPassenger not found in file!\n")

        else:

            print("\nThis seat is already taken!\n")

    def modify_passenger_flight_class(self):

        passenger_flight, passenger_passport, flight_class = UserInfoPassenger().ask_for_passenger_info_flight_class()
        loader = AirportAD().read_passengers_file()

        try:
            flight = loader[passenger_flight + passenger_passport].flight
            passport = loader[passenger_flight + passenger_passport].passport
            seat = loader[passenger_flight + passenger_passport].seat
            location = loader[passenger_flight + passenger_passport].location

            my_airport = AirportAD().read_passengers_file()
            my_airport[passenger_flight + passenger_passport].flight_class = flight_class

            passenger = Passengers(flight, passport, flight_class, seat, location)

            modify_pilot = {passenger_flight + passenger_passport:passenger}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/passengers.csv", "w")
            file.write("flight,passport,class,seat,location\n")

            for data in data_load:
                file.write(data.flight + "," + data.passport + "," + data.flight_class + "," + data.seat + "," + data.location)
            file.close()

            print("\nPassenger's flight class successfully changed!\n")

        except:
            print("\nPassenger not found in file!\n")

    def modify_passenger_check_point_location(self):

        passenger_flight, passenger_passport, check_point = UserInfoPassenger().ask_for_passenger_info_check_point()
        loader = AirportAD().read_passengers_file()

        try:
            check_point_plus_line = check_point + "\n"

            flight = loader[passenger_flight + passenger_passport].flight
            passport = loader[passenger_flight + passenger_passport].passport
            flight_class = loader[passenger_flight + passenger_passport].flight_class
            seat = loader[passenger_flight + passenger_passport].seat

            my_airport = AirportAD().read_passengers_file()
            my_airport[passenger_flight + passenger_passport].location = check_point_plus_line

            passenger = Passengers(flight, passport, flight_class, seat, check_point_plus_line)

            modify_pilot = {passenger_flight + passenger_passport:passenger}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/passengers.csv", "w")
            file.write("flight,passport,class,seat,location\n")

            for data in data_load:
                file.write(data.flight + "," + data.passport + "," + data.flight_class + "," + data.seat + "," + data.location)
            file.close()

            print("\nPassenger's check point location successfully changed!\n")

        except:
            print("\nPassenger not found in file!\n")

    def go_back(self):

        pass

class ModifyFlight:

    def modify_flight_status(self):

        flight_id, flight_plate, flight_status = UserInfoFlight().ask_for_flight_info_status()
        loader = AirportAD().read_flights_file()

        try:
            id = loader[flight_id + flight_plate].id
            plate = loader[flight_id + flight_plate].plate
            origin = loader[flight_id + flight_plate].origin
            destiny = loader[flight_id + flight_plate].destiny
            departure = loader[flight_id + flight_plate].departure
            arriving = loader[flight_id + flight_plate].arriving
            departure_gate = loader[flight_id + flight_plate].departure_gate
            take_off_track = loader[flight_id + flight_plate].take_off_track
            arriving_gate = loader[flight_id + flight_plate].arriving_gate
            landing_track = loader[flight_id + flight_plate].landing_track
            pilot = loader[flight_id + flight_plate].pilot
            copilot = loader[flight_id + flight_plate].copilot
            attendants = loader[flight_id + flight_plate].attendants

            my_airport = AirportAD().read_flights_file()
            my_airport[flight_id + flight_plate].status = flight_status

            flight = Flights(id, plate, origin, destiny, departure, arriving, flight_status, departure_gate, take_off_track, arriving_gate, landing_track, pilot, copilot, attendants)

            modify_pilot = {flight_id + flight_plate:flight}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/flights.csv", "w")
            file.write("id,plate,origin,destiny,departure,arriving,status,departure gate,take off track,arriving gate,landing track,pilot,copilot,attendants\n")

            for data in data_load:
                file.write(data.id + "," + data.plate + "," + data.origin + "," + data.destiny + "," + data.departure + "," + data.arriving + "," + data.status + "," + data.departure_gate + "," + data.take_off_track + "," + data.arriving_gate + "," + data.landing_track + "," + data.pilot + "," + data.copilot + "," + data.attendants)
            file.close()

            print("\nFlight's status successfully changed!\n")

        except:
            print("\nFlight not found in file!\n")

    def modify_flight_departure_gate(self):

        flight_id, flight_plate, flight_departure_gate = UserInfoFlight().ask_for_flight_info_departure_gate()
        loader = AirportAD().read_flights_file()

        try:
            id = loader[flight_id + flight_plate].id
            plate = loader[flight_id + flight_plate].plate
            origin = loader[flight_id + flight_plate].origin
            destiny = loader[flight_id + flight_plate].destiny
            departure = loader[flight_id + flight_plate].departure
            arriving = loader[flight_id + flight_plate].arriving
            status = loader[flight_id + flight_plate].status
            take_off_track = loader[flight_id + flight_plate].take_off_track
            arriving_gate = loader[flight_id + flight_plate].arriving_gate
            landing_track = loader[flight_id + flight_plate].landing_track
            pilot = loader[flight_id + flight_plate].pilot
            copilot = loader[flight_id + flight_plate].copilot
            attendants = loader[flight_id + flight_plate].attendants

            my_airport = AirportAD().read_flights_file()
            my_airport[flight_id + flight_plate].departure_gate = flight_departure_gate

            flight = Flights(id, plate, origin, destiny, departure, arriving, status, flight_departure_gate, take_off_track, arriving_gate, landing_track, pilot, copilot, attendants)

            modify_pilot = {flight_id + flight_plate:flight}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/flights.csv", "w")
            file.write("id,plate,origin,destiny,departure,arriving,status,departure gate,take off track,arriving gate,landing track,pilot,copilot,attendants\n")

            for data in data_load:
                file.write(data.id + "," + data.plate + "," + data.origin + "," + data.destiny + "," + data.departure + "," + data.arriving + "," + data.status + "," + data.departure_gate + "," + data.take_off_track + "," + data.arriving_gate + "," + data.landing_track + "," + data.pilot + "," + data.copilot + "," + data.attendants)
            file.close()

            print("\nFlight's departure gate successfully changed!\n")

        except:
            print("\nFlight not found in file!\n")

    def modify_flight_arrival_gate(self):

        flight_id, flight_plate, flight_arrival_gate = UserInfoFlight().ask_for_flight_info_arrival_gate()
        loader = AirportAD().read_flights_file()

        try:
            id = loader[flight_id + flight_plate].id
            plate = loader[flight_id + flight_plate].plate
            origin = loader[flight_id + flight_plate].origin
            destiny = loader[flight_id + flight_plate].destiny
            departure = loader[flight_id + flight_plate].departure
            arriving = loader[flight_id + flight_plate].arriving
            status = loader[flight_id + flight_plate].status
            departure_gate = loader[flight_id + flight_plate].departure_gate
            take_off_track = loader[flight_id + flight_plate].take_off_track
            landing_track = loader[flight_id + flight_plate].landing_track
            pilot = loader[flight_id + flight_plate].pilot
            copilot = loader[flight_id + flight_plate].copilot
            attendants = loader[flight_id + flight_plate].attendants

            my_airport = AirportAD().read_flights_file()
            my_airport[flight_id + flight_plate].arriving_gate = flight_arrival_gate

            flight = Flights(id, plate, origin, destiny, departure, arriving, status, departure_gate, take_off_track, flight_arrival_gate, landing_track, pilot, copilot, attendants)

            modify_pilot = {flight_id + flight_plate:flight}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/flights.csv", "w")
            file.write("id,plate,origin,destiny,departure,arriving,status,departure gate,take off track,arriving gate,landing track,pilot,copilot,attendants\n")

            for data in data_load:
                file.write(data.id + "," + data.plate + "," + data.origin + "," + data.destiny + "," + data.departure + "," + data.arriving + "," + data.status + "," + data.departure_gate + "," + data.take_off_track + "," + data.arriving_gate + "," + data.landing_track + "," + data.pilot + "," + data.copilot + "," + data.attendants)
            file.close()

            print("\nFlight's arrival gate successfully changed!\n")

        except:
            print("\nFlight not found in file!\n")

    def modify_flight_take_off_track(self):

        flight_id, flight_plate, flight_take_off_track = UserInfoFlight().ask_for_flight_info_take_off_track()
        loader = AirportAD().read_flights_file()

        try:
            id = loader[flight_id + flight_plate].id
            plate = loader[flight_id + flight_plate].plate
            origin = loader[flight_id + flight_plate].origin
            destiny = loader[flight_id + flight_plate].destiny
            departure = loader[flight_id + flight_plate].departure
            arriving = loader[flight_id + flight_plate].arriving
            status = loader[flight_id + flight_plate].status
            departure_gate = loader[flight_id + flight_plate].departure_gate
            arriving_gate = loader[flight_id + flight_plate].arriving_gate
            landing_track = loader[flight_id + flight_plate].landing_track
            pilot = loader[flight_id + flight_plate].pilot
            copilot = loader[flight_id + flight_plate].copilot
            attendants = loader[flight_id + flight_plate].attendants

            my_airport = AirportAD().read_flights_file()
            my_airport[flight_id + flight_plate].take_off_track = flight_take_off_track

            flight = Flights(id, plate, origin, destiny, departure, arriving, status, departure_gate, flight_take_off_track, arriving_gate, landing_track, pilot, copilot, attendants)

            modify_pilot = {flight_id + flight_plate:flight}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/flights.csv", "w")
            file.write("id,plate,origin,destiny,departure,arriving,status,departure gate,take off track,arriving gate,landing track,pilot,copilot,attendants\n")

            for data in data_load:
                file.write(data.id + "," + data.plate + "," + data.origin + "," + data.destiny + "," + data.departure + "," + data.arriving + "," + data.status + "," + data.departure_gate + "," + data.take_off_track + "," + data.arriving_gate + "," + data.landing_track + "," + data.pilot + "," + data.copilot + "," + data.attendants)
            file.close()

            print("\nFlight's take off track successfully changed!\n")

        except:
            print("\nFlight not found in file!\n")

    def modify_flight_landing_track(self):

        flight_id, flight_plate, flight_landing_track = UserInfoFlight().ask_for_flight_info_landing_track()
        loader = AirportAD().read_flights_file()

        try:
            id = loader[flight_id + flight_plate].id
            plate = loader[flight_id + flight_plate].plate
            origin = loader[flight_id + flight_plate].origin
            destiny = loader[flight_id + flight_plate].destiny
            departure = loader[flight_id + flight_plate].departure
            arriving = loader[flight_id + flight_plate].arriving
            status = loader[flight_id + flight_plate].status
            departure_gate = loader[flight_id + flight_plate].departure_gate
            take_off_track = loader[flight_id + flight_plate].take_off_track
            arriving_gate = loader[flight_id + flight_plate].arriving_gate
            pilot = loader[flight_id + flight_plate].pilot
            copilot = loader[flight_id + flight_plate].copilot
            attendants = loader[flight_id + flight_plate].attendants

            my_airport = AirportAD().read_flights_file()
            my_airport[flight_id + flight_plate].take_off_track = flight_landing_track

            flight = Flights(id, plate, origin, destiny, departure, arriving, status, departure_gate, take_off_track, arriving_gate, flight_landing_track, pilot, copilot, attendants)

            modify_pilot = {flight_id + flight_plate:flight}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/flights.csv", "w")
            file.write("id,plate,origin,destiny,departure,arriving,status,departure gate,take off track,arriving gate,landing track,pilot,copilot,attendants\n")

            for data in data_load:
                file.write(data.id + "," + data.plate + "," + data.origin + "," + data.destiny + "," + data.departure + "," + data.arriving + "," + data.status + "," + data.departure_gate + "," + data.take_off_track + "," + data.arriving_gate + "," + data.landing_track + "," + data.pilot + "," + data.copilot + "," + data.attendants)
            file.close()

            print("\nFlight's landing track successfully changed!\n")

        except:
            print("\nFlight not found in file!\n")

    def modify_flight_pilot(self):

        flight_id, flight_plate, flight_pilot = UserInfoFlight().ask_for_flight_info_pilot()
        loader = AirportAD().read_flights_file()

        try:
            id = loader[flight_id + flight_plate].id
            plate = loader[flight_id + flight_plate].plate
            origin = loader[flight_id + flight_plate].origin
            destiny = loader[flight_id + flight_plate].destiny
            departure = loader[flight_id + flight_plate].departure
            arriving = loader[flight_id + flight_plate].arriving
            status = loader[flight_id + flight_plate].status
            departure_gate = loader[flight_id + flight_plate].departure_gate
            take_off_track = loader[flight_id + flight_plate].take_off_track
            arriving_gate = loader[flight_id + flight_plate].arriving_gate
            landing_track = loader[flight_id + flight_plate].landing_track
            copilot = loader[flight_id + flight_plate].copilot
            attendants = loader[flight_id + flight_plate].attendants

            my_airport = AirportAD().read_flights_file()
            my_airport[flight_id + flight_plate].pilot = flight_pilot

            flight = Flights(id, plate, origin, destiny, departure, arriving, status, departure_gate, take_off_track, arriving_gate, landing_track, flight_pilot, copilot, attendants)

            modify_pilot = {flight_id + flight_plate:flight}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/flights.csv", "w")
            file.write("id,plate,origin,destiny,departure,arriving,status,departure gate,take off track,arriving gate,landing track,pilot,copilot,attendants\n")

            for data in data_load:
                file.write(data.id + "," + data.plate + "," + data.origin + "," + data.destiny + "," + data.departure + "," + data.arriving + "," + data.status + "," + data.departure_gate + "," + data.take_off_track + "," + data.arriving_gate + "," + data.landing_track + "," + data.pilot + "," + data.copilot + "," + data.attendants)
            file.close()

            print("\nFlight's pilot successfully changed!\n")

        except:
            print("\nFlight not found in file!\n")

    def modify_flight_copilot(self):

        flight_id, flight_plate, flight_copilot = UserInfoFlight().ask_for_flight_info_copilot()
        loader = AirportAD().read_flights_file()

        try:
            id = loader[flight_id + flight_plate].id
            plate = loader[flight_id + flight_plate].plate
            origin = loader[flight_id + flight_plate].origin
            destiny = loader[flight_id + flight_plate].destiny
            departure = loader[flight_id + flight_plate].departure
            arriving = loader[flight_id + flight_plate].arriving
            status = loader[flight_id + flight_plate].status
            departure_gate = loader[flight_id + flight_plate].departure_gate
            take_off_track = loader[flight_id + flight_plate].take_off_track
            arriving_gate = loader[flight_id + flight_plate].arriving_gate
            landing_track = loader[flight_id + flight_plate].landing_track
            pilot = loader[flight_id + flight_plate].pilot
            attendants = loader[flight_id + flight_plate].attendants

            my_airport = AirportAD().read_flights_file()
            my_airport[flight_id + flight_plate].copilot = flight_copilot

            flight = Flights(id, plate, origin, destiny, departure, arriving, status, departure_gate, take_off_track, arriving_gate, landing_track, pilot, flight_copilot, attendants)

            modify_pilot = {flight_id + flight_plate:flight}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/flights.csv", "w")
            file.write("id,plate,origin,destiny,departure,arriving,status,departure gate,take off track,arriving gate,landing track,pilot,copilot,attendants\n")

            for data in data_load:
                file.write(data.id + "," + data.plate + "," + data.origin + "," + data.destiny + "," + data.departure + "," + data.arriving + "," + data.status + "," + data.departure_gate + "," + data.take_off_track + "," + data.arriving_gate + "," + data.landing_track + "," + data.pilot + "," + data.copilot + "," + data.attendants)
            file.close()

            print("\nFlight's copilot successfully changed!\n")

        except:
            print("\nFlight not found in file!\n")

    def modify_flight_attendants(self):

        flight_id, flight_plate, flight_attendants = UserInfoFlight().ask_for_flight_info_attendants()
        loader = AirportAD().read_flights_file()

        try:
            flight_attendants_plus_line = flight_attendants + "\n"

            id = loader[flight_id + flight_plate].id
            plate = loader[flight_id + flight_plate].plate
            origin = loader[flight_id + flight_plate].origin
            destiny = loader[flight_id + flight_plate].destiny
            departure = loader[flight_id + flight_plate].departure
            arriving = loader[flight_id + flight_plate].arriving
            status = loader[flight_id + flight_plate].status
            departure_gate = loader[flight_id + flight_plate].departure_gate
            take_off_track = loader[flight_id + flight_plate].take_off_track
            arriving_gate = loader[flight_id + flight_plate].arriving_gate
            landing_track = loader[flight_id + flight_plate].landing_track
            pilot = loader[flight_id + flight_plate].pilot
            copilot = loader[flight_id + flight_plate].copilot

            my_airport = AirportAD().read_flights_file()
            my_airport[flight_id + flight_plate].attendants = flight_attendants_plus_line

            flight = Flights(id, plate, origin, destiny, departure, arriving, status, departure_gate, take_off_track, arriving_gate, landing_track, pilot, copilot, flight_attendants_plus_line)

            modify_pilot = {flight_id + flight_plate:flight}
            data_modify = my_airport
            data_modify.update(modify_pilot)
            data_load = data_modify.values()

            file = open("data/flights.csv", "w")
            file.write("id,plate,origin,destiny,departure,arriving,status,departure gate,take off track,arriving gate,landing track,pilot,copilot,attendants\n")

            for data in data_load:
                file.write(data.id + "," + data.plate + "," + data.origin + "," + data.destiny + "," + data.departure + "," + data.arriving + "," + data.status + "," + data.departure_gate + "," + data.take_off_track + "," + data.arriving_gate + "," + data.landing_track + "," + data.pilot + "," + data.copilot + "," + data.attendants)
            file.close()

            print("\nFlight's attendants successfully changed!\n")

        except:
            print("\nFlight not found in file!\n")

    def go_back(self):

        pass

class Csv:

    def write_to_csv(self):

        file = open("statistics.csv", "w+")
        file.write("date, time, # of empty tracks, # of busy tracks, # passengers in check-in, # of passengers in security, # of passengers boarded, # of flights landed, # of flights departured, available gates, occupied gates")
        file.write("\n")
        file.write("," * 11)
        file.close()

        file = open("statistics.csv", "r")
        lst = list(csv.reader(file))
        file.close()

        file = open("statistics.csv", "w")
        self.compute_values(lst)
        csv.writer(file).writerows(lst)
        file.close()

    def compute_values(self, lst):

        data_check = Check()
        data_user = UserTimes()
        date = data_user.ask_for_date()
        time = data_user.ask_for_time()

        lst[1][0] = date
        lst[1][1] = time
        lst[1][2], _ = data_check.number_of_empty_tracks(date, time)
        count, flights_by_plate = data_check.number_of_empty_tracks(date, time)
        lst[1][3] =     data_check.number_of_busy_tracks(count)
        find_flights = data_check.find_flights(flights_by_plate, date, time)
        lst[1][4] = data_check.count_check_in(find_flights)
        lst[1][5] = data_check.count_security(find_flights)
        lst[1][6] = data_check.count_boarded(find_flights)
        lst[1][7] = data_check.count_flights_off(find_flights)
        lst[1][8] = data_check.count_flights_taken_in(find_flights)
        lst[1][9],lst[1][10] = data_check.count_available_and_busy_gates(date, time)

class ExecuteMenus:

    def execute_menu(self, _option):

        add = Add()
        menu = Menu()

        display_menu = {
        1: Csv().write_to_csv,
        2: add.add_flight,
        3: add.add_traveller,
        4: add.add_passenger,
        5: menu.pilot_menu,
        6: menu.attendant_menu,
        7: menu.traveller_menu,
        8: menu.passenger_menu,
        9: menu.flight_menu,
        0: sys.exit
        }

        display_menu[_option]()

    def execute_pilot(self, _option):

        modify = ModifyPilot()

        pilot_menu = {
        1: modify.modify_pilot_marital_status,
        0: modify.go_back
        }

        pilot_menu[_option]()

    def execute_attendant(self, _option):

        modify = ModifyAttendant()

        attendant_menu = {
        1: modify.modify_attendant_marital_status,
        0: modify.go_back
        }

        attendant_menu[_option]()

    def execute_traveller(self, _option):

        modify = ModifyTraveller()

        traveller_menu = {
        1: modify.modify_traveller_marital_status,
        2: modify.modify_traveller_gender,
        3: modify.modify_traveller_birth_date,
        4: modify.modify_traveller_forename,
        5: modify.modify_traveller_surname,
        0: modify.go_back
        }

        traveller_menu[_option]()

    def execute_passenger(self, _option):

        modify = ModifyPassenger()

        passenger_menu = {
        1: modify.modify_passenger_seat,
        2: modify.modify_passenger_flight_class,
        3: modify.modify_passenger_check_point_location,
        0: modify.go_back
        }

        passenger_menu[_option]()

    def execute_flight(self, _option):

        modify = ModifyFlight()
        menu = Menu()

        flight_menu = {
        1: modify.modify_flight_status,
        2: modify.modify_flight_departure_gate,
        3: modify.modify_flight_arrival_gate,
        4: modify.modify_flight_take_off_track,
        5: modify.modify_flight_landing_track,
        6: menu.crew_menu,
        0: modify.go_back
        }

        flight_menu[_option]()

    def execute_crew(self, _option):

        modify = ModifyFlight()

        crew_menu = {
        1: modify.modify_flight_pilot,
        2: modify.modify_flight_copilot,
        3: modify.modify_flight_attendants,
        0: modify.go_back
        }

        crew_menu[_option]()
