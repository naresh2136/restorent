# rest.py

order = {"upma", "dosa"}

items = {}

fr = open("data.csv")
fr.readline()
for item in fr:
	item = item.strip()
	print(item)

fr.close()

"""
1, 4.00, burger 
2, 2.00, dosa 

1 : { burger: 4.00, dosa: 6.00}, 2: {dosa:1, upma:2}

"""
