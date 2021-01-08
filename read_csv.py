import csv
import ast

all_clickable_mods = {}
with open('mod_relationships.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        x = row['related_mods']
        x = ast.literal_eval(x)
        test_dict[row['module']] = x

