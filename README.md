AlfredSmartAppWorkflow
======================

An Alfred Workflow that works with a SmartThings SmartApp


#To install#
* Install the "Alfred Workflow" SmartApp from the Connections category on your mobile device.  Choose the switches that you wish to be controllable through Alfred.

#Currently Supported Commands#
* `st_login` will take you through the login process
* `st_logout` will destroy your auth token
* `st ` will collect the devices specified in all of your installed smartapp instances
* `st on`, followed by selecting the desired device, will turn it on
* `st off`, followed by selecting the desired device, will turn it off


#Updating the workflow#
1. Open Alfred Preferences `cmd+space` (or whatever you have set to open alfred) followed by `cmd+,`
2. In the `Workflows` section, select `SmartThings`, then select the `-` at the bottom to remove the workflow
3. In the project directory, run the `bundle.sh` script
4. double-click the `SmartThings.alfredworkflow` file to install it


#Logging while developing#
Alfred doesn't give you any output that I know of. I have been creating an `output.txt` file and writing my logs to that. To find the installed directory, open `Alfred Preferences`, double-click any of the script steps, and select `Open workflow folder` from the bottom-right of the window.
