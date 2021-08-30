
from enum import Enum, IntEnum
class Country(Enum): 
    Afghanistan = 93 
    Albania = 355 
    Algeria = 213 
    Andorra = 376 
    Angola = 244 
    Antarctica = 672 
print('\nMember name: {}'.format(Country.Albania.name)) 
print('Member value: {}'.format(Country.Albania.value)) 
for data in Country: 
    print('{:15} = {}'.format(data.name, data.value))
    
import enum 
class Country(enum.IntEnum): 
    Afghanistan = 93 
    Albania = 355 
    Algeria = 213 
    Andorra = 376 
    Angola = 244 
    Antarctica = 672 
print('Country Name ordered by Country Code:') 
print('\n'.join('  ' + c.name for c in sorted(Country)))


class Country(IntEnum): 
    Afghanistan = 93 
    Albania = 355 
    Algeria = 213 
    Andorra = 376 
    Angola = 244 
    Antarctica = 672 
country_code_list = list(map(int, Country)) 
print(country_code_list) 
