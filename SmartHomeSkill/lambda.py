import time
import json
import uuid

from jsonschema import validate

SAMPLE_DEVICES = [
    {
        "endpointId": "001",
        "manufacturerName": "SmartStuff, Inc.",
        "modelName": "SmartSwitch",
        "friendlyName": "Floor Lamp",
        "description": "Supports setting on/off only",
		"displayCategories": ["SWITCH"],
        "isReachable": True,
        "actions": ["turnOn", "turnOff"],
        "cookie": {},
		"capabilities": [
		     {
                "type": "AlexaInterface",
                "interface": "Alexa.PowerController",
                "version": "3",
                "properties": {
                    "supported": [
                        { "name": "powerState" }
                    ],
                    "proactivelyReported": True,
                    "retrievable": True
                }
            },
			{
				"type": "AlexaInterface",
				"interface": "Alexa.EndpointHealth",
				"version": "3",
				"properties": {
					"supported":[
						{ "name":"connectivity" }
					],
					"proactivelyReported": True,
					"retrievable": True
				}
			},
			{
				"type": "AlexaInterface",
				"interface": "Alexa",
				"version": "3"
			}
		]
    },
    {
        "endpointId": "002",
        "manufacturerName": "SmartStuff, Inc.",
        "modelName": "SmartWhite",
        "friendlyName": "Office Light",
        "description": "White bulb that supports dimming and color temperature changes only",
        "displayCategories": ["LIGHT"],
		"isReachable": True,
        "actions": ["turnOn", "turnOff",
					"setPercentage", "incrementPercentage", "decrementPercentage",
					"setColorTemperature", "incrementColorTemperature", "decrementColorTemperature"],
        "cookie": {},
		"capabilities": [
            {
                "type": "AlexaInterface",
                "interface": "Alexa.PowerController",
                "version": "3",
                "properties": {
                    "supported": [
                        { "name": "powerState" }
                    ],
                    "proactivelyReported": True,
                    "retrievable": True
                }
            },
            {
                "type": "AlexaInterface",
                "interface": "Alexa.ColorTemperatureController",
                "version": "3",
                "properties": {
                    "supported": [
                        { "name": "colorTemperatureInKelvin" }
                    ],
                    "proactivelyReported": True,
                    "retrievable": True
                }
            },
            {
                "type": "AlexaInterface",
                "interface": "Alexa.BrightnessController",
                "version": "3",
                "properties": {
                    "supported": [
                        { "name": "brightness" }
                    ],
                    "proactivelyReported": True,
                    "retrievable": True
                }
            },
            {
                "type": "AlexaInterface",
                "interface": "Alexa.PowerLevelController",
                "version": "3",
                "properties": {
                    "supported": [
                        { "name": "powerLevel" }
                    ],
                    "proactivelyReported": True,
                    "retrievable": True
                }
            },
            {
                "type": "AlexaInterface",
                "interface": "Alexa.PercentageController",
                "version": "3",
                "properties": {
                    "supported": [
                        { "name": "percentage" }
                    ],
                    "proactivelyReported": True,
                    "retrievable": True
                }
            },
			{
				"type": "AlexaInterface",
				"interface": "Alexa.EndpointHealth",
				"version": "3",
				"properties": {
					"supported":[
						{ "name":"connectivity" }
					],
					"proactivelyReported": True,
					"retrievable": True
				}
			},
			{
				"type": "AlexaInterface",
				"interface": "Alexa",
				"version": "3"
			}
		]
    },
    {
        "endpointId": "003",
        "manufacturerName": "SmartStuff, Inc.",
        "modelName": "SmartStat",
        "friendlyName": "Downstairs Thermostat",
        "description": "Can change and query temperatures",
		"displayCategories": ["THERMOSTAT"],
        "isReachable": True,
        "actions": ["setTargetTemperature", "incrementTargetTemperature", "decrementTargetTemperature",
					"getTargetTemperature", "getTemperatureReading"],
        "cookie": {},
		"capabilities": [
            {
                "type": "AlexaInterface",
                "interface": "Alexa.ThermostatController",
                "version": "3",
                "properties": {
                    "supported": [
                        { "name": "targetSetpoint" },
                        { "name": "thermostatMode" }
                    ],
                    "proactivelyReported": True,
                    "retrievable": True
                }
            },
            {
                "type": "AlexaInterface",
                "interface": "Alexa.TemperatureSensor",
                "version": "3",
                "properties": {
                    "supported": [
                        { "name": "temperature" }
                    ],
                    "proactivelyReported": True,
                    "retrievable": True
                }
            },
			{
				"type": "AlexaInterface",
				"interface": "Alexa.EndpointHealth",
				"version": "3",
				"properties": {
					"supported":[
						{ "name":"connectivity" }
					],
					"proactivelyReported": True,
					"retrievable": True
				}
			},
			{
				"type": "AlexaInterface",
				"interface": "Alexa",
				"version": "3"
			}		
		]
    },
    {
        "endpointId": "004",
        "manufacturerName": "SmartStuff, Inc.",
        "modelName": "SmartLock",
        "friendlyName": "Back Door Lock",
        "description": "Can lock and query locked/unlocked status. Does not unlock door",
		"displayCategories": ["SMARTLOCK"],
        "isReachable": True,
        "actions": ["setLockState", "getLockState"],
        "cookie": {},
		"capabilities": [
            {
                "type": "AlexaInterface",
                "interface": "Alexa.LockController",
                "version": "3",
                "properties": {
                    "supported": [
                        { "name": "lockState" }
                    ],
                    "proactivelyReported": True,
                    "retrievable": True
                }
            },
			{
				"type": "AlexaInterface",
				"interface": "Alexa.EndpointHealth",
				"version": "3",
				"properties": {
					"supported":[
						{ "name":"connectivity" }
					],
					"proactivelyReported": True,
					"retrievable": True
				}
			},
			{
				"type": "AlexaInterface",
				"interface": "Alexa",
				"version": "3"
			}
		]
    },
    {
        "endpointId": "005",
        "manufacturerName": "SmartStuff, Inc.",
        "modelName": "SmartCam",
        "friendlyName": "Front Door Camera",
        "description": "Streaming camera",
		"displayCategories": ["CAMERA"],
        "isReachable": True,
        "actions": ["retrieveCameraStreamUri"],
        "cookie": {},
		"capabilities": [
            {
                "type": "AlexaInterface",
                "interface": "Alexa.CameraStreamController",
                "version": "3",
                "cameraStreamConfigurations" : [ {
                    "protocols": ["RTSP"],
                    "resolutions": [{"width":1280, "height":720}],
                    "authorizationTypes": ["NONE"],
                    "videoCodecs": ["H264"],
                    "audioCodecs": ["AAC"]
                } ]
            },
			{
				"type": "AlexaInterface",
				"interface": "Alexa.EndpointHealth",
				"version": "3",
				"properties": {
					"supported":[
						{ "name":"connectivity" }
					],
					"proactivelyReported": True,
					"retrievable": True
				}
			},
			{
				"type": "AlexaInterface",
				"interface": "Alexa",
				"version": "3"
			}
		]
    }
]



def lambda_handler(request, context):

    if request["directive"]["header"]["name"] == "Discover":
        response = {
			"event": {
				"header": {
					"namespace": "Alexa.Discovery",
					"name": "Discover.Response",
					"payloadVersion": "3",
					"messageId": get_uuid()
				},
				"payload": {
					"endpoints": SAMPLE_DEVICES
				}
			}
		}
    else:
        response = handle_request(request)

    validate_message(request, response)
    return response


def handle_request(request):
    request_namespace = request["directive"]["header"]["namespace"]
    request_name = request["directive"]["header"]["name"]

    if request_namespace == "Alexa.PowerController":
        if request_name == "TurnOn":
            value = "ON"
        else:
            value = "OFF"

        response = {
            "context": {
                "properties": [
                    {
                        "namespace": "Alexa.PowerController",
                        "name": "powerState",
                        "value": value,
                        "timeOfSample": time.strftime("%Y-%m-%dT%H:%M:%S.00Z", time.gmtime(seconds)),
                        "uncertaintyInMilliseconds": 500
                    }
                ]
            },
            "event": {
                "header": {
                    "namespace": "Alexa",
                    "name": "Response",
                    "payloadVersion": "3",
                    "messageId": str(uuid.uuid4()),
                    "correlationToken": request["directive"]["header"]["correlationToken"]
                },
                "endpoint": {
                    "scope": {
                        "type": "BearerToken",
                        "token": "access-token-from-Amazon"
                    },
                    "endpointId": request["directive"]["endpoint"]["endpointId"]
                },
                "payload": {}
            }
        }
        return response

    elif request_namespace == "Alexa.Authorization":
        if request_name == "AcceptGrant":
            response = {
                "event": {
                    "header": {
                        "namespace": "Alexa.Authorization",
                        "name": "AcceptGrant.Response",
                        "payloadVersion": "3",
                        "messageId": "5f8a426e-01e4-4cc9-8b79-65f8bd0fd8a4"
                    },
                    "payload": {}
                }
            }
            return response

	
def validate_message(request, response):
    path_to_validation_schema = "alexa_smart_home_message_schema.json"

    with open(path_to_validation_schema) as json_file:
        schema = json.load(json_file)
    validate(response, schema)
