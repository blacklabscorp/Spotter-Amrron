# Module load
from twilio.rest import Client

# Environment Variables
import os
twilioAccountSid=os.environ["s_twilioAccountSid"]
twilioAuthToken=os.environ["s_twilioAuthToken"]
twilioAmrronCell=os.environ["s_twilioAmrronCell"]
amrron00User=os.environ["s_amrron00User"]
amrron00Cell=os.environ["s_amrron00Cell"]
amrron01User=os.environ["s_amrron01User"]
amrron01Cell=os.environ["s_amrron01Cell"]
#amrron02User=os.environ["s_amrron02User"]
#amrron02Cell=os.environ["s_amrron02Cell"]
#amrron03User=os.environ["s_amrron03User"]
#amrron03Cell=os.environ["s_amrron03Cell"]
#amrron04User=os.environ["s_amrron04User"]
#amrron04Cell=os.environ["s_amrron04Cell"]
#amrron05User=os.environ["s_amrron05User"]
#amrron05Cell=os.environ["s_amrron05Cell"]
from Spot_OTP import *

# Transmit Menu
def TransmitMenu():
    twilioAccountSid=os.environ["s_twilioAccountSid"]
    twilioAuthToken=os.environ["s_twilioAuthToken"]
    twilioAmrronCell=os.environ["s_twilioAmrronCell"]
    amrron00User=os.environ["s_amrron00User"]
    amrron00Cell=os.environ["s_amrron00Cell"]
    amrron01User=os.environ["s_amrron01User"]
    amrron01Cell=os.environ["s_amrron01Cell"]
    print('T R A N S M I T  M E N U')
    print('_________________________')
    print()
    while True:
        print('Option: [M] Return to Main Inputs')
        print('Option: [00T] ',amrron00User,' SMS delivery')
        print('Option: [00P] ',amrron00User,' Phone delivery')
        print('Option: [01T] ',amrron01User,' SMS Delivery')
        print('Option: [01P] ',amrron01User,' Phone Delivery')
        print('Option: [CAT] All CA SMS Delivery')
        print('Option: [CAP] All CA Phone Delivery')
        print('Option: [OTP] One Time Pad practice')
        transmitMenu=input ('Which option would you like...')        
        if transmitMenu=="M":
            print()
            break
        if transmitMenu=="00T":
            print()
            print('Off to Transmit...')
            print()
            Transmit(transmitMenu)
            break
        if transmitMenu=="00P":
            print()
            print('Off to Transmit...')
            print()
            Transmit(transmitMenu)
            break
        if transmitMenu=="01T":
            print()
            print('Off to Transmit...')
            print()
            Transmit(transmitMenu)
            break
        if transmitMenu=="01P":
            print()
            print('Off to Transmit...')
            print()
            Transmit(transmitMenu)
            break
        if transmitMenu=="CAT":
            print()
            print('Off to Transmit...')
            print()
            Transmit(transmitMenu)
        if transmitMenu=="CAP":
            print()
            print('Off to Transmit...')
            print()
            Transmit(transmitMenu)
        if transmitMenu=='OTP':
            print()
            print('[OTP] One Time Pad (experimental / Table CT NO 1 English)')
            otp_main()
            ctno1english()
            padin()
            padout()
            break
        return None

# Function: Transmit
def Transmit(transmitMenu):
    comm=transmitMenu
    if comm=="00T":
        # Message 
        # Function: Twilio Web Service for SMS
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        message = client.messages \
                    .create(
                        body="Amrron Alert: Spot Report",

                         from_=twilioAmrronCell,

                         to=amrron00Cell
                     )
        print(message.sid)
    if comm=="00P":
        # Message 
        # Function: Twilio Web Service for Phone
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        call = client.calls.create(
           url='https://handler.twilio.com/twiml/EH2a4e1f4ff24ac11ba56d0f147b850c97',
                        to=amrron00Cell,
                        from_=twilioAmrronCell
                    )
        print(call.sid)
    if comm=="01T":
        # Message 
        # Function: Twilio Web Service for SMS
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        message = client.messages \
                    .create(
                         body="Amrron Alert: Spot Report",
                         from_=twilioAmrronCell,
                         to=amrron01Cell
                     )
        print(message.sid)
    if comm=="01P":
        # Message 
        # Function: Twilio Web Service for Phone
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        call = client.calls.create(
           url='https://handler.twilio.com/twiml/EH2a4e1f4ff24ac11ba56d0f147b850c97',
                        to=amrron01Cell,
                        from_=twilioAmrronCell
                    )
        print(call.sid)
    if comm=="02T":
        # Message 
        # Function: Twilio Web Service for SMS
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        message = client.messages \
                    .create(
                         body="Amrron Alert: Spot Report to Amrron 02",
                         from_=twilioAmrronCell,
                         to=amrron02Cell
                     )
        print(message.sid)
    if comm=="02P":
        # Message 
        # Function: Twilio Web Service for Phone
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        call = client.calls.create(
           url='https://handler.twilio.com/twiml/EH2a4e1f4ff24ac11ba56d0f147b850c97',
                        to=amrron02Cell,
                        from_=twilioAmrronCell
                    )
        print(call.sid)

    if comm=="03T":
        # Message 
        # Function: Twilio Web Service for SMS
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        message = client.messages \
                    .create(
                         body="Amrron Alert: Spot Report to Amrron 03",
                         from_=twilioAmrronCell,
                         to=amrron03Cell
                     )
        print(message.sid)
    if comm=="03P":
        # Message 
        # Function: Twilio Web Service for Phone
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        call = client.calls.create(
           url='https://handler.twilio.com/twiml/EH2a4e1f4ff24ac11ba56d0f147b850c97',
                        to=amrron03Cell,
                        from_=twilioAmrronCell
                    )
        print(call.sid)


    if comm=="04T":
        # Message 
        # Function: Twilio Web Service for SMS
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        message = client.messages \
                    .create(
                         body="Amrron Alert: Spot Report to Amrron 04",
                         from_=twilioAmrronCell,
                         to=amrron04Cell
                     )
        print(message.sid)
    if comm=="04P":
        # Message 
        # Function: Twilio Web Service for Phone
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        call = client.calls.create(
           url='https://handler.twilio.com/twiml/EH2a4e1f4ff24ac11ba56d0f147b850c97',
                        to=amrron04Cell,
                        from_=twilioAmrronCell
                    )
        print(call.sid)
    if comm=="05T":
        # Message 
        # Function: Twilio Web Service for SMS
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        message = client.messages \
                    .create(
                         body="Amrron Alert: Spot Report to Amrron 05",
                         from_=twilioAmrronCell,
                         to=amrron05Cell
                     )
        print(message.sid)
    if comm=="05P":
        # Message 
        # Function: Twilio Web Service for Phone
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        call = client.calls.create(
           url='https://handler.twilio.com/twiml/EH2a4e1f4ff24ac11ba56d0f147b850c97',
                        to=amrron05Cell,
                        from_=twilioAmrronCell
                    )
        print(call.sid)
    if comm=="CAT":
        # Message 
        # Function: Twilio Web Service for SMS
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        message = client.messages \
                    .create(
                         body="Amrron Alert: Spot Report to California Amrron",
                         from_=twilioAmrronCell,
                         to=romeo07
                     )
        print(message.sid)
    if comm=="CAP":
        # Message 
        # Function: Twilio Web Service for Phone
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        call = client.calls.create(
           url='https://handler.twilio.com/twiml/EH2a4e1f4ff24ac11ba56d0f147b850c97',
                        to=romeo07,
                        from_=twilioAmrronCell
                    )
        print(call.sid)
    return

#print('Test Block')
#TransmitMenu()

# Pre-Req libraries Install
# pip install twilio

