import os
from json import load, dump

STARTS = set()
DIRR= "biomes"

for filename in os.listdir(DIRR):
    with open(os.path.join(DIRR, filename)) as file:
        curr = load(file)
        start = curr["starts"]
        for s in start:
            STARTS.add(s)

with open("starts.json", "w") as out:
    dump(list(STARTS), out, indent=4)
