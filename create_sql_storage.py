import pandas as pd
import json
from get_mod_data import get_mod_data
from add_other_modules import add_all
from filter_clickable_mods import only_clickable

mod_relationships = pd.DataFrame(columns=['module', 'related_mods'])

# time to iterate over all the modules :(

with open('all_mods.json', 'r') as file:
    all_mods_name = json.load(file)
    for i in range(len(all_mods_name)):
        if not all_mods_name[i]['semesterData']:
            continue
        mod_name = all_mods_name[i]['moduleCode']

        # need to get dictionary of all the modules related
        related_mods = []
        add_all(related_mods, get_mod_data(mod_name))
        related_mods = only_clickable(related_mods)

        mod_relationships = mod_relationships.append({'module': mod_name, 'related_mods': related_mods}, ignore_index=True)
        print(i)

mod_relationships.to_csv('mod_relationships_new.csv', index=False)