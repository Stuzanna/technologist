import csv
import json

#courtesy of chatGPT

# Specify the path to the CSV file
csv_file_path = 'file path'
# Specify the path to save the JSON file
output_file_path = './output.json'


def convert_csv_to_json(csv_file_path, output_file_path):
    data = []

    # Read the CSV file
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Convert each row to a dictionary and append to the data list
        for row in csv_reader:
            data.append(row)

    # Convert the data to JSON format
    json_data = json.dumps(data, indent=4)

    # Save JSON data to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(json_data)

    print("JSON data saved to", output_file_path)



try:
    convert_csv_to_json(csv_file_path, output_file_path)
except IOError as e:
    print("Error reading or writing the file:", e)
