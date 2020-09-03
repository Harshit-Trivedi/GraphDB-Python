# Overview
Data extraction for parks in Nova Scotia, Canada and visualization 

## Dataset Source

https://data.novascotia.ca/Lands-Forests-and-Wildlife/DNR-Camping-Parks-Reservation-Data-2016/4zt7-x443

### About the Dataset

The dataset DNR Camping Parks Reservation Data 2016 lists various camping sites in Nova Scotia and this information is collected through the reservation system 
for the general public to reserve camping sites in Nova Scotia. The dataset has 34,900 rows and 13 columns. It lists a lot of information regarding the park’s 
name (ParkName), origin state and country of the water body, total booking size (partySize), type of rate (RateType), the type of booking (BookingType), Equipment, 
Booking start date along with its end date, night and their permits.

## File Description

### file1.csv

I have used the csv module to read and write the contents from the dataset csv file named DNR_Camping_Parks_Reservation_Data_2016.csv to file1.csv respectively. 
To create the csv file from extracting all the data from dataset, I have used the functions ‘csv.writer’ and ‘csv.reader’ to write and read data respectively. 
As I am dealing with csv files, naturally the delimiter used is comma (,).

### file2.csv

Here I have removed the unnecessary columns and extracted data on ParkName, State, PartySize, BookingType, RateType and Equipment.

### file3.csv

Scanned the "Equipment" column, and replaced all “less than” with “LT” [e.g. less than 30 ft. after transforming LT30ft]. Similarly, replaced all “Single tent” with “ST”.
I have used the regex module to perform this substitutions. To find and replace these words, I have used the ‘.sub’ function. I have replaced and substituted both the 
words consecutively rather than simultaneously to make the code simpler.

### file4.csv

This file has only the 20 unique parks in Nova Scotia which have the maximum number of "partySize".

## Visualization using Neo4j

### Load data and node creation
![](graph%20images/load_data_and_node_creation.png)

### Parks with identical ‘RateType’, connected using a ‘NeghbourByRate’ relation
![](graph%20images/NeghbourByRate.png)

### Parks with identical ‘Equipment’, connected using a ‘NeghbourByEquipment’ relation
![](graph%20images/NeghbourByEquipment.png)

### Final Image file that has both the relations: NeghourByRate and NeghbourByEquipment
![](graph%20images/graph.png)

### Using visualization, found the park with maximum "partySize"
![](graph%20images/visualization.png)

