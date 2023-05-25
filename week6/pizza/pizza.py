import sys
from tabulate import tabulate
import csv

def main():

    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file')

    table, headers = form_table(sys.argv[1])
    print(tabulate(table, headers, tablefmt="grid"))

def form_table(menu):
    table = []
    try:
        file = open(menu)
    except FileNotFoundError:
        sys.exit('File does not exist')

    lines = csv.DictReader(file)
    if 'sicilian.csv' == menu:
      headers = ['Sicilian Pizza', 'Small', 'Large']
      for row in lines:
          t = [row['Sicilian Pizza'], row['Small'], row['Large']]
          table.append(t)
    if 'regular.csv' == menu :
      headers = ['Regular Pizza', 'Small', 'Large']
      for row in lines:
          t = [row['Regular Pizza'], row['Small'], row['Large']]
          table.append(t)

    return table, headers

if __name__ == "__main__":
    main()