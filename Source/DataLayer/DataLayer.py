#Just a test file
import _csv


def get_destinations():
    with open('Destinations.csv') as csv_file:
        csv_reader = _csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                ids,place = row
                print(f'\t id: {ids} er id fyrir: {place}')
                line_count += 1
        #print(f'Processed {line_count} lines.')

def add_destinations(new_ids,new_place):
    with open('Destinations.csv','a') as csv_file:
        csv_reader = _csv.reader(csv_file, delimiter=',')
        line_count = 0
        myCSVrow = new_ids+','+new_place
        csv_file.write(myCSVrow)


new_ids = str('NewIDdkdkd')
new_place = str('NewPlacekdsæd')
add_destinations(new_ids,new_place)
get_destinations()
