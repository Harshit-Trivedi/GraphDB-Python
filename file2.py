import csv

# open required csv and read it as a text string
with open('file1.csv', 'r') as input:
    csv_reader = csv.DictReader(input)

# open new file to save changes
    with open('file2.csv', 'wb') as out_file:
        fieldnames = ['ParkName', 'State', 'partySize', 'RateType', 'BookingType', 'Equipment']
        output_data = csv.DictWriter(out_file, fieldnames=fieldnames, delimiter =',')

        output_data.writeheader()

        #removing not required columns
        for line in csv_reader:
            del line['Country']
            del line['Adult']
            del line['Child']
            del line['BookingStartDate']
            del line['BookingEnddate']
            del line['Night']
            del line['Permits']
            output_data.writerow(line)

print("Writing complete")
    
