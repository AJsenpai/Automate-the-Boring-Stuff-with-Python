# removeCsvHeader.py - Removes the header from all CSV files in the current working directory

import csv, os

os.chdir("c:/Users/Jai/Desktop/Docs")

os.makedirs("headerRemoved", exist_ok=True)


# loop through every file in the current working directory
for files in os.listdir("."):
    if not files.endswith(".csv"):
        continue  # skip for non-csv files
    print(f"Removing header form {files}....")

    # read the csv files in skipping first row
    csv_rows = []
    with open(files, "r") as filereader:
        readerObj = csv.reader(filereader)
        for row in readerObj:
            if readerObj.line_num == 1:
                continue
            csv_rows.append(row)

    # write the csv files
    with open(os.path.join("headerRemoved", files), "w", newline="") as writer:
        writerObj = csv.writer(writer)
        for row in csv_rows:
            writerObj.writerow(row)
