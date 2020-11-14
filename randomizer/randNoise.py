from json import load, dump
from os.path import join
import random as r
from randomizer.helper import get_n_random

bad_bois = {"minecraft:gravel", "minecraft:sand", "minecraft:red_sand"}


def noise_main(config, data):
    biome_counts = config["random-biome-counts"]
    base_dir = join("Base datapack", "noise_settings")
    output_dir = join(config["output"], "minecraft",
                      "worldgen", "noise_settings", "custom")
    for dim, count in biome_counts.items():
        with open(join(base_dir, "{}-settings.json".format(dim))) as base:
            base_data = load(base)
        base_data["amplified"] = bool(r.randint(0, 1))
        # Randomize Default Block
        blk = get_n_random(data["blocks"], 1)[0]
        if config["remove-falling-blocks"]:
            while blk in bad_bois:
                blk = get_n_random(data["blocks"], 1)[0]
        base_data["default_block"]["Name"] = blk
        # Randomize fluid
        if dim != "end":
            base_data["default_fluid"]["Name"] = get_n_random(data["fluids"], 1)[
                0]

        with open(join(output_dir, "{}-settings.json".format(dim)), 'w') as output:
            dump(base_data, output, indent=4)
    print("* Random Noise Completed *")
