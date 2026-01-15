import csv

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
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            header = rows[0]

            cleaned_columns = []
            if row in cleaned_columns:



        return cleaned_columns

    except FileNotFoundError:
        print("File not found")



filename = "Heart_Disease_Prediction.csv"
cleaned_data = clean_empty_values(filename)
formated_data = format_column_names(filename)

print(cleaned_data)
print(formated_data)