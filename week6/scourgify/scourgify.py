import sys
import csv

def main():
    check_inputs(sys.argv)

    try:
       old_file = open(sys.argv[1])
    except FileNotFoundError:
       sys.exit('Could not read invalid_file.csv')

    write_file(sys.argv[2])

def check_inputs(i):
    if len(i) < 3:
        sys.exit('Too few command-line arguments')
    elif len(i) > 3:
        sys.exit('Too many command-line arguments')
    elif '.csv' not in i[1] or '.csv' not in i[1]:
        sys.exit('Not a CSV file')

def write_file(f2):

    students = []

    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lastName, firstName = row['name'].split(', ')
            students.append({'first': firstName, 'last': lastName, "house": row['house']})

    # header names, first/last/house
    keys = students[0].keys()
    with open(sys.argv[2], 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, keys)
        writer.writeheader()
        writer.writerows(students)

if __name__ == "__main__":
    main()