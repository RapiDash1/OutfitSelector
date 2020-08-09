from clothingItem import ClothingCategory, ClothingItem, ClothingType
import logging
import random

class OutfitCollection():

    def __init__(self):
        self.upperWearCollection = []
        self.lowerWearCollection = []
        self.alreadyUsedOutfits = []
        self.previouislyUsedOutfits = []
        self.upperWearCollectionSize = 0
        self.lowerWearCollectionSize = 0
        logging.basicConfig(level=logging.DEBUG)
    
    def addClothingItemToCollection(self, newClothingItem: ClothingItem):
        if newClothingItem.itemType == ClothingType.UpperWear:
            self.upperWearCollection.append(newClothingItem)
            self.upperWearCollectionSize += 1
            logging.info("{0} added to upperWearCollection".format(str(newClothingItem)))
        else:
            self.lowerWearCollection.append(newClothingItem)
            self.lowerWearCollectionSize += 1
            logging.info("{0} added to lowerWearCollection".format(str(newClothingItem)))

    def selectOutfit(self, fancy=False):
        upperWear = self.upperWearCollection[int(random.random()*self.upperWearCollectionSize)]
        lowerWear = self.lowerWearCollection[int(random.random()*self.lowerWearCollectionSize)]
        while not self.checkElementInPrevList(upperWear.name):
            upperWear = self.upperWearCollection[int(random.random()*self.upperWearCollectionSize)]
        while not self.checkElementInPrevList(lowerWear.name, False):
            lowerWear = self.lowerWearCollection[int(random.random()*self.lowerWearCollectionSize)]

        self.previouislyUsedOutfits.append([upperWear, lowerWear])
        # logging.info("U: " + str(upperWear) + " L: " + str(lowerWear))
        return (upperWear, lowerWear)
    
    def releaseEarliestUsedClothes(self):
        self.previouislyUsedOutfits.pop(0)

    def getOutfit(self, fancy=False):
        todaysOutfit = self.selectOutfit(fancy)
        if len(self.previouislyUsedOutfits) > 2:
            self.releaseEarliestUsedClothes()
        return todaysOutfit

    def checkElementInPrevList(self, itemName, upper=True):
        for outfit in self.previouislyUsedOutfits:
            if upper:
                if outfit[0].name == itemName:
                    return False
            else:
                if outfit[1].name == itemName:
                    return False
        return True


