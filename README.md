SmartThings-Alfred
======================

An Alfred Workflow that allows you to control your physical graph through Alfred V2 (http://www.alfredapp.com)


#Currently Supported Commands#
* `st_login` will take you through the login process
* `st_logout` will destroy your auth token
* `st ` will collect the devices specified in all of your installed smartapp instances
* `st on`, followed by selecting the desired device, will turn it on
* `st off`, followed by selecting the desired device, will turn it off


#Installing the most recent version#
1. [Download SmartThings.alfredworkflow](https://github.com/PhysicalGraph/SmartThings-Alfred/wiki/Downloads)
2. double-click the `SmartThings.alfredworkflow` file to install it


#Updating the workflow#
1. Open Alfred Preferences `cmd+space` (or whatever you have set to open alfred) followed by `cmd+,`
2. In the `Workflows` section, select `SmartThings`, then select the `-` at the bottom to remove the workflow
3. In the project directory, run the `bundle.sh` script
4. double-click the `SmartThings.alfredworkflow` file to install it


#Tips for developing#
###Finding the installed directory###
To find the installed directory, open `Alfred Preferences`, double-click any of the script steps, and select `Open workflow folder` from the bottom-right of the window.

###Logging###
Alfred doesn't give you any output that I know of. I have been creating an `output.txt` file and writing my logs to that. The `output.txt` file will be created in the `installed directory`.

###Editing###
You may find it easier to make changes directly in the `installed directory` because any changes you make there will be reflected in Alfred immediately. Just make sure you don't copy any generated files back to your git directory (or at the very least don't commit them). We like to keep things clean :)
