the_world ={}
countries = []
cities = []
while True:
    query_country = input('TYPE THE NAME OF THE COUNTRY:')
    countries.append(query_country)
    city = input('what is the capital city of ' + query_country + ' ?')
    cities.append(city)
    quiz = input('Would you like to add counties?(y/n)')
    if quiz == 'n':
        break
for i in range(len(countries)):
    the_world[countries [i]] = cities[i]
print(the_world)
