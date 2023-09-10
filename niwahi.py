# Sample Python code for a ride-sharing platform

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class Driver(User):
    def __init__(self, name, email, password, car_details):
        super().__init__(name, email, password)
        self.car_details = car_details
        self.available = True

    def offer_ride(self, destination, seats_available, fare):
        return {
            'driver': self,
            'destination': destination,
            'seats_available': seats_available,
            'fare': fare
        }

class Passenger(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0

    def request_ride(self, driver, destination, passengers):
        if driver.available and driver.seats_available >= passengers:
            fare = driver.fare * passengers
            if self.balance >= fare:
                self.balance -= fare
                driver.available = False
                driver.seats_available -= passengers
                return f'Ride to {destination} confirmed!'
            else:
                return 'Insufficient balance'
        else:
            return 'Ride not available'

# Example usage:

driver1 = Driver('Felix Barmatey', 'john@example.com', 'driverpass', {
    'car_model': 'Toyota Prado',
    'plate_number': 'KAU 891J'
})
driver1.fare = 1000  # Set fare per passenger
driver1.seats_available = 4

passenger1 = Passenger('Alice', 'alice@example.com', 'passengerpass')
passenger1.balance = 1500

ride_request = passenger1.request_ride(driver1, 'Nairobi', 3)
print(ride_request)

print(f'Driver: {driver1.name}, Available Seats: {driver1.seats_available}')
print(f'Passenger: {passenger1.name}, Balance: {passenger1.balance}')
