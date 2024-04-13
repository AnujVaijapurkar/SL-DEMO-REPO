import os
import csv

def tsv_to_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter='\t')
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            for row in tsvreader:
                csvwriter.writerow(row)

def convert_tsv_to_csv_in_directory(root_directory):
    for foldername, _, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('M4T_S2ST_2023_07_manifest_eng-arb-orig.tsv'):
                input_file = os.path.join(foldername, filename)
                output_file = os.path.join(foldername, filename.replace('.tsv', '.csv'))
                tsv_to_csv(input_file, output_file)

<<<<<<< HEAD
def branch_function1():
    print("Branch function1")
=======
def master_function1():
    print("master_function1")
>>>>>>> master
    
if __name__ == "__main__":
    root_directory = "C:\\Users\\vaija\\Downloads"  # Replace this with the root directory containing subdirectories and .tsv files
    convert_tsv_to_csv_in_directory(root_directory)
