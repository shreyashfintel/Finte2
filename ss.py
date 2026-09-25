class Vehicle:
    def __init__(self, brand: str, model: str, wheels: int):
        self.brand = brand
        self.model = model
        self.wheels = wheels

    def display_details(self):
        print(f"Vehicle: {self.brand} {self.model}")
        print(f"Wheels : {self.wheels}")


class TwoWheeler(Vehicle):
    def __init__(self, brand: str, model: str, has_abs: bool = True):
        super().__init__(brand, model, wheels=2)
        self.has_abs = has_abs

    def display_details(self):
        super().display_details()
        print(f"ABS    : {'Yes' if self.has_abs else 'No'}\n")


class ThreeWheeler(Vehicle):
    def __init__(self, brand: str, model: str, fuel_type: str = "CNG"):
        super().__init__(brand, model, wheels=3)
        self.fuel_type = fuel_type

    def display_details(self):
        super().display_details()
        print(f"Fuel   : {self.fuel_type}\n")


class FourWheeler(Vehicle):
    def __init__(self, brand: str, model: str, seating_capacity: int = 5):
        super().__init__(brand, model, wheels=4)
        self.seating_capacity = seating_capacity

    def display_details(self):
        super().display_details()
        print(f"Seats  : {self.seating_capacity}\n")


if __name__ == "__main__":
    bike = TwoWheeler("Royal Enfield", "Hunter 350", has_abs=True)
    auto = ThreeWheeler("Bajaj", "Compact RE", fuel_type="CNG")
    car = FourWheeler("Tata", "Nexon", seating_capacity=5)

    vehicles = [bike, auto, car]

    for v in vehicles:
        v.display_details()