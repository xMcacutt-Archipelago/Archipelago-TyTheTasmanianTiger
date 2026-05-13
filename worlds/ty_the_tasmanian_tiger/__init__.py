import dataclasses
from typing import List, Dict, Optional, Any
from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Region, Location
from Options import OptionError, PerGameCommonOptions
from Utils import visualize_regions
from worlds.AutoWorld import WebWorld, World

from .items import *
from .data import *
from .locations import ty1_location_table, Ty1Location, ty1_location_name_groups
from .options import Ty1Options, ty1_option_groups
from .regions import create_regions, connect_regions, connect_all_regions
from .rules import set_rules


class Ty1Web(WebWorld):
    theme = "jungle"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Ty the Tasmanian Tiger 1 randomizer connected to an Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["xMcacutt", "Dashieswag92"]
    )

    tutorials = [setup_en]
    option_groups = ty1_option_groups


class Ty1World(World):
    """
    Ty the Tasmanian Tiger is a 3D platformer collectathon created by Australian developers Krome Studios.
    Play as Ty and travel the Australian outback to snowy mountains to defeat Boss Cass and rescue your family from The Dreaming.
    """
    game: str = "Ty the Tasmanian Tiger"
    options_dataclass = Ty1Options
    options: Ty1Options
    topology_present = True
    item_name_to_id = {name: item.code for name, item in ty1_item_table.items()}
    location_name_to_id = {name: item.code for name, item in ty1_location_table.items()}
    region_name_to_code = {name: code for code, name in ty1_levels.items()}
    portal_map: List[int] = [Ty1LevelCode.A1.value, Ty1LevelCode.A2.value, Ty1LevelCode.A3.value,
                                    Ty1LevelCode.B1.value, Ty1LevelCode.B2.value, Ty1LevelCode.B3.value,
                                    Ty1LevelCode.C1.value, Ty1LevelCode.C2.value, Ty1LevelCode.C3.value]
    item_name_groups = ty1_item_name_groups
    location_name_groups = ty1_location_name_groups
    trap_weights = {}

    web = Ty1Web()

    # UT Stuff Here
    ut_can_gen_without_yaml = True

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.itempool = []
        self.portal_map = [Ty1LevelCode.A1.value, Ty1LevelCode.A2.value, Ty1LevelCode.A3.value,
                           Ty1LevelCode.B1.value, Ty1LevelCode.B2.value, Ty1LevelCode.B3.value,
                           Ty1LevelCode.C1.value, Ty1LevelCode.C2.value, Ty1LevelCode.C3.value]

    def fill_slot_data(self):
        return {
            "ModVersion": "1.4.0",
            "Goal": self.options.goal.value,
            "ProgressiveElementals": self.options.progressive_elementals.value,
            "ProgressiveLevel": self.options.progressive_level.value,
            "LevelUnlockStyle": self.options.level_unlock_style.value,
            "TheggGating": self.options.thegg_gating.value,
            "CogGating": self.options.cog_gating.value,
            "ReqBosses": self.options.req_bosses.value,
            "GateTimeAttacks": self.options.gate_time_attacks.value,
            "PortalMap": self.portal_map,
            "FramesRequireInfra": self.options.frames_require_infra.value,
            "Scalesanity": self.options.scalesanity.value,
            "Signsanity": self.options.signsanity.value,
            "Lifesanity": self.options.lifesanity.value,
            "Framesanity": self.options.framesanity.value,
            "Opalsanity": self.options.opalsanity.value,
            "AdvancedLogic": self.options.logic_difficulty.value,
            "DeathLink": self.options.death_link.value,
            "MulTyLink": self.options.mul_ty_link.value,
            "ExtraTheggs": self.options.extra_theggs.value,
            "ExtraCog": self.options.extra_cogs.value,
        }

    def generate_early(self) -> None:
        self.handle_ut_yamless(None)
        extra_thegg_count = self.options.extra_theggs.value * 3
        extra_cog_count = self.options.extra_cogs.value

        if extra_thegg_count + self.options.thegg_gating.value * 3 > 72:
            raise OptionError("[Ty the Tasmanian Tiger] More than 72 theggs added to the pool.")

        if extra_cog_count + self.options.cog_gating.value * 6 > 90:
            raise OptionError("[Ty the Tasmanian Tiger] More than 90 cogs added to the pool.")

        self.trap_weights = {
            "Knocked Down Trap": self.options.knocked_down_trap_weight.value,
            "Slow Trap": self.options.slow_trap_weight.value,
            "Gravity Trap": self.options.gravity_trap_weight.value,
            "Acid Trap": self.options.acid_trap_weight.value,
            "Exit Trap": self.options.exit_trap_weight.value,
        }
        if self.options.opalsanity:
            self.options.local_items.value.add("Picture Frame")

    def create_item(self, name: str) -> Item:
        item_info = ty1_item_table[name]
        return Ty1Item(name, item_info.classification, item_info.code, self.player)

    def create_items(self):
        create_items(self)

    def create_event(self, region_name: str, event_name: str) -> None:
        region: Region = self.multiworld.get_region(region_name, self.player)
        loc: Ty1Location = Ty1Location(self.player, event_name, None, region)
        loc.place_locked_item(Ty1Item(event_name, ItemClassification.progression, None, self.player))
        region.locations.append(loc)

    def create_regions(self):
        create_regions(self)
        self.create_event("Bull's Pen", "Beat Bull")
        self.create_event("Crikey's Cove", "Beat Crikey")
        self.create_event("Fluffy's Fjord", "Beat Fluffy")
        self.create_event("Cass' Crest", "Beat Shadow")
        self.create_event("Final Battle", "Beat Cass")
        connect_all_regions(self, self.portal_map)

    def set_rules(self):
        set_rules(self)

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        new_hint_data = {}

        for key, data in ty1_location_table.items():
            try:
                location: Location = self.multiworld.get_location(key, self.player)
            except KeyError:
                continue
            region_name: str = data.region
            containing_level_code: Ty1LevelCode = self.region_name_to_code.get(region_name)
            if containing_level_code is None or containing_level_code not in ty1_core_levels:
                continue

            try:
                level_index: int = self.portal_map.index(containing_level_code.value)
            except ValueError:
                continue

            portal_code: int = level_index + 4
            if level_index > 5:
                portal_code = portal_code + 2
            elif level_index > 2:
                portal_code = portal_code + 1

            try:
                portal_name: str = ty1_levels_short[Ty1LevelCode(portal_code)]
            except ValueError:
                continue

            new_hint_data[location.address] = f"{portal_name} Portal"
            hint_data[self.player] = new_hint_data

    def get_filler_item_name(self) -> str:
        return get_junk_item_names(self.random, 1)[0]

    def handle_ut_yamless(self, slot_data: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:

        if not slot_data \
                and hasattr(self.multiworld, "re_gen_passthrough") \
                and isinstance(self.multiworld.re_gen_passthrough, dict) \
                and self.game in self.multiworld.re_gen_passthrough:
            slot_data = self.multiworld.re_gen_passthrough[self.game]

        if not slot_data:
            return None

        # fill in options
        self.options.goal.value = slot_data["Goal"]
        self.options.progressive_elementals.value = slot_data["ProgressiveElementals"]
        self.options.progressive_level.value = slot_data["ProgressiveLevel"]
        self.options.level_unlock_style.value = slot_data["LevelUnlockStyle"]
        self.options.thegg_gating.value = slot_data["TheggGating"]
        self.options.cog_gating.value = slot_data["CogGating"]
        self.options.req_bosses.value = slot_data["ReqBosses"]
        self.options.gate_time_attacks.value = slot_data["GateTimeAttacks"]
        self.portal_map = slot_data["PortalMap"]
        self.options.frames_require_infra.value = slot_data["FramesRequireInfra"]
        self.options.scalesanity.value = slot_data["Scalesanity"]
        self.options.signsanity.value = slot_data["Signsanity"]
        self.options.lifesanity.value = slot_data["Lifesanity"]
        self.options.framesanity.value = slot_data["Framesanity"]
        self.options.opalsanity.value = slot_data["Opalsanity"]
        self.options.logic_difficulty.value = slot_data["AdvancedLogic"]
        self.options.death_link.value = slot_data["DeathLink"]
        self.options.mul_ty_link.value = slot_data["MulTyLink"]
        self.options.extra_theggs.value = slot_data["ExtraTheggs"]
        self.options.extra_cogs.value = slot_data["ExtraCog"]

        return slot_data

    def generate_output(self, output_directory: str):
        pass
    # def pre_fill(self) -> None:
    #     visualize_regions(self.multiworld.get_region("Menu", self.player), f"Player{self.player_name}.puml",
    #                       show_entrance_names=True,
    #                       regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
    #                           self.player])