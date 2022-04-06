#+19126122194
from twilio.rest import Client

account_sid="AC454ef3886af69d20a97a631288a1153c"
auth_token="72ec7ac0d37975e222f33bbc15588659"

client=Client(account_sid, auth_token)

def sms(numberp,ownerName,phone):
    to_number=str(phone)
    to_number="+91 "+to_number
    msg=client.messages.create(
        body="Dear "+ownerName+" your Vehicle No.:"+numberp+" has been exceeded the date of expiration as it is over 15years of manufactured date and hence needs to be scrapped according to rules and regulations of RTO",
        from_="+19126122194",
        to=to_number
    )

    print(msg.sid)
    

#sms("123456","Yuga",9307156651)