## Spotter Readme

# PIP Install manual runs, if not using setup.py

These additional libraries will need to be installed in addition to Python 3.7.3
pip install --upgrade pip

Twilio library for SMS and phone integrations
pip install twilio

Beautiful Soup for Html/XML scrapping
pip install bs4

Http Requests
pip install request or requests

Open Weather Wrapper for python interfacing to OpenWeather
pip install pyowm
usage notes: https://pyowm.readthedocs.io/en/latest/usage-examples-v2/weather-api-usage-examples.html

Objectpath use for walking an XML file
Pip install objectpath

PYQRCode for purposes of creating a QRcode for obscuring the target location from plain site; experimentation for stenography
Pip Install pyqrcode

WatchDog for file directory auditing; will be used in automation of base
PIP install watchdog

Out of working directory where the application will be installed, create a subdirectory called SpotData this is where output files will go.

The following environment variables are used to isolate PII or sensitive key information to memory so as to be less likely to be mistakenly uploaded to repository.  The Input menu has an ability to export these sensitive environment variables to a JSON to allow for easier transportability across platforms.

These are the variables name you'll want to populate with data.
# Path or Environment variables 
These are the required environmen path or variables (windows) that are needed for configuration of the application.  If the API key variables is not present, the menu will handle this condition and mark menu accordingly that the feature is unavailable.

1. s_accuWeatherKey		AccuWeather API Key (requires sign-up for API key from Accuweather)
1. s_googleKey			Google API Key (requires sign-up for API key from Accuweather)
1. s_OpenWeatherKey		Open Weather Key (requires sign-up for API key from OpenWeather)
1. s_twilioAccountSid		Twilio Username (requires sign-up for API key from Twilio)
1. s_twilioAmrronCell		Twilio phone number (+18005551212 format) (requires sign-up for API key from Twilio)
1. s_twilioAuthToken		Twilio password (requires sign-up for API key from Twilio)
1. s_adafruitIoName		AdafruitIo User Name
1. s_adafruitIoKey			AdafruitIO Key
1. s_DarkSkysKey			Alternative weather service Key
1. s_amrronDefaultWebServerUrl	Amrron web server for presentation tier (FUTURE FEATURE on AWS)
1. s_amrronDefaultWebServiceUrl	Amrron web service logger URL (FUTURE FEATURE on AWS)
1. s_amrronDefaultWebServiceKey	Amrron web service logger Key (FUTURE FEATURE on AWS)
1. s_callsignDefault		Your Default Callsign
1. s_cityStateDefault		Your Default City, State
1. s_postalcodeDefault		Your Default zip code
1. s_gridDefault			Your Default Grid
1. s_xDefault			Your Default Longitude
1. s_yDefault			Your Default Lattitude
1. s_dmrIdDefault			Your Default DMR Id
1. s_k2sDefault			This is a default file name defined for testing (has call sign in filename)
1. s_amrronDefaultUser		Amrron Default User name
1. s_amrronDefaultCell		Amrron Default User's cell ('+18005551212')
1. s_amrron00User			Optional Amrron user name
1. s_amrron00Cell			Optional Amrron user call
1. s_amrron00Email			Optional Amrron user email
1. s_amrron01User			Optional Amrron user name
1. s_amrron01Cell			Optional Amrron user call
1. s_amrron01Email			Optional Amrron user email
1. s_amrron02User			Optional Amrron user name
1. s_amrron02Cell			Optional Amrron user call
1. s_amrron02Email			Optional Amrron user email
1. s_amrron03User			Optional Amrron user name
1. s_amrron03Cell			Optional Amrron user call
1. s_amrron03Email			Optional Amrron user email
1. s_amrron04User			Optional Amrron user name
1. s_amrron04Cell			Optional Amrron user call
1. s_amrron04Email			Optional Amrron user email
1. s_amrron05User			Optional Amrron user name
1. s_amrron05Cell			Optional Amrron user call
1. s_amrron05Email			Optional Amrron user email
1. s_USGS


## Header 2
### Header 3
**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/blacklabscorp/Spotter-Amrron/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
