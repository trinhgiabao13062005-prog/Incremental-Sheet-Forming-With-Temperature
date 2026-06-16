import csv
import os

input_dir = r"E:\Scientific Research\Incremental Sheet Forming\Data\raw_machanical"
output_dir = r"E:\Scientific Research\Incremental Sheet Forming\Data\clean_data_mechanical"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

print("Tim thay {} files:".format(len(csv_files)))

for filename in sorted(csv_files):
    input_file = os.path.join(input_dir, filename)
    output_file = os.path.join(output_dir, "clean_" + filename)

    try:
        with open(input_file, "r", newline='', encoding="utf-8") as infile:
            reader = csv.reader(infile)
            rows = list(reader)

        filtered_rows = [row for row in rows if any(cell.strip() for cell in row)]

        with open(output_file, "w", newline='', encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            writer.writerows(filtered_rows)

        print("Xong: clean_{}".format(filename))

    except Exception as e:
        print("LOI {}: {}".format(filename, str(e)))

print("\nHoan thanh tat ca!")