import pandas as pd
import pip
import json
import re
import numpy as np


def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])


def concat_file_location(file_name):
    file_location = 'C:\\Users\\kshir\\Documents\\Paradox Interactive\\Age of Wonders 4\\JSONDump\\'
    return file_location + file_name


def shape(lst):
    length = len(lst)
    shp = tuple(shape(sub) if isinstance(sub, list) else 0 for sub in lst)
    if any(x != 0 for x in shp):
        return length, shp
    else:
        return length


def check(item):
    res = [(type(item), len(item))]
    for i in item:
        res.append((type(i), (len(i) if hasattr(i, '__len__') else None)))
    return res


abilities_file_location = concat_file_location('Abilities.json')

'''
empire_progression_file_location = concat_file_location('EmpireProgression.json')
hero_items_file_location = concat_file_location('HeroItems.json')
hero_skills_file_location = concat_file_location('HeroSkills.json')
siege_projects_file_location = concat_file_location('SiegeProjects.json')
spells_file_location = concat_file_location('Spells.json')
structure_upgrades_file_location = concat_file_location('StructureUpgrades.json')
tomes_file_location = concat_file_location('Tomes.json')
units_file_location = concat_file_location('Units.json')
'''

'''
with open(abilities_file_location) as abilities_json:
    abilities_data = json.load(abilities_json)
    type(abilities_data)
'''

abilities_json = open(abilities_file_location)
del abilities_file_location
abilities_data = json.load(abilities_json)
del abilities_json
abilities = pd.DataFrame(abilities_data)
del abilities_data

modifiers = abilities["modifiers"]

# For a given index and list within the series "modifiers"
for idx, lst in enumerate(modifiers):
    # If the row contains a list that isn't empty
    if isinstance(lst, list) and len(lst)>0:
        # Look through each dictionary in that list
        for d in lst:
            if "description" in d and "poison" in d["description"].lower() and False:
                print(idx, d["description"])

tst = [0, 0, 0]
print(abilities.loc[tst])

# print(check(abilities_data[0]))
