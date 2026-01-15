import csv
import re

def clean_empty_values(filename):
    try:
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

            header = rows[0]
            data_rows = rows[1:]

            cleaned_rows = [header]

            for row in data_rows:
                if all(cell.strip() != "" for cell in row):
                    cleaned_rows.append(row)

            
            return cleaned_rows
        
    except FileNotFoundError:
        print("File not found")


def format_column_names(filename):
    try:
        with open(filename, "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            header = rows[0]
            data_rows = rows[1:]

            cleaned_header = []
            for column in header:
                #mystring.replace(" ", "_")
                column = column.strip().lower() # trim + lowercase
                column = column.replace(" ", "") # spaces to underscore
                column = re.sub(r"[^\w]", "", column) # remove special chars
                cleaned_header.append(column)

        return cleaned_header + data_rows

    except FileNotFoundError:
        print("File not found")
        return []


filename = "Heart_Disease_Prediction.csv"
#cleaned_data = clean_empty_values(filename)
formated_data = format_column_names(filename)

#print(cleaned_data)
print(formated_data)