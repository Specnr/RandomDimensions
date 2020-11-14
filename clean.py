import os

DATA = os.path.join("Compiled datapacks", "random_dimensions", "data")
DIMS = os.path.join(DATA, "r-dim", "dimension")
WORLDGEN = os.path.join(DATA, "minecraft", "worldgen")
BIOME = os.path.join(WORLDGEN, "biome", "custom")
SURFACE = os.path.join(WORLDGEN, "configured_surface_builder", "custom")
NOISE = os.path.join(WORLDGEN, "noise_settings", "custom")
DIRS = [DIMS, BIOME, SURFACE, NOISE]


def main():
    for d in DIRS:
        for filename in os.listdir(d):
            if filename.count(".") != 0:
                print("Removing {} from {}".format(filename, d))
                os.remove(os.path.join(d, filename))


if __name__ == "__main__":
    print("Beginning Cleanup")
    main()
    print("Done!")
