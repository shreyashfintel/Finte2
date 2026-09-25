class Vehicle:
    def __init__(self, brand: str, model: str, wheels: int):
        self.brand = brand
        self.model = model
        self.wheels = wheels

    def get_info(self):
        return f"{self.brand} {self.model} ({self.wheels}-wheeler)"


class TwoWheeler(Vehicle):
    def __init__(self, brand: str, model: str, engine_cc: int):
        super().__init__(brand, model, wheels=2)
        self.engine_cc = engine_cc

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | Engine: {self.engine_cc}cc"


class ThreeWheeler(Vehicle):
    def __init__(self, brand: str, model: str, fuel_type: str):
        super().__init__(brand, model, wheels=3)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | Fuel: {self.fuel_type}"


class FourWheeler(Vehicle):
    def __init__(self, brand: str, model: str, seating_capacity: int):
        super().__init__(brand, model, wheels=4)
        self.seating_capacity = seating_capacity

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | Seating: {self.seating_capacity} passengers"


# Example Usage
if __name__ == "__main__":
    vehicles = [
        TwoWheeler("Royal Enfield", "Classic 350", engine_cc=349),
        ThreeWheeler("Bajaj", "RE Compact", fuel_type="CNG"),
        FourWheeler("Tata", "Harrier", seating_capacity=5),
    ]

    for vehicle in vehicles:
        print(vehicle.get_info())