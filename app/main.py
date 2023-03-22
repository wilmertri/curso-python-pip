import utils
import read_csv
import charts


def run():

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