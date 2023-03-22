import matplotlib.pyplot as plt

def generate_bar_chart(labels, values, name):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./images/{name.lower()}_bar.png')

def generate_pie_chart(labels, values, name):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig(f'./images/{name.lower()}_pie.png')

if __name__ == '__main__':
  labels = ['a', 'b', 'c', 'd']
  values = [100, 200, 80, 150]
  generate_pie_chart(labels, values)
