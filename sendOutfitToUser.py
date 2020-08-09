import time
import schedule
import twilioinfo
from twilio.rest import Client
from clothingItem import ClothingCategory
from outfitCollection import OutfitCollection
from collectionModifiers import addItemsToCollection

client = Client(twilioinfo.accountId, twilioinfo.apiKey)

fromNumber = "whatsapp:"+twilioinfo.twillioNumber
toNumber = "whatsapp:"+twilioinfo.myPhoneNumber

collection = OutfitCollection()
addItemsToCollection(collection)

def getOutfit():
    outfit = collection.getOutfit()
    outfitMessage = """
        Your outfit for the day -

    Upper Wear: {0}
    Lower Wear: {1}

Have a great day :).
    """.format(outfit[0].name, outfit[1].name)
    client.messages.create(body=outfitMessage, from_=fromNumber, to=toNumber)

schedule.every().day.at("8:30").do(getOutfit)

while True:
    schedule.run_pending()
    time.sleep(1)