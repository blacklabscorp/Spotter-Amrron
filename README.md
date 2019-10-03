## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/blacklabscorp/Spotter-Amrron/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

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

1. s_accuWeatherKey		AccuWeather API Key (requires sign-up for API key from Accuweather)
1. s_googleKey			Google API Key (requires sign-up for API key from Accuweather)
s_OpenWeatherKey		Open Weather Key (requires sign-up for API key from OpenWeather)
s_twilioAccountSid		Twilio Username (requires sign-up for API key from Twilio)
s_twilioAmrronCell		Twilio phone number (+18005551212 format) (requires sign-up for API key from Twilio)
s_twilioAuthToken		Twilio password (requires sign-up for API key from Twilio)
s_adafruitIoName		AdafruitIo User Name
s_adafruitIoKey			AdafruitIO Key
s_DarkSkysKey			Alternative weather service Key
s_amrronDefaultWebServerUrl	Amrron web server for presentation tier (FUTURE FEATURE on AWS)
s_amrronDefaultWebServiceUrl	Amrron web service logger URL (FUTURE FEATURE on AWS)
s_amrronDefaultWebServiceKey	Amrron web service logger Key (FUTURE FEATURE on AWS)
s_callsignDefault		Your Default Callsign
s_cityStateDefault		Your Default City, State
s_postalcodeDefault		Your Default zip code
s_gridDefault			Your Default Grid
s_xDefault			Your Default Longitude
s_yDefault			Your Default Lattitude
s_dmrIdDefault			Your Default DMR Id
s_k2sDefault			This is a default file name defined for testing (has call sign in filename)
s_amrronDefaultUser		Amrron Default User name
s_amrronDefaultCell		Amrron Default User's cell ('+18005551212')
s_amrron00User			Optional Amrron user name
s_amrron00Cell			Optional Amrron user call
s_amrron00Email			Optional Amrron user email
s_amrron01User			Optional Amrron user name
s_amrron01Cell			Optional Amrron user call
s_amrron01Email			Optional Amrron user email
s_amrron02User			Optional Amrron user name
s_amrron02Cell			Optional Amrron user call
s_amrron02Email			Optional Amrron user email
s_amrron03User			Optional Amrron user name
s_amrron03Cell			Optional Amrron user call
s_amrron03Email			Optional Amrron user email
s_amrron04User			Optional Amrron user name
s_amrron04Cell			Optional Amrron user call
s_amrron04Email			Optional Amrron user email
s_amrron05User			Optional Amrron user name
s_amrron05Cell			Optional Amrron user call
s_amrron05Email			Optional Amrron user email
s_USGS


# Header 1
## Header 2
### Header 3

- List
s_accuWeatherKey		AccuWeather API Key (requires sign-up for API key from Accuweather)
s_googleKey			Google API Key (requires sign-up for API key from Accuweather)
s_OpenWeatherKey		Open Weather Key (requires sign-up for API key from OpenWeather)
s_twilioAccountSid		Twilio Username (requires sign-up for API key from Twilio)
s_twilioAmrronCell		Twilio phone number (+18005551212 format) (requires sign-up for API key from Twilio)
s_twilioAuthToken		Twilio password (requires sign-up for API key from Twilio)
s_adafruitIoName		AdafruitIo User Name
s_adafruitIoKey			AdafruitIO Key
s_DarkSkysKey			Alternative weather service Key
s_amrronDefaultWebServerUrl	Amrron web server for presentation tier (FUTURE FEATURE on AWS)
s_amrronDefaultWebServiceUrl	Amrron web service logger URL (FUTURE FEATURE on AWS)
s_amrronDefaultWebServiceKey	Amrron web service logger Key (FUTURE FEATURE on AWS)
s_callsignDefault		Your Default Callsign
s_cityStateDefault		Your Default City, State
s_postalcodeDefault		Your Default zip code
s_gridDefault			Your Default Grid
s_xDefault			Your Default Longitude
s_yDefault			Your Default Lattitude
s_dmrIdDefault			Your Default DMR Id
s_k2sDefault			This is a default file name defined for testing (has call sign in filename)
s_amrronDefaultUser		Amrron Default User name
s_amrronDefaultCell		Amrron Default User's cell ('+18005551212')
s_amrron00User			Optional Amrron user name
s_amrron00Cell			Optional Amrron user call
s_amrron00Email			Optional Amrron user email
s_amrron01User			Optional Amrron user name
s_amrron01Cell			Optional Amrron user call
s_amrron01Email			Optional Amrron user email
s_amrron02User			Optional Amrron user name
s_amrron02Cell			Optional Amrron user call
s_amrron02Email			Optional Amrron user email
s_amrron03User			Optional Amrron user name
s_amrron03Cell			Optional Amrron user call
s_amrron03Email			Optional Amrron user email
s_amrron04User			Optional Amrron user name
s_amrron04Cell			Optional Amrron user call
s_amrron04Email			Optional Amrron user email
s_amrron05User			Optional Amrron user name
s_amrron05Cell			Optional Amrron user call
s_amrron05Email			Optional Amrron user email
s_USGS

- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/blacklabscorp/Spotter-Amrron/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
