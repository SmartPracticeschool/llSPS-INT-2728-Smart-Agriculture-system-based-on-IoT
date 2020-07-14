import time
import sys
import ibmiotf.application # to install pip install ibmiotf
import ibmiotf.device

#Provide your IBM Watson Device Credentials
organization = "1x1z9i" #replace the ORG ID
deviceType = "AgriDevice"#replace the Device type wi
deviceId = "agri2"#replace Device ID
authMethod = "token"
authToken = "!Z@58mjh1FKt1O1wIH" #Replace the authtoken

def myCommandCallback(cmd): # function for Callback
        print("Command received: %s" % cmd.data)
        if cmd.data['command']=='ON':
                print("MOTOR ON IS RECEIVED")
                          
        elif cmd.data['command']=='OFF':
                print("MOTOR OFF IS RECEIVED")
                

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
              
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
