class Planet:
    def __init__(self, name, planet_type, star):
        if not isinstance(name, str):
            raise TypeError(f'name, planet type, and star must be strings')
        elif not isinstance(planet_type, str):
            raise TypeError(f'name, planet type, and star must be strings')
        elif not isinstance(star, str):
            raise TypeError(f'name, planet type, and star must be strings')
        elif name == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')
        elif planet_type == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')
        elif star == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')

        self.name = name
        self.planet_type = planet_type
        self.star = star


    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'
    
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'
    

planet_1=Planet('erath', 'Terrestrial', 'sun') 
planet_2=Planet('erath2', 'Terrestrial2', 'sun2') 
planet_3=Planet('erath3', 'Terrestrial3', 'sun3') 
 

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())