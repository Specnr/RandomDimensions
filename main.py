from json import load
from random import randint
import os
from randomizer.randBiomes import biomes_main
from randomizer.randDims import dims_main
from randomizer.randNoise import noise_main
from randomizer.randSurfaces import surfaces_main


def load_data():
    base_dir = "data"
    data = {}
    for filename in os.listdir(base_dir):
        with open(os.path.join(base_dir, filename)) as f:
            data[filename.split(".")[0]] = load(f)
    return data


def load_config():
    with open("config.json") as f:
        config = load(f)
        config["output"] = os.path.join("Compiled datapacks",
                                        "random_dimensions", "data")
        if config["seed"] == -1:
            config["seed"] = randint(-2e10, 2e10)
        return config


def main():
    config = load_config()
    data = load_data()
    surfaces_main(config, data)
    biomes_main(config, data)
    noise_main(config, data)
    dims_main(config, data)


if __name__ == "__main__":
    print("** Starting Randomization **")
    main()
    print("** Completed! **")
