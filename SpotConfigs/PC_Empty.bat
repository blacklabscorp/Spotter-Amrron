REM required variables for spotter, just add your value in "" next to the variable below with a space in between to set the env variables.
setx s_callsignDefault "ChangeMe"
setx s_dmrIdDefault "ChangeMe"
setx s_cityStateDefault "ChangeMe"
setx s_xDefault "ChangeMe"
setx s_yDefault "ChangeMe"
setx s_gridDefault "ChangeMe"
setx s_postalcodeDefault "ChangeMe"
setx s_k2sDefault "ChangeMe"

setx s_amrron00User "ChangeMe"
setx s_amrron01User "ChangeMe"
setx s_amrron00Cell "ChangeMe"
setx s_amrron01Cell "ChangeMe"
setx s_amrron00Email "ChangeMe"
setx s_amrron01Email "ChangeMe"

REM To use the web services in spotter you need to procure your key from these vendors, some are free for low # calls, others are not that expensive
REM PROTECT YOUR API KEYS as they will cost you if compromised (My checked in key ran up $200 overnight on Twilio), 
REM GitHub has enemy bots that look for Keys and steal them when accidently checked in which is so regular they now have a service to proactive bot code to look for the mistake and alert you in email.
REM Google has good lockdown configurability; Twilio does as well but leaves you default at risk. OpenWeather is less of a target.

setx s_googleKey "ChangeMe"
setx s_openWeatherKey "ChangeMe"
setx s_accuWeatherKey "ChangeMe"
setx s_twilioAccountSid "ChangeMe"
setx s_twilioAmrronCell "ChangeMe"
setx s_twilioAuthToken "ChangeMe"