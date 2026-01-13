import csv

filename = input("Enter CSV filename: ")

try:
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        header = rows[0]
        data = rows[1:]

        print("\n--- CSV SUMMARY ---")
        print(f"File name       : {filename}")
        print(f"Columns         : {len(header)}")
        print(f"Column names    : {header}")
        print(f"Total rows      : {len(data)}")

except:
    FileNotFoundError()
    print("File not found")
