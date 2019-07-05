The following directory is really just a utility directory for exporting and importing environment variables.  
There is also a SpotDefaults for reference.  There is an empty set of environment variables (PC_Empty), these need values for Spotter to work
properly.  I have built-in logic in the menu to make them alert, if the API keys are not populated for instance.  
I am still working with how to set these persistently for Linux in the interim you can run the Linux_empty after you populate it's values at the term line
I also created a callable module for setting these at run time in python for Linux, but they are not persistent and when you exit the menu the values would drop too.


If you want to get a JSON capture of your "secrets" that are stored in the env variables then run this script (SpotConfigs) and it will output them to a JSON file.  Careful of this file as it has your $$ Keys in it.

