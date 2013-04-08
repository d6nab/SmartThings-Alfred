AlfredSmartAppWorkflow
======================

An Alfred Workflow that works with a SmartThings SmartApp


#To install#
1. Download and install the workflow: https://github.com/vlaminck/AlfredSmartAppWorkflow/blob/master/SmartThings.alfredworkflow?raw=true
2. Create a smartApp at http://graph.api.smartthings.com/ide/apps using smartApp.groovy: https://github.com/vlaminck/AlfredSmartAppWorkflow/blob/master/smartApp.groovy


#Currently Supported Commands#
`st_login` will take you through the login process
`st_logout` will destroy your auth token
`st ` will collect the devices specified in all of your installed smartapp instances
`st <device_name> on` will turn on your device. (it's easiest to down-arrow to select your device)
`st <device_name> off` will turn off your device. (it's easiest to down-arrow to select your device)
