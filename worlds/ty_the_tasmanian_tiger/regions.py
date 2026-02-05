from enum import Enum

from BaseClasses import MultiWorld, Region, Entrance
from worlds.ty_the_tasmanian_tiger.options import Ty1Options
from worlds.ty_the_tasmanian_tiger.locations import create_locations
from typing import List, Dict
from .data import *

class Ty1Region(Region):
    subregions: List[Region] = []


def connect_regions(world, from_name: str, to_name: str, entrance_name: str) -> Entrance:
    entrance_region = world.get_region(from_name)
    exit_region = world.get_region(to_name)
    return entrance_region.connect(exit_region, entrance_name)


def create_region(world, name: str):
    reg = Region(name, world.player, world.multiworld)
    create_locations(world.player, world.options, reg)
    world.multiworld.regions.append(reg)

def create_regions(world):
    create_region(world, "Menu")
    create_region(world, "Rainbow Cliffs")
    create_region(world, "Rainbow Cliffs - PF")
    create_region(world, "Bli Bli Station")
    create_region(world, "Bli Bli Station Gate")
    create_region(world, "Bli Bli Station Gate - PF")
    create_region(world, "Pippy Beach")
    create_region(world, "Pippy Beach - PF")
    create_region(world, "Lake Burril")
    create_region(world, "Final Gauntlet")
    create_region(world, "Final Gauntlet - PF")
    create_region(world, "Two Up")
    create_region(world, "Two Up - PF")
    create_region(world, "Two Up - Upper Area")
    create_region(world, "Two Up - Upper Area - PF")
    create_region(world, "Two Up - End Area")
    create_region(world, "Walk in the Park")
    create_region(world, "Walk in the Park - PF")
    create_region(world, "Ship Rex")
    create_region(world, "Ship Rex - PF")
    create_region(world, "Ship Rex - Beyond Gate")
    create_region(world, "Ship Rex - Beyond Gate - PF")
    create_region(world, "Bull's Pen")
    create_region(world, "Bridge on the River Ty")
    create_region(world, "Bridge on the River Ty - Underwater")
    create_region(world, "Bridge on the River Ty - PF")
    create_region(world, "Bridge on the River Ty - Beyond Broken Bridge")
    create_region(world, "Bridge on the River Ty - Beyond Broken Bridge Underwater")
    create_region(world, "Bridge on the River Ty - Beyond Broken Bridge - PF")
    create_region(world, "Snow Worries")
    create_region(world, "Snow Worries - PF")
    create_region(world, "Snow Worries - Underwater")
    create_region(world, "Outback Safari")
    create_region(world, "Crikey's Cove")
    create_region(world, "Lyre, Lyre Pants on Fire")
    create_region(world, "Lyre, Lyre Pants on Fire - PF")
    create_region(world, "Beyond the Black Stump")
    create_region(world, "Beyond the Black Stump - PF")
    create_region(world, "Beyond the Black Stump - Upper Area")
    create_region(world, "Beyond the Black Stump - Glide Behind the Mountain")
    create_region(world, "Beyond the Black Stump - Upper Area - PF")
    create_region(world, "Rex Marks the Spot")
    create_region(world, "Rex Marks the Spot - PF")
    create_region(world, "Rex Marks the Spot - Underwater")
    create_region(world, "Fluffy's Fjord")
    create_region(world, "Cass' Pass")
    create_region(world, "Cass' Crest")
    create_region(world, "Final Battle")


def connect_all_regions(world, portal_map: List[int]):
    if world.options.level_shuffle and not hasattr(world, "re_gen_passthrough"):
        world.random.shuffle(portal_map)
    for i in portal_map:
        print(i)
    connect_regions(world, "Menu",
                    "Rainbow Cliffs", "Menu -> Z1")
    connect_regions(world, "Rainbow Cliffs",
                    "Rainbow Cliffs - PF", "Z1 - PF")
    connect_regions(world, "Rainbow Cliffs",
                    "Bli Bli Station", "Z1 -> A Zone")
    connect_regions(world, "Bli Bli Station",
                    "Bli Bli Station Gate", "A Zone Gate")
    connect_regions(world, "Bli Bli Station Gate",
                    "Bli Bli Station Gate - PF", "A Zone Gate - PF")
    connect_regions(world, "Rainbow Cliffs",
                    "Pippy Beach", "Z1 -> B Zone")
    connect_regions(world, "Pippy Beach",
                    "Pippy Beach - PF", "B Zone - PF")
    connect_regions(world, "Rainbow Cliffs",
                    "Lake Burril", "Z1 -> C Zone")
    connect_regions(world, "Rainbow Cliffs",
                    "Final Gauntlet", "Z1 -> E Zone")
    connect_regions(world, "Final Gauntlet",
                    "Final Gauntlet - PF", "E Zone - PF")
    ent_a1 = connect_regions(world, "Bli Bli Station",
                             ty1_levels[Ty1LevelCode(portal_map[0])], "A1 Portal")
    ent_a2 = connect_regions(world, "Bli Bli Station Gate",
                             ty1_levels[Ty1LevelCode(portal_map[1])], "A2 Portal")
    ent_a3 = connect_regions(world, "Bli Bli Station Gate",
                             ty1_levels[Ty1LevelCode(portal_map[2])], "A3 Portal")
    connect_regions(world, "Bli Bli Station Gate", ty1_levels[Ty1LevelCode.A4], "A4 Portal")
    ent_b1 = connect_regions(world, "Pippy Beach",
                             ty1_levels[Ty1LevelCode(portal_map[3])], "B1 Portal")
    ent_b2 = connect_regions(world, "Pippy Beach",
                             ty1_levels[Ty1LevelCode(portal_map[4])], "B2 Portal")
    ent_b3 = connect_regions(world, "Pippy Beach",
                             ty1_levels[Ty1LevelCode(portal_map[5])], "B3 Portal")
    connect_regions(world, "Pippy Beach", ty1_levels[Ty1LevelCode.D4], "D4 Portal")
    ent_c1 = connect_regions(world, "Lake Burril",
                             ty1_levels[Ty1LevelCode(portal_map[6])], "C1 Portal")
    ent_c2 = connect_regions(world, "Lake Burril",
                             ty1_levels[Ty1LevelCode(portal_map[7])], "C2 Portal")
    ent_c3 = connect_regions(world, "Lake Burril",
                             ty1_levels[Ty1LevelCode(portal_map[8])], "C3 Portal")
    connect_regions(world, "Lake Burril", ty1_levels[Ty1LevelCode.C4], "C4 Portal")
    connect_regions(world, "Final Gauntlet",
                    "Cass' Pass", "E1 Portal")
    connect_regions(world, "Cass' Pass",
                    "Cass' Crest", "E1 -> D2")
    connect_regions(world, "Cass' Crest",
                    "Final Battle", "D2 -> E4")
    connect_regions(world, "Two Up",
                    "Two Up - PF", "Two Up - PF")
    connect_regions(world, "Two Up",
                    "Two Up - Upper Area", "Two Up - Upper Area")
    connect_regions(world, "Two Up - Upper Area",
                    "Two Up - Upper Area - PF", "Two Up - Upper Area - PF")
    connect_regions(world, "Two Up",
                    "Two Up - End Area", "Two Up - End Area")
    connect_regions(world, "Walk in the Park",
                    "Walk in the Park - PF", "Walk in the Park - PF")
    connect_regions(world, "Ship Rex",
                    "Ship Rex - PF", "Ship Rex - PF")
    connect_regions(world, "Ship Rex",
                    "Ship Rex - Beyond Gate", "Ship Rex - Sea Gate")
    connect_regions(world, "Ship Rex - Beyond Gate",
                    "Ship Rex - Beyond Gate - PF", "Ship Rex - Gate - PF")
    connect_regions(world, "Bridge on the River Ty",
                    "Bridge on the River Ty - Underwater", "Bridge on the River Ty - Underwater")
    connect_regions(world, "Bridge on the River Ty",
                    "Bridge on the River Ty - PF", "Bridge on the River Ty - PF")
    connect_regions(world, "Bridge on the River Ty",
                    "Bridge on the River Ty - Beyond Broken Bridge", 
                    "Bridge on the River Ty - Broken Bridge Glide")
    connect_regions(world, "Bridge on the River Ty - Beyond Broken Bridge",
                    "Bridge on the River Ty - Beyond Broken Bridge Underwater",
                    "Bridge on the River Ty - Beyond Broken Bridge Underwater")
    connect_regions(world, "Bridge on the River Ty - Beyond Broken Bridge",
                    "Bridge on the River Ty - Beyond Broken Bridge - PF", 
                    "Bridge on the River Ty - Broken Bridge - PF")
    connect_regions(world, "Snow Worries",
                    "Snow Worries - PF", "Snow Worries - PF")
    connect_regions(world, "Snow Worries",
                    "Snow Worries - Underwater", "Snow Worries - Underwater")
    connect_regions(world, "Lyre, Lyre Pants on Fire",
                    "Lyre, Lyre Pants on Fire - PF", "Lyre, Lyre Pants on Fire - PF")
    connect_regions(world, "Beyond the Black Stump",
                    "Beyond the Black Stump - PF", "Beyond the Black Stump - PF")
    connect_regions(world, "Beyond the Black Stump",
                    "Beyond the Black Stump - Upper Area", "Beyond the Black Stump - Upper Area")
    connect_regions(world, "Beyond the Black Stump - Upper Area",
                    "Beyond the Black Stump - Glide Behind the Mountain",
                    "Beyond the Black Stump - Glide")
    connect_regions(world, "Beyond the Black Stump - Upper Area",
                    "Beyond the Black Stump - Upper Area - PF", 
                    "Beyond the Black Stump - Upper Area - PF")
    connect_regions(world, "Rex Marks the Spot",
                    "Rex Marks the Spot - PF", "Rex Marks the Spot, PF")
    connect_regions(world, "Rex Marks the Spot",
                    "Rex Marks the Spot - Underwater", "Rex Marks the Spot - Underwater")
    # 0.6.0 ENTRANCE RANDO SUPPORT
    # if options.level_shuffle:
        # disconnect_entrance_for_randomization(ent_a1, 0)
        # disconnect_entrance_for_randomization(ent_a2, 0)
        # disconnect_entrance_for_randomization(ent_a3, 0)
        # disconnect_entrance_for_randomization(ent_b1, 0)
        # disconnect_entrance_for_randomization(ent_b2, 0)
        # disconnect_entrance_for_randomization(ent_b3, 0)
        # disconnect_entrance_for_randomization(ent_c1, 0)
        # disconnect_entrance_for_randomization(ent_c2, 0)
        # disconnect_entrance_for_randomization(ent_c3, 0)
        # target_group_lookup: Dict[int, List[int]] = {0: [0]}
        # return randomize_entrances(world.worlds[player], True, target_group_lookup)
