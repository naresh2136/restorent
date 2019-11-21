
# rest.py
import re

order = {"upma", "dosa"}

items = {}

fr = open("data.csv")
fr.readline()
for item in fr:
	item = item.strip()
	row = re.split("\s*,\s*", item)
	print(row)
	input()

fr.close()