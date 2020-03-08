from items import *
from swords import *

SMELT_RECIPES = {
    Steel: (Iron, 120),
    HotGold: (GoldIngot, 140),
    HotPlat: (PlatIngot, 160)
}

HAMMER_RECIPES = {
    BasicSword: (Steel, 60),
    GoldSword: (HotGold, 80),
    PlatSword: (HotPlat, 100)
}

GRINDER_RECIPES = {
    SharpBasicSword: (BasicSword, 100),
    SharpGoldSword: (GoldSword, 120),
    SharpPlatSword: (PlatSword, 140)
}