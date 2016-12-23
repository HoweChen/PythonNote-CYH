import json
from country_codes import get_country_code
import pygal


filename = './Python Basic/JSON/WorldPopulation/population_data.json'
with open(filename) as fopen:
    pop_data = json.load(fopen)
    # print(type(pop_data))
    # pop_data is a list
    # print(pop_data)

pygal_data = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        # print(country_name + ': ' + str(population))
        code = get_country_code(country_name)
        # print(code)
        if code:
            print(code + ': ' + str(population))
            pygal_data[code] = population
        else:
            print('Error - ' + country_name)

wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', pygal_data)
# print([item for item in pygal_data.items()])

wm.render_to_file('./Python Basic/JSON/WorldPopulation/world_population.svg')
