from typing import Mapping, Any

from Utils import visualize_regions
from worlds.AutoWorld import WebWorld, World
from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Region, Location
from worlds.unfair_flips.options import UnfairFlipsOptions, unfair_flips_options
from worlds.unfair_flips.items import *
from worlds.unfair_flips.locations import *
from worlds.unfair_flips.regions import *


class UnfairFlipsWeb(WebWorld):
    theme = "partyTime"

    setup_en = Tutorial(
        "Unfair Flips Setup Guide",
        "A guide to setting up the Unfair Flips randomizer connected to an Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["xMcacutt", "Dashieswag92", "itepastra"]
    )

    tutorials = [setup_en]
    options_groups = unfair_flips_options


locations = generate_locations()


class UnfairFlipsWorld(World):
    """
    Flip da coin!
    """
    game = "Unfair Flips"
    options_dataclass = UnfairFlipsOptions
    options: UnfairFlipsOptions
    topology_present = False
    item_name_to_id = {name: item.code for name, item in unfair_flips_item_table.items()}
    location_name_to_id = locations
    itempool = []

    web = UnfairFlipsWeb()

    ut_can_gen_without_yaml = True

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.itempool = []


    def fill_slot_data(self):
        # visualize_regions(self.multiworld.get_region("Menu", self.player), f"Player{self.player}.puml",
        #                   show_entrance_names=True,
        #                   regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
        #                       self.player])
        gate_count = self.options.required_heads // 2
        upgrades_count = round(gate_count * (1 - JUNK_FACTOR))
        return {
            "ModVersion": "1.4.0",
            # "EnergyLink": self.options.energy_link.value,
            "RequiredHeads": self.options.required_heads.value,
            "StartingHeadsChance": self.options.starting_heads_chance.value,
            "DeathLink": self.options.death_link.value,
            "DeathLinkChance": self.options.death_link_chance.value,
            "DeathLinkMinStreak": self.options.death_link_min_streak.value,
            "FlipDifficulty": self.options.flip_difficulty.value,
            "HeadsUpgradeCount": gate_count,
            "FlipSpeedUpgradeCount": gate_count,
            "ComboUpgradeCount": gate_count,
            "AutoFlipEnabled": self.options.auto_flip.value,
            "AutoFlipUpgradeCount": upgrades_count,
        }


    def handle_ut_yamless(self, slot_data: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        if not slot_data \
                and hasattr(self.multiworld, "re_gen_passthrough") \
                and isinstance(self.multiworld.re_gen_passthrough, dict) \
                and self.game in self.multiworld.re_gen_passthrough:
            slot_data = self.multiworld.re_gen_passthrough[self.game]
        if not slot_data:
            return None
        self.options.required_heads.value = slot_data["RequiredHeads"]
        self.options.flip_difficulty.value = slot_data["FlipDifficulty"]
        self.options.starting_heads_chance.value = slot_data["StartingHeadsChance"]
        return slot_data


    def generate_early(self):
        self.handle_ut_yamless(None)


    def get_filler_item_name(self) -> str:
        return get_random_item_names(self.random, 1, junk_weights)[0]


    def create_regions(self):
        create_regions(self)
        connect_all_regions(self)
        return

    def create_items(self):
        create_items(self)
        return

    def create_item(self, name: str) -> Item:
        item_info = unfair_flips_item_table[name]
        return UnfairFlipsItem(name, item_info.classification, item_info.code, self.player)

    def create_event(self, region_name: str, event_loc_name: str, event_item_name: str) -> None:
        region: Region = self.multiworld.get_region(region_name, self.player)
        loc: UnfairFlipsLocation = UnfairFlipsLocation(self.player, event_loc_name, None, region)
        loc.place_locked_item(UnfairFlipsItem(event_item_name, ItemClassification.progression, None, self.player))
        region.locations.append(loc)

    def generate_output(self, output_dir):
        return
