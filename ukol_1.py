import math
class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name   
        self.locality_coefficient = locality_coefficient    
class Property(Locality):
    def __init__(self, name, locality_coefficient, locality):
        super().__init__(name, locality_coefficient)
        self.locality= locality      
class Residence(Property):
    ESTATE_TYPE_COEFFICIENTS = {
        'land': 0.85,           
        'building site': 9,   
        'forrest': 0.35,      
        'garden': 2,  
        'premises': 15

    }
    def __init__(self, name, locality_coefficient, locality, estate_type, area, commercial):
        super().__init__(name, locality_coefficient, locality)
        self.estate_type = estate_type
        self.area = area
        self.commercial = commercial
    def calculate_tax(self):
        if self.estate_type not in self.ESTATE_TYPE_COEFFICIENTS:
            raise ValueError("Neplatný typ pozemku.")
        estate_coefficient = self.ESTATE_TYPE_COEFFICIENTS[self.estate_type]
        tax = self.area * estate_coefficient * self.locality_coefficient
        if self.commercial:
            tax *= 2
        return math.ceil(tax)
    def __str__(self):
        tax = self.calculate_tax()
        return f" {self.name}, plocha {self.area} metrů čtverečních, lokalita {self.locality} (s koeficientem {self.locality_coefficient}). Daň z této nemovitosti je {tax} Kč."
 
zemědělský_pozemek = Residence ("Zemědělský pozemek", 0.8, "Manětín", 'land', 900, commercial=False )
dům = Residence ( "Dum", 0.8, "Manětín","premises", 120, commercial=False)
kancelář = Residence ( "Kancelář",3.0, "Brno","premises", 90, commercial=True)
print(zemědělský_pozemek)
print(dům)
print(kancelář)