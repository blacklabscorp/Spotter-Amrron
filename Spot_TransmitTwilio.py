from Spot_Keys_PC import twilioAccountSid,twilioAuthToken,romeo07,oscarRomeo01,twilioAmrron
from twilio.rest import Client

# Function: Transmit
def Transmit(transmitMenu):
    comm=transmitMenu
    if comm=="OT":
        # Message 
        # Function: Twilio Web Service for SMS
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        message = client.messages \
                    .create(
                         body="Amrron Alert: Spot Report to Oscar Romeo 01",
                         from_=twilioAmrron,
                         to=oscarRomeo01
                     )
        print(message.sid)
    if comm=="OP":
        # Message 
        # Function: Twilio Web Service for SMS
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        call = client.calls.create(
           url='https://handler.twilio.com/twiml/EH2a4e1f4ff24ac11ba56d0f147b850c97',
                        to=oscarRomeo01,
                        from_=twilioAmrron
                    )
        print(call.sid)
    if comm=="RT":
        # Message 
        # Function: Twilio Web Service for SMS
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        message = client.messages \
                    .create(
                         body="Amrron Alert: Spot Report to Romeo 07",
                         from_=twilioAmrron ,
                         to=romeo07
                     )
        print(message.sid)
    if comm=="RP":
        # Message 
        # Function: Twilio Web Service for SMS
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        call = client.calls.create(
           url='https://handler.twilio.com/twiml/EH2a4e1f4ff24ac11ba56d0f147b850c97',
                        to=romeo07,
                        from_=twilioAmrron
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
                         from_=twilioAmrron,
                         to=romeo07
                     )
        print(message.sid)
    if comm=="CAP":
        # Message 
        # Function: Twilio Web Service for SMS
        # Auth method
        client = Client(twilioAccountSid, twilioAuthToken)
        call = client.calls.create(
           url='https://handler.twilio.com/twiml/EH2a4e1f4ff24ac11ba56d0f147b850c97',
                        to=romeo07,
                        from_=twilioAmrron
                    )
        print(call.sid)
