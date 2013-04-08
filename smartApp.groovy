/**
 *  Alfred Workflow
 *
 *  Author: @bearduino
 *  Date: 2013-04-04
 */

preferences {
	section("Allow Alfred to Control These Things...") {
		input "switches", "capability.switch", title: "Which Switches?", multiple: true
	}
}

mappings {
	path("/switches") {
		action: [
			GET: "listSwitches",
			PUT: "updateSwitches"
		]
	}
	path("/switches/$id") {
		action: [
			GET: "showSwitch",
			PUT: "updateSwitch"
		]
	}
	/*path("/switches/:id/subscriptions") {
		action: [
			POST: "addSwitchSubscription"
			DELETE: "removeSwitchSubscription"
		]
	}*/
}

def installed() {}

def updated() {}

def listSwitches() { 
	switches
}

void updateSwitches() {
	def command = request.JSON?.command
	if (command) {
		switches."$command"()
	}
}

def showSwitch() {
	def mySwitch = switches.find { it.id == params.id }
	if (!mySwitch) {
		httpError(404, "Switch not found")
	}
	mySwitch
}

void updateSwitch() {
	def command = request.JSON?.command
	if (command) {
		def mySwitch = switches.find { it.id == params.id }
		if (!mySwitch) {
			httpError(404, "Switch not found")
		} else {
			mySwitch."$command"()
		}
	}
}

def addSwitchSubscription() {
	def switchId = request.JSON?.switchId
	def mySwitch = switches.find { it.id == switchId }
	if (mySwitch) {
		subscribe(mySwitch, "switch", switchHandler)
	}
}

def removeSwitchSubscription() {
	def switchId = request.JSON?.switchId
	def mySwitch = switches.find { it.id == switchId }
	if (mySwitch) {
		unsubscribe(mySwitch)
	}
}

def switchHandler(evt) {
	// TODO:  Pass data along to Alfred
}