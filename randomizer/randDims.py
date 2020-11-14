from json import load, dump
from os.path import join
import random as r


def dims_main(config, data):
    biome_counts = config["random-biome-counts"]
    base_dir = join("Base datapack", "dimension")
    output_dir = join(config["output"], "r-dim", "dimension")
    for dim, count in biome_counts.items():
        with open(join(base_dir, f"r-{dim}.json")) as base:
            base_data = load(base)
            # Set the seed
            base_data["generator"]["seed"] = config["seed"]
            source = base_data["generator"]["biome_source"]
            source["seed"] = config["seed"]
            # Randomise noise?
            biomes = source["biomes"]
            for i in range(count):
                biomes.append({
                    "parameters": {
                        "altitude": round(r.uniform(-1, 1), 1),
                        "weirdness": round(r.uniform(-1, 1), 1),
                        "offset": round(r.uniform(0, 1), 1),
                        "temperature": round(r.uniform(-1, 1), 1),
                        "humidity": round(r.uniform(-1, 1), 1)
                    },
                    "biome": f"minecraft:custom/{dim}-{i}"
                })
        with open(join(output_dir, f"r-{dim}.json"), 'w') as output:
            dump(base_data, output, indent=4)
    print("* Random Dimensions Completed *")
