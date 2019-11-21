
import re

inp = "1, 4.00, burger"
out = re.split("\s*,\s*", inp)
print(out)
print(out[1])
print(out[2])

d = {}
d[out[0]] = {}
print(d)

d[out[0]][out[2]] = out[1]
print(d)