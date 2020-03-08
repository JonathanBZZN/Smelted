from items import *
from swords import *
from Shield import SteelShield

SMELT_RECIPES = {

    Steel: ([Iron], 200),
    BigSteel: ([Iron, Iron], 150),
    HotGold: ([GoldIngot], 140),
    HotPlat: ([PlatIngot], 160)

}

HAMMER_RECIPES = {
    BasicSword: (Steel, 60),
    GoldSword: (HotGold, 80),
    PlatSword: (HotPlat, 100),
    SteelShield: (BigSteel, 100)
}

GRINDER_RECIPES = {
    SharpBasicSword: (BasicSword, 100),
    SharpGoldSword: (GoldSword, 120),
    SharpPlatSword: (PlatSword, 140)
}