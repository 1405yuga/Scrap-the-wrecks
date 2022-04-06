
from genericpath import exists
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime,timedelta

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

#numberp="MH01AV886"
def checkInfo(numberp):
    result=db.collection("NumberPlate").document(numberp).get()

    if result:
        #get registration date
        d=result.to_dict()["registrationDate"]
        string_date=str(d).split(" ")[0]
        print(string_date)
        date=datetime.strptime(string_date,'%Y-%m-%d')+timedelta(days=1)

        #get current date
        today=date.today()

        #cal difference 
        gap=today-date
        gap=gap.days/365.25
        print(gap)

        #check 15 years or above
        if(gap>=15):
            #needs to scrap
            ownerName=result.to_dict()["ownerName"]
            phone=result.to_dict()["mobile"]
            print(ownerName+" ",phone)
            return ownerName,phone
        else:
            return "noScrap",""
        
    else:
        return "noDB",""
        

#o,p=checkInfo(numberp)
#print(o)