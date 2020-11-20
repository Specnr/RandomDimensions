# Ensure we're in a random world
execute as @e[predicate=r-dim:in_n_over] at @s run function r-dim:teleport/tele-over
execute as @e[predicate=r-dim:in_n_end] at @s run function r-dim:teleport/tele-over-end
# Nether travel
execute as @e[predicate=r-dim:in_overworld] at @s if block ~ ~ ~ nether_portal run function r-dim:teleport/tele-nether
execute as @e[predicate=r-dim:in_nether] at @s if block ~ ~ ~ nether_portal run function r-dim:teleport/tele-over-nether
# End travel
execute as @e[predicate=r-dim:in_overworld] at @s if block ~ ~ ~ minecraft:end_portal run function r-dim:teleport/tele-end
execute as @e[predicate=r-dim:in_end] at @s if block ~ ~ ~ minecraft:end_portal run function r-dim:teleport/tele-over-end
execute as @e[predicate=r-dim:in_overworld] at @s if block ~ ~-1 ~ minecraft:end_portal run function r-dim:teleport/tele-end
execute as @e[predicate=r-dim:in_end] at @s if block ~ ~-1 ~ minecraft:end_portal run function r-dim:teleport/tele-over-end
