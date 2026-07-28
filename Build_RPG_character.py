full_dot = '●'
empty_dot = '○'

def create_character(name_character, strength, intelligence, charisma):
        if not isinstance(name_character, str):
             return 'The character name should be a string'
        elif name_character == '':
             return 'The character should have a name'
        elif len(name_character) > 10:
             return 'The character name is too long'
        elif name_character.count(' ') > 0:
              return 'The character name should not contain spaces'
        stats=[strength, intelligence, charisma]   
        for stat in stats:
              if not isinstance(stat, int):
                    return 'All stats should be integers'         
              elif stat < 1 :
                    return 'All stats should be no less than 1'
              elif stat > 4:
                    return 'All stats should be no more than 4'
        if sum(stats) != 7:
              return 'The character should start with 7 points'

        def dots(value):
              return value * full_dot + (10 - value) * empty_dot

        return f'{name_character}\nSTR {dots(strength)}\nINT {dots(intelligence)}\nCHA {dots(charisma)}'


my_character=create_character("Amir", 4, 2, 1)
print(my_character)