# Constants: Keys worth protecting
twilioAccountSid=""
twilioAuthToken=""
twilioAmrron=""
oscarRomeo01=""
romeo07=""
callsign=""
callsignDefault=''
dmrIdDefault=

# Constants: Google API Key
googleKey="A"

import os
def Spot_Env():
    os.environ["twilioAccountSid"] = twilioAccountSid
    os.environ["twilioAuthToken"] = twilioAuthToken
    os.environ["twilioAmrron"] = twilioAmrron
    os.environ["googleKey"] = googleKey
    os.environ["OscarRomeo01"] = oscarRomeo01
    os.environ["Romeo07"] = romeo07
    os.environ["dmrIdDefaults"]=dmrIdDefaults
