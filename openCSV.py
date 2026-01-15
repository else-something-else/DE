import csv

filename = input("Enter CSV filename: ")

try:
    with open(filename, "r") as csvFile:
        reader = csv.reader(csvFile)
        rows = list(reader)

        header = rows[0]
        data = rows[1:]

        print("\n--- CSV SUMMARY ---")
        print(f"File name       : {filename}")
        print(f"Columns         : {len(header)}")
        print(f"Columns names   : {header}")
        print(f"Total rows      : {len(data)}")

except FileNotFoundError:
    print("file not found")