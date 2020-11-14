import os
from json import load, dump

FEATURES = [
	set(),
	set(),
	set(),
	set(),
	set(),
	set(),
	set(),
	set(),
	set(),
	set()
]
DIRR= "biomes"

for filename in os.listdir(DIRR):
    with open(os.path.join(DIRR, filename)) as file:
        curr = load(file)
        feats = curr["features"]
        for i in range(len(feats)):
            for f in feats[i]:
                FEATURES[i].add(f)
for i in range(len(FEATURES)):
	FEATURES[i] = list(FEATURES[i])

with open("features.json", "w") as out:
    dump(FEATURES, out, indent=4)
