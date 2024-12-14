from datetime import datetime

class Flight:
    def __init__(self, flight_number, departure_city, arrival_city, departure_time, arrival_time, seats):
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = datetime.strptime(departure_time, "%Y-%m-%d %H:%M")
        self.arrival_time = datetime.strptime(arrival_time, "%Y-%m-%d %H:%M")
        self.seats = seats
        self.booked_seats = 0

    def calculate_duration(self):
        return (self.arrival_time - self.departure_time).total_seconds() // 3600

    def check_availability(self):
        return self.seats > self.booked_seats

    def book_seat(self):
        if self.check_availability():
            self.booked_seats += 1
            return True
        return False

    def display_flight_info(self):
        return (f"Рейс: {self.flight_number}\n"
                f"Пункт отправления: {self.departure_city}\n"
                f"Пункт прибытия: {self.arrival_city}\n"
                f"Время отправления: {self.departure_time.strftime('%Y-%m-%d %H:%M')}\n"
                f"Время прибытия: {self.arrival_time.strftime('%Y-%m-%d %H:%M')}\n"
                f"Свободные места: {self.seats - self.booked_seats}\n"
                f"Продолжительность: {self.calculate_duration()} часов")


class User:
    def __init__(self, username, last_name, passport_id, phone_number):
        self.username = username
        self.last_name = last_name
        self.passport_id = passport_id
        self.phone_number = phone_number
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)

    def display_profile(self):
        return (f"Имя: {self.username}\n"
                f"Фамилия: {self.last_name}\n"
                f"Паспорт номера: {self.passport_id}\n"
                f"Телефон: {self.phone_number}")


class Booking:
    def __init__(self, user, flight):
        self.user = user
        self.flight = flight

    def create_booking(self):
        if self.flight.book_seat():
            return f"Бронирование успешно для {self.user.username} на рейс {self.flight.flight_number}."
        return f"Нет доступных мест на рейсе {self.flight.flight_number}."



class Trip:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        for existing_flight in self.flights:
            if self._flights_overlap(existing_flight, flight):
                return f"Ошибка: Рейсы {existing_flight.flight_number} и {flight.flight_number} пересекаются по времени."
        self.flights.append(flight)
        return f"Рейс {flight.flight_number} успешно добавлен в путешествие."

    def _flights_overlap(self, flight1, flight2):
        return not (flight1.arrival_time <= flight2.departure_time or flight2.arrival_time <= flight1.departure_time)

    def display_trip_info(self):
        if not self.flights:
            return "Путешествие не содержит рейсов."
        info = "Рейсы в путешествии:\n"
        for flight in self.flights:
            info += flight.display_flight_info() + "\n"
        return info

if __name__ == '__main__':
    flight1 = Flight("A101", "Бишкек", "Ош", "2024-12-20 09:00", "2024-12-20 11:00", 100)
    flight2 = Flight("A102", "Бишкек", "Ош", "2024-12-20  15:00", "2024-12-20 17:00", 50)
    
    flights = [flight1, flight2]
    trip = Trip()
    
    registered_users = []
    
    print("Добро пожаловать в систему бронирования путешествий!\n")
    
    while True:
        print("1. Получить информацию о рейсах\n"
              "2. Забронировать билет\n"
              "3. Получить список зарегистрированных пользователей\n"
              "4. Создать путешествие\n"
              "5. Получить информацию о добавленных рейсах\n"
              "6. Получить информацию о рейсе по времени отправления\n"
              "7. Выйти\n")
        try:
            command = input("Выберите операцию:\n")
            
            if command == "1":
                for flight in flights:
                    print(flight.display_flight_info())
                print(trip.display_trip_info())
            
            elif command == "2":
                username = input("Введите имя: ")
                last_name = input("Введите фамилию: ")
                passport_id = input("Введите номер паспорта: ")
                phone_number = input("Введите номер телефона: ")

                user = User(username, last_name, passport_id, phone_number)
                registered_users.append(user)  # Добавляем пользователя в список зарегистрированных
                print("\nДоступные рейсы:")
                all_flights = flights + trip.flights
                
                for i, flight in enumerate(all_flights, 1):
                    print(f"{i}. {flight.flight_number}: {flight.departure_city} -> {flight.arrival_city}, "
                          f"{flight.departure_time.strftime('%Y-%m-%d %H:%M')} - "
                          f"{flight.arrival_time.strftime('%Y-%m-%d %H:%M')}, "
                          f"Свободные места: {flight.seats - flight.booked_seats}")
                
                try:
                    flight_choice = int(input("\nТандалган рейстин номерин киргизиңиз: ")) - 1
                    if flight_choice < 0 or flight_choice >= len(all_flights):
                        raise ValueError("Неверный номер рейса.")
                    chosen_flight = all_flights[flight_choice]
                    booking_instance = Booking(user, chosen_flight)
                    result = booking_instance.create_booking()
                    user.add_booking(booking_instance)
                    print(result)
                except ValueError as e:
                    print(f"Ошибка: {e}. Пожалуйста, введите корректный номер рейса.")

            elif command == "3":
                print("\nСписок зарегистрированных пользователей:")
                for user in registered_users:
                    print(user.display_profile())
                    print("Забронированные билеты:")
                    for booking in user.bookings:
                        print("___________")
                        print(booking.flight.display_flight_info())
                        print("----------")

            elif command == "4":             
                while True:
                    flight_number = input("Введите номер рейса (или 'выход' для завершения): ")
                    if flight_number.lower() == 'выход':
                        break
                    departure_city = input("Введите пункт отправления: ")
                    arrival_city = input("Введите пункт прибытия: ")
                    departure_time = input("Введите время отправления (YYYY-MM-DD HH:MM): ")
                    arrival_time = input("Введите время прибытия (YYYY-MM-DD HH:MM): ")
                    seats = int(input("Введите количество мест: "))
                    
                    try:
                        new_flight = Flight(flight_number, departure_city, arrival_city, departure_time, arrival_time, seats)
                        result = trip.add_flight(new_flight)
                        print(result)
                        print(trip.display_trip_info())
                    except ValueError as e:
                        print(f"Ошибка: {e}. Пожалуйста, введите корректные данные.")

            elif command == "5":
                print(trip.display_trip_info())
                print("----------")
                
            elif command == "6":
                flight_number = input("Введите номер рейса: ")
                departure_time_str = input("Введите время отправления (YYYY-MM-DD HH:MM): ")
                

                try:
                    departure_time = datetime.strptime(departure_time_str, "%Y-%m-%d %H:%M")
                except ValueError:
                    print("Ошибка: Неверный формат времени. Пожалуйста, используйте формат YYYY-MM-DD HH:MM.")
                    continue

            
                found_flight = None
                all_flights = flights + trip.flights 
                for flight in all_flights:
                    if flight.flight_number == flight_number and flight.departure_time == departure_time:
                        found_flight = flight
                        break


                if found_flight:
                    print("___________")
                    print("Рейс найден:", found_flight.display_flight_info())
                    print("----------")
                else:
                    print("___________")
                    print("Рейс не найден.")

            elif command == "7":
                print("Спасибо за использование. До свидания!")
                break
        except ValueError as e:
            print(f"Ошибка: {e}. Пожалуйста, попробуйте снова.")