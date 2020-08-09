from enum import Enum, unique

@unique
class ClothingType(Enum):
    UpperWear = 0
    LowerWear = 1


@unique
class ClothingCategory(Enum):
    Daily = 0
    Fancy = 1


class ClothingItem():

    def __init__(self, name, category, itemType):
        self.itemType = itemType
        self.category = category
        self.name = name

    def __str__(self):
        return self.name + " is a " + str(self.category) + " " + str(self.itemType)

    def __repr__(self):
        return "<ClothingItem> Name: {0}, Category: {1}, Type: {2}".format(self.name, self.category, self.itemType)