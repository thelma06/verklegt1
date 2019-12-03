#Just a test file
import _csv

with open('Destinations.csv') as csv_file:
    csv_reader = _csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Dálkanöfnin eru {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} er id fyrir {row[1]}')
            line_count += 1
    print(f'Processed {line_count} lines.')