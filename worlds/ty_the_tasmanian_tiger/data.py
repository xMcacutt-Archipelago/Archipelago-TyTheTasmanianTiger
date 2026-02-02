from enum import Enum


class Ty1LevelCode(Enum):
    Z1 = 0
    A1 = 4
    A2 = 5
    A3 = 6
    A4 = 7
    B1 = 8
    B2 = 9
    B3 = 10
    D4 = 19
    C1 = 12
    C2 = 13
    C3 = 14
    C4 = 15
    D1 = 16
    D2 = 17
    E1 = 20
    E2 = 21
    E3 = 22
    E4 = 23


ty1_core_levels = [Ty1LevelCode.A1, Ty1LevelCode.A2, Ty1LevelCode.A3,
                   Ty1LevelCode.B1, Ty1LevelCode.B2, Ty1LevelCode.B3,
                   Ty1LevelCode.C1, Ty1LevelCode.C2, Ty1LevelCode.C3]



ty1_levels: dict[Ty1LevelCode, str] = {
    Ty1LevelCode.Z1: "Rainbow Cliffs",
    Ty1LevelCode.A1: "Two Up",
    Ty1LevelCode.A2: "Walk in the Park",
    Ty1LevelCode.A3: "Ship Rex",
    Ty1LevelCode.A4: "Bull's Pen",
    Ty1LevelCode.B1: "Bridge on the River Ty",
    Ty1LevelCode.B2: "Snow Worries",
    Ty1LevelCode.B3: "Outback Safari",
    Ty1LevelCode.D4: "Crikey's Cove",
    Ty1LevelCode.C1: "Lyre, Lyre Pants on Fire",
    Ty1LevelCode.C2: "Beyond the Black Stump",
    Ty1LevelCode.C3: "Rex Marks the Spot",
    Ty1LevelCode.C4: "Fluffy's Fjord",
    Ty1LevelCode.D1: "Credits",
    Ty1LevelCode.D2: "Cass' Crest",
    Ty1LevelCode.E1: "Cass' Pass",
    Ty1LevelCode.E2: "Final Battle",
    Ty1LevelCode.E3: "Bonus World 1",
    Ty1LevelCode.E4: "Bonus World 2"
}

ty1_levels_short: dict[Ty1LevelCode, str] = {
    Ty1LevelCode.Z1: "Rainbow Cliffs",
    Ty1LevelCode.A1: "Two Up",
    Ty1LevelCode.A2: "WitP",
    Ty1LevelCode.A3: "Ship Rex",
    Ty1LevelCode.A4: "Bull's Pen",
    Ty1LevelCode.B1: "BotRT",
    Ty1LevelCode.B2: "Snow Worries",
    Ty1LevelCode.B3: "Outback Safari",
    Ty1LevelCode.D4: "Crikey's Cove",
    Ty1LevelCode.C1: "LLPoF",
    Ty1LevelCode.C2: "BtBS",
    Ty1LevelCode.C3: "RMtS",
    Ty1LevelCode.C4: "Fluffy's Fjord",
    Ty1LevelCode.D1: "Credits",
    Ty1LevelCode.D2: "Cass' Crest",
    Ty1LevelCode.E1: "Cass' Pass",
    Ty1LevelCode.E2: "Bonus World 1",
    Ty1LevelCode.E3: "Bonus World 2",
    Ty1LevelCode.E4: "Final Battle",
}