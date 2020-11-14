import os
from json import load, dump

PARTICLES = []
DIRR= "biomes"

for filename in os.listdir(DIRR):
    with open(os.path.join(DIRR, filename)) as file:
        curr = load(file)
        if "particle" in curr["effects"]:
            PARTICLES.append(curr["effects"]["particle"])
        

with open("particles.json", "w") as out:
    dump(PARTICLES, out, indent=4)
