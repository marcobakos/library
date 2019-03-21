import csv

#
with open('Students_Unique_OK.csv') as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file)
    for row in cool_csv_dict:
        print(row)

with open('Students_Unique_OK.csv') as file_obj:
    for i in range(11):
        file_rec = file_obj.readline()
        print(file_rec)