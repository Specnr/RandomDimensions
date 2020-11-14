from json import load, dump
from os.path import join
from random import randint, uniform
from copy import deepcopy
from randomizer.helper import get_n_random, get_random_features, get_random_spawners


def random_decimal_colour():
    return randint(0, 256**3)


def biomes_main(config, data):
    biome_counts = config["random-biome-counts"]
    base_dir = join("Base datapack", "biome")
    output_dir = join(config["output"], "minecraft",
                      "worldgen", "biome", "custom")
    for dim, count in biome_counts.items():
        # Use the base file as a basis
        with open(join(base_dir, f"{dim}-base.json")) as base:
            base_data = load(base)
            for i in range(count):
                curr = deepcopy(base_data)
                # Define builder
                curr["surface_builder"] = f"minecraft:custom/{dim}-{i}-surface"
                effects = curr["effects"]
                # Define random colours
                effects["sky_color"] = random_decimal_colour()
                effects["fog_color"] = random_decimal_colour()
                effects["water_color"] = random_decimal_colour()
                effects["water_fog_color"] = random_decimal_colour()
                effects["grass_color"] = random_decimal_colour()
                effects["foliage_color"] = random_decimal_colour()
                # Randomize sounds
                m_types = ["mood_sound", "additions_sound",
                           "music", "ambient_sound"]
                for t in m_types:
                    sound = get_n_random(data[t], randint(0, 1))
                    if len(sound) == 0:
                        del effects[t]
                    else:
                        if "sound" in effects[t]:
                            effects[t]["sound"] = sound[0]
                        else:
                            effects[t] = sound[0]
                # Randomize particles
                # Apply particles if succeeds random chance
                if randint(1, 100*config["particle-chance"]) == 1:
                    effects["particle"] = get_n_random(data["particles"], 1)
                # Randomize starts
                curr["starts"] += get_n_random(data["starts"],
                                               config["random-structures"][dim])
                # Randomize spawners
                curr["spawners"] = get_random_spawners(
                    data["spawners"], config["per-mob-cap"])
                # Add enderman to ensure beatable
                curr["spawners"]["monster"].append(
					{
						"type": "minecraft:enderman",
						"weight": randint(0, 100),
						"maxCount": randint(config["per-mob-cap"] // 2, config["per-mob-cap"]),
						"minCount": randint(0, config["per-mob-cap"] // 2)
					}
				)
                # Randomize carvers
                carvers = get_n_random(
                    data["carvers"], config["random-carvers"][dim])
                curr["carvers"]["air"] += carvers
                # Randomize features
                curr["features"] = get_random_features(
                    data["features"], curr["features"], config["random-features"][dim])
                if dim == "overworld":
                    for fl in curr["features"]:
                        to_rem = []
                        for j in range(len(fl)):
                            # Basalt is hecka invasive
                            if "basalt" in fl[j] or "delta" in fl[j]:
                                to_rem.append(j)
                        for x in sorted(to_rem, reverse=True):
                            del fl[x]

                # Depth, temp and scale
                curr["depth"] = round(uniform(0, 1), 1)
                curr["temp"] = round(uniform(0, 1), 1)
                curr["scale"] = round(uniform(0.7, 1.7), 1)

                with open(join(output_dir, f"{dim}-{i}.json"), 'w') as output:
                    dump(curr, output, indent=4)
    print("* Random Biomes Completed *")
