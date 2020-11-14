import os
from json import load, dump

MUSIC = set()
DIRR= "biomes"
M_TYPE = "ambient_sound"

for filename in os.listdir(DIRR):
    with open(os.path.join(DIRR, filename)) as file:
        curr = load(file)
        eff = curr["effects"]
        if M_TYPE in eff:
            if "sound" in eff[M_TYPE]:
                MUSIC.add(eff[M_TYPE]["sound"])
            else:
                MUSIC.add(eff[M_TYPE])

with open(f"{M_TYPE}.json", "w") as out:
    dump(list(MUSIC), out, indent=4)
