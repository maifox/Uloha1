from math import ceil

class Locality:
    def __init__(self, name: str, locality_coefficient: float):
        self.name = name
        self.locality_coefficient  = locality_coefficient

class Property:
    def __init__(self, locality: Locality):
        self.locality = locality

# Koeficienty pro různé typy pozemků
estate_coefficients = {
    "land": 0.85,          # zemědělský pozemek
    "building site": 9.0,  # stavební pozemek
    "forrest": 0.35,       # les
    "garden": 2.0          # zahrada
    }
class Estate(Property):
    def __init__(self, locality: Locality, estate_type: str, area: float):
        # Zavolá __init__ třídy Property
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
        # Výpočet daně pro pozemek: plocha pozemku * koeficient dle typu pozemku (atribut estate_type) * místní koeficient
        tax = ceil(self.area*estate_coefficients[self.estate_type]*self.locality.locality_coefficient)
        return tax

class Residence(Property):
    def __init__(self, locality: Locality, area: float, commercial: bool = False):
        # Zavolá __init__ třídy Property
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    def calculate_tax(self):
        commercial_index = 1
        if self.commercial:
            commercial_index *= 2 # Pro podnikání je daň dvojnásobná
        # Výpočet daně pro pozemek: podlahová plocha * koeficient lokality * 15 (* 2 pokud je daň je dvojnásobná).
        tax = ceil(self.area*self.locality.locality_coefficient*15*commercial_index)
        return tax

# Testovací výpisy
print (Estate (Locality ("Manětín", 0.8), "land", 900).calculate_tax())
print (Residence(Locality ("Manětín", 0.8), 120).calculate_tax())
print (Residence(Locality ("Brno", 3), 90, commercial=True).calculate_tax())
