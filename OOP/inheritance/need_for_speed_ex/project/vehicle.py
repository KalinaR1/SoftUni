class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kms):
        to_be_driven = kms * self.fuel_consumption
        if self.fuel - to_be_driven >= 0:
            self.fuel -= to_be_driven



