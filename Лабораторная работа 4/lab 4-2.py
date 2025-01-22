import csv
import json

def csv_to_json(file_path, delimiter=',', line_terminator='\n'):
    with open(file_path, 'r', newline=line_terminator) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        data = [row for row in reader]

    json_data = json.dumps(data, indent=4)
    print(json_data)


file_path = 'input.csv'
csv_to_json(file_path)