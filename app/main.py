import utils
import read_csv
import charts
import pandas as pd

def run():

  '''
  
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  
  '''
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'North America']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values 

  charts.generate_pie_chart(countries, percentages, 'north_america')

  data = read_csv.read_csv('data.csv')
  country = input('Ingrese el país: ')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    name_country = country['Country/Territory']
    keys, values = utils.get_population(country)
    charts.generate_bar_chart(keys, values, name_country)
    charts.generate_pie_chart(keys, values, name_country)

if __name__ == '__main__':
  run()