import argparse
import csv

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('trasaction_file_path', help='Transaction File Path is required.')
argument_parser.add_argument('standard_file_path', help='Standard File Path is required.')
arguments = argument_parser.parse_args()

print(arguments.standard_file_path)

with open(arguments.trasaction_file_path) as csv_file:
    csv_rows = csv.reader(csv_file , delimiter = ',')
    line_count = 0
    
    for row in csv_rows:
        if line_count == 0:
            print(f'column names are {",".join(row)}')        
        else:
            print(f'row {line_count} - {",".join(row)}')
           
        line_count += 1