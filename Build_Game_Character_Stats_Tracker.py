class GameCharacter:
    def __init__(self, name):
        self._name= name
        self._health= 100
        self._mana= 50
        self._level= 1

    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_health):
        if not isinstance(new_health, int):
            raise TypeError("'health' must be int.")
        if new_health < 0:
            new_health = 0
        if new_health > 100:
            new_health = 100
        self._health= new_health
    
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, new_mana):
        if not isinstance(new_mana, int):
            raise TypeError("'health' must be int.")
        if new_mana < 0:
            new_mana = 0
        if new_mana > 50:
            new_mana = 50
        if 0 > new_mana < 50:
            raise ValueError("'health' must between 0 to 50")
        self._mana= new_mana
    
    @property
    def level(self):
        return self._level
    
    def level_up(self):
        self._level +=1
        self.health = 100
        self.mana= 50
        print(f'{self._name} leveled up to {self._level}!')
    
    def __str__(self):
        return(f'Name: {self._name}\nLevel: {self._level}\nHealth: {self._health}\nMana: {self._mana}')



hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up