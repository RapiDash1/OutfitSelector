from clothingItem import ClothingCategory, ClothingItem, ClothingType
import logging
import random
import json

class OutfitCollection():

    def readLastSavedClothes(self):
        f = open("lastUsedClothes.json", "r")
        return json.loads(f.read())

    def __init__(self):
        self.upperWearCollection = []
        self.lowerWearCollection = []
        self.alreadyUsedOutfits = []
        self.previouislyUsedOutfits = self.readLastSavedClothes()
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

        self.previouislyUsedOutfits.append([upperWear.name, lowerWear.name])
        # logging.info("U: " + str(upperWear) + " L: " + str(lowerWear))
        return (upperWear, lowerWear)
    
    def releaseEarliestUsedClothes(self):
        self.previouislyUsedOutfits.pop(0)
        self.updateLastUsedClothes()

    def updateLastUsedClothes(self):
        f = open("lastUsedClothes.json", "w")
        f.write(json.dumps(self.previouislyUsedOutfits))

    def getOutfit(self, fancy=False):
        todaysOutfit = self.selectOutfit(fancy)
        if len(self.previouislyUsedOutfits) > 2:
            self.releaseEarliestUsedClothes()
        return todaysOutfit

    def checkElementInPrevList(self, itemName, upper=True):
        for outfit in self.previouislyUsedOutfits:
            if upper:
                if outfit[0] == itemName:
                    return False
            else:
                if outfit[1] == itemName:
                    return False
        return True


