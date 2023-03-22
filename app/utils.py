def get_population(country_dict):
  start_index = 5
  end_index = 12
  range_populations = dict(list(country_dict.items())[start_index:end_index])
  population = { year[0:4] : int(p) for (year, p) in range_populations.items() }
  print(population)
  return population.keys(), population.values()

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result