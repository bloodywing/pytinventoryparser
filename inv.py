#!/usr/bin/env python
import csv
import sys

inventorystring = sys.argv[1]

inventoryentries = inventorystring.split('~')

items = dict()
prefixes = dict()

with open('items.tsv') as itemsfile:
    itemsreader = csv.reader(itemsfile, delimiter='\t', quotechar='"')
    for row in itemsreader:
        items.update({row[0]: {'name': row[1]}})

with open('prefixes.tsv') as prefixfile:
    prefixreader = csv.reader(prefixfile, delimiter='\t', quotechar='"')
    for row in prefixreader:
        prefixes.update({row[0]: {'name': row[1]}})

for row in inventoryentries:
    itemid, amount, prefixid = row.split(',')
    if itemid in items.keys():
        print(items[itemid]['name'], amount, prefixes.get(prefixid, {}).get('name', ''))
