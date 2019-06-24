This example code from WatchDog, allows for this Watcher script to output to your console window the files you have manipulated.  This script only watching the directory you launch, from which is why this needs to be copied too and launched from within the following path...
c:\[UserProfile]\NBEMS.files\ICS\messages\

You will need to install the Watcher module in python by running this command.
pip install watchdog

copy the Spot_FlMsgWatcher script to this folder, and by launching the script to get a console screen, it will capture all file changes in this directory will be recorded to console screen. The script can be refined to just watch for changed files only, which is probably more interesting to keep a log of the messages you have created to be sent for later submission of what you attempted to communicate.  This does not record whether the user attempted to send the file though.  There might be a way to do this but would require more research.

You can run this file from within the FLMsg folder and it will keep a running log of you activity of the folder for your records.  I will investigate creating a version that will generate this to a central logging server for NCS records.