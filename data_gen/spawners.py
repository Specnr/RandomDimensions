import os
from json import load, dump

SPAWNERS = {
    "creature": set(),
    "monster": set(),
    "water_creature": set(),
    "ambient": set(),
    "water_ambient": set(),
    "misc": set()
}
DIRR= "biomes"

for filename in os.listdir(DIRR):
    with open(os.path.join(DIRR, filename)) as file:
        curr = load(file)
        spwn = curr["spawners"]
        for t, l in spwn.items():
            for item in l:
                SPAWNERS[t].add(item["type"])

NEW_SPAWNERS = {}
for t, s in SPAWNERS.items():
    NEW_SPAWNERS[t] = list(s)

with open("spawners.json", "w") as out:
    dump(NEW_SPAWNERS, out, indent=4)
