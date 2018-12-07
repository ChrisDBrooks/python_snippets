import os
import csv

file_path_from_user = input("Enter the file path: ")
for file in os.listdir(file_path_from_user):
    if file.endswith(".csv"):
        os.chdir(file_path_from_user)  # Change to the directory with the csv file so the open module finds the file

        with open(file) as file_to_analyze:
            file_reader = csv.reader(file_to_analyze)
            next(file_reader)  # Skip the header row
            for row in file_reader:
                print(row[0])