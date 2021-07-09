from json import load, dump
from os.path import join
from copy import deepcopy
from randomizer.helper import get_n_random


def surfaces_main(config, data):
    first_pass = True
    biome_counts = config["random-biome-counts"]
    base_dir = join("Base datapack", "configured_surface_builder")
    output_dir = join(config["output"], "minecraft",
                      "worldgen", "configured_surface_builder", "custom")
    for dim, count in biome_counts.items():
        # Use the base file as a basis
        with open(join(base_dir, "{}-base-surface.json".format(dim))) as base:
            base_data = load(base)
            for i in range(count):
                curr = deepcopy(base_data)
                # Randomize config
                surface_config = curr["config"]
                blocks = get_n_random(data["blocks"], 3)
                # Ensure 1 biome as stone as top layer to ensure gravel
                surface_config["top_material"]["Name"] = "minecraft:stone" if first_pass else blocks[0]
                surface_config["under_material"]["Name"] = blocks[1]
                surface_config["underwater_material"]["Name"] = blocks[2]
                with open(join(output_dir, "{}-{}-surface.json".format(dim, i)), 'w') as output:
                    dump(curr, output, indent=4)
                first_pass = False
    print("* Random Surface Builders Completed *")
