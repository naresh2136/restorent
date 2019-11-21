
# rest.py
import re

order = {"upma", "dosa"}

items = {}

fr = open("data.csv")
fw = open("del.csv", "w")
fr.readline()
for item in fr:
	item = item.strip()
	row = re.split("\s*,\s*", item)
	fw.write(row[0] + " " + row[2] + " " + row[1] + "\n")
fr.close()
fw.close()
