class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passengers(self, name):
        if not self.available_seats():
            return False
        else:
            self.passengers.append(name)
            return True
    
    def available_seats(self):
        return self.capacity - len(self.passengers)