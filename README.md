# OutfitSelector

This app selects your outfit for the day, so that you don't have to.

Host this app on the cloud and run it daily at your preferred time to get your outfit for the day.

---

## Getting Started

### Prerequisites

* Clone this repo to your local machine.
* Install python if you havent.
* Install the 3rd party python modules - 
    * `pip install -r requirements.txt`
* Login to twilio and try out their WhatsApp sandbox.
    * https://www.twilio.com/console/sms/whatsapp/learn

### Initial Setup

* Create `twilioinfo.py` file.
    * Populate the following infomration in it - \
        `myPhoneNumber = "<Your Phone Number>"` \
        `twillioNumber = "<Twilio Sandbox Number>"` \
        `accountId = "<Your Account ID>"` \
        `apiKey = "<Your API Key>"`

* Create `yourClothes.py` file.
    * Populate the following infomration in it - \
        `dailyUpperWearItemList = ["itemOne", "itemTwo"......]` \
        `dailyLowerWearItemList = ["itemOne", "itemTwo"......]`

### Running the app

* `python sendOutfitToUser.py`

---

## Author

* RapiDash1





