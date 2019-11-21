# rest.py
import re

order = {"upma", "coke", "burger", "tea", "abc"}

items = {}

fr = open("data.csv")
fr.readline()
for item in fr:
    item = item.strip()
    row = re.split("\s*,\s*", item)
    if row[0] not in items:
        items[row[0]] = {}
    items[row[0]][row[2]] = float(row[1])
fr.close()

print(items)

rest = []
for i in items:
    all_items = set(items[i].keys())
    print(i, order, all_items)
    if order.issubset(all_items):
        print("==>", i)
        rest.append(i)

print(rest)