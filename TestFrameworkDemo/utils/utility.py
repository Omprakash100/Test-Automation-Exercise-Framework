import csv

def read_csv_data(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def write_csv_data(file_path, data_to_add):
    with open(file_path, 'a', newline='\n') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data_to_add)