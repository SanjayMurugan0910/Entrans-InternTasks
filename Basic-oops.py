# -----------------------------
# Basic OOP Example in Python
# -----------------------------

# Base Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand           # public attribute
        self.model = model           # public attribute
        self._speed = 0              # protected attribute
        self.__engine_no = "ENG123"  # private attribute

    # Encapsulation: controlling access to data
    def start(self):
        print(f"{self.brand} {self.model} is starting...")

    def accelerate(self, value):
        self._speed += value
        print(f"{self.brand} {self.model} speed: {self._speed} km/h")

    def get_engine_number(self):     # getter for private attribute
        return self.__engine_no


# Derived Class (Inheritance)
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)  # Call parent constructor
        self.fuel_type = fuel_type      # New attribute specific to Car

    # Polymorphism: overriding start() method
    def start(self):
        print(f"{self.brand} {self.model} ({self.fuel_type}) is starting smoothly...")


# Another Derived Class (to show polymorphism)
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model, "Electric")
        self.battery_capacity = battery_capacity

    # Override accelerate behavior
    def accelerate(self, value):
        self._speed += value
        print(f"{self.brand} {self.model} (EV) accelerating silently to {self._speed} km/h")


# -----------------------------
# Object Creation and Usage
# -----------------------------

# Creating objects
car1 = Car("Toyota", "Camry", "Petrol")
ev1 = ElectricCar("Tesla", "Model 3", "82 kWh")

# Method calls
car1.start()              # overridden method from Car
car1.accelerate(50)       # inherited method
print("Engine No:", car1.get_engine_number())

print()  # spacing

ev1.start()               # polymorphic behavior
ev1.accelerate(100)
print("Engine No:", ev1.get_engine_number())
