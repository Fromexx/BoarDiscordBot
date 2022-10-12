import enum

class ItemType(enum.Enum):
    Weapon = 0,
    Graffiti = 1,
    Sticker = 2,
    Patch = 3,
    Agent = 4,
    Key = 5,
    Container = 6,
    Music = 7,
    Knife = 8,
    Gloves = 9,
    Label = 10,
    Pass = 11,
    Souvenir = 12

class WeaponType(enum.Enum):
    Pistol = 0,
    Shotgun = 1,
    MachineGun = 2,
    SubmachineGun = 3,
    Rifle = 4,
    SniperRifle = 5
