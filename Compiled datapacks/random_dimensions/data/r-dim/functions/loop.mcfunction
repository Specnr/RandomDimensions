# Ensure we're in a random world
execute at @a[predicate=r-dim:in_n_over] run function r-dim:teleport/tele-over
execute at @a[predicate=r-dim:in_n_end] run function r-dim:teleport/tele-over-end
# Nether travel
execute at @a[predicate=r-dim:in_overworld] if block ~ ~ ~ nether_portal run function r-dim:teleport/tele-nether
execute at @a[predicate=r-dim:in_nether] if block ~ ~ ~ nether_portal run function r-dim:teleport/tele-over-nether
# End travel
execute at @a[predicate=r-dim:in_overworld] if block ~ ~ ~ minecraft:end_portal run function r-dim:teleport/tele-end
execute at @a[predicate=r-dim:in_end] if block ~ ~ ~ minecraft:end_portal run function r-dim:teleport/tele-over-end