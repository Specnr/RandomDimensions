import os
from json import load, dump

ALL = set()
BLACKLIST_ENDS = [
    "slab",
    "fence",
    "wall",
    "stairs",
    "trapdoor",
    "anvil",
    "pane",
    "chest",
    "sapling",
    "shulker_box",
    "podzol",
    "mycelium",
    "door",
    "fungus",
    "mushroom",
    "campfire",
    "tnt",
    "barrel",
    "roots",
    "bamboo",
    "nest",
    "hive",
    "log",
    "wood",
    "leaves",
    "pumpkin",
    "cactus",
    "melon",
    "grass_block",
    "basalt",
    "frosted_ice"
]

for filename in os.listdir("blocks"):
    with open(os.path.join("blocks", filename)) as file:
        curr = load(file)
        vals = curr["values"]
        for v in vals:
            if v.startswith("minecraft"):
                valid = True
                for b in BLACKLIST_ENDS:
                    valid = valid and not v.endswith(b)
                if valid:
                    ALL.add(v)

with open("blocks.json", "w") as out:
    dump(list(ALL), out, indent=4)
