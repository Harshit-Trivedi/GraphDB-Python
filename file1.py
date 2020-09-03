import csv

# create new file
with open('file1.csv' , 'wb') as output:

    # open required csv
    with open('DNR_Camping_Parks_Reservation_Data_2016.csv') as csv_file:
        output_data = csv.writer(output, delimiter =',')
        data = csv.reader(csv_file, delimiter=',')
        for row in data:
            output_data.writerow(row)
print("Writing complete")
    
