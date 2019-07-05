The following directory is really just a utility directory for exporting and importing environment variables.  
There is also a SpotDefaults for reference.  There is an empty set of environment variables (PC_Empty), these need values for Spotter to work
properly.  I have built-in logic in the menu to make them alert, if the API keys are not populated for instance.  
I am still working with how to set these persistently for Linux in the interim you can run the Linux_empty after you populate it's values at the term line
I also created a callable module for setting these at run time in python for Linux, but they are not persistent and when you exit the menu the values would drop too.


If you want to get a JSON capture of your "secrets" that are stored in the env variables then run this script (SpotConfigs) and it will output them to a JSON file.  
Careful of this file as it has your $$ Keys in it.


Here's some notes on the PC Install...


PC Environment readiness / Installation instructions

Install GitHub and sync down the Spotter-Amrron repository @ c:/spotter-amrron 
Install Python 3.7.3 64 bit (not default for Windows as this is 32 Bit)
Install pip3 install
	-upgrade the install for Pip3
Install Virtualenv
	-activate the virtualenv by running 
		virtualenv spotter
		./activate.bat inside the c:/spotter/Scripts folder this create completes virtualenv for Spotter setup
		You should now see (spotter) in front of your command prompt this is now active
Create an installation folder called spot from c:/spotter-amrron and drop into the c:/spotter/ directory
Pip3 install -r requirements.txt from within the c:/spotter/ directory
	pip3 install -r c:\spotter\spot\SpotConfigs\requirements.txt
Warm set the variables with the batch script from c:/spotter/spot/SpotConfigs/PC_Empty.bat 
	Or correct the values before running this script
Test python with a local JSON output of your environment variables.

Restarting Spotter
Cmd prompt yourself to the c:/spotter/ folder
Launch the activate command to start the virtualenv
	c:/spotter/Scripts/activate.bat
	Go into the root applications folder c:/spotter/spot and launch the following script
		Spot_Main.py


Here's some notes on the Ubuntu install....

3.7.3 update
Sudo apt update
sudo apt update
sudo apt install software-properties-common

Sudo add-apt-repository ppa:deadsnakes/ppa
Sudo apt install python 3.7

-Install Virtualenv https://virtualenv.pypa.io/en/latest/userguide/
-Download via git spotter-amrron
-create spotter folder 
-virtualenv --python=/usr/bin/python3.7 spotter
Source ./activate at the ~/spotter/bin dir
-copy the Spot folder into /spotter/bin/spot

3] pip3 install –r requirements.txt
4] python3.7 Spot_RPIConfigs.py
5] python3.7 Spot_MainRPI.py

If needed install the following apps via sudo apt install 
-Sudo Apt install the following apps: Fldigi, FLAmp, FLMsg, FLWrap