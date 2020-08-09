from clothingItem import ClothingCategory, ClothingItem, ClothingType
from yourClothes import dailyUpperWearItemList, dailyLowerWearItemList

def dailyUpperWearItem(name):
    return ClothingItem(name, ClothingCategory.Daily, ClothingType.UpperWear)

def alldailyUpperWearItems():
    return [dailyUpperWearItem(itemName) for itemName in dailyUpperWearItemList]

def dailyLowerWearItem(name):
    return ClothingItem(name, ClothingCategory.Daily, ClothingType.LowerWear)

def alldailyLowerWearItems():
    return [dailyLowerWearItem(itemName) for itemName in dailyLowerWearItemList]

def addItemsToCollection(collection):
    upperWearItems = alldailyUpperWearItems()
    lowerWearItems = alldailyLowerWearItems()

    for upperWearItem in upperWearItems:
        collection.addClothingItemToCollection(upperWearItem)
    for lowerWearItem in lowerWearItems:
        collection.addClothingItemToCollection(lowerWearItem)
