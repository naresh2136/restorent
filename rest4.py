# rest.py
import re

order = {"upma", "burger"}
order = {"upma"}

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
    if order.issubset(all_items):
        rest.append(i)

price = {}
for i in rest:
    price[i] = 0
    for item in order:
        print(i, item, items[i][item])
        price[i] = price[i] + items[i][item]

print(price)

best = min(price.values())
print(best)

for i in price:
    if price[i] == best:
        print(i)