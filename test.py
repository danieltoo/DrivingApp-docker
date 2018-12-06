import requests
import json

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def paintError(error):
    return ("%s %s %s %s %s" % (color.BOLD, color.RED, error, color.END, color.END))
def paintOK(ok):
    return ("%s %s %s %s %s" % (color.BOLD, color.GREEN, ok, color.END, color.END))


def checkServices():
    _orion = True 
    _ql = True
    _driving = True
    _notifications = True
    _key = True
    # TEST SERVICES
    #ORION TEST
    try :
        orion = requests.get('http://0.0.0.0:1026/version')
        orionMessage = "Orion "
        if orion.status_code == 200 :
            orionMessage += paintOK("OK")
        else :
            orionMessage += paintError("ERROR %i" % (orion.status_code))
        print(orionMessage)
    except:
        print(paintError("The Orion is not running"))
        _orion = False
    #QUANTUMLEAP TEST
    try:   
        ql = requests.get('http://0.0.0.0:8668/v2/version')
        qlMessage = "QuantumLeap "
        if ql.status_code == 200 :
            qlMessage += paintOK("OK")
        else :
            qlMessage += paintError("ERROR %i" % (ql.status_code))
        print(qlMessage)
    except: 
        print(paintError("The QuamtumLeap is not running"))
        _ql = False
    #DRIVINGAPP SERVICE TEST   
    try:
        api = requests.get('http://0.0.0.0:4005/api')
        apiMessage = "/api "
        if api.status_code == 200 :
            apiMessage += paintOK("OK")
        else :
            apiMessage += paintError("ERROR %i" %(api.status_code))
   
        service = requests.get('http://0.0.0.0:4005/service')
        serviceMessage = "/service "    
        if service.status_code == 200 :
            serviceMessage += paintOK("OK")
        else :
            serviceMessage += paintError("ERROR %i" %(service.status_code))
            
        crate = requests.get('http://0.0.0.0:4005/crate')
        crateMessage = "/crate "
        if crate.status_code == 200 :
            crateMessage += paintOK("OK")
        else :
            crateMessage += paintError("ERROR %i" %(crate.status_code))
        
        print ("DrivingApp Service %s %s %s" % (apiMessage, serviceMessage, crateMessage))
    except: 
        print(paintError("The DrivingApp Service is not running"))
        _driving = False

    #NOTIFICATIONS SERVICE TEST 
    try:   
        notifications = requests.get('http://0.0.0.0:3001')
        notificationsMessage = "Notifications Service "
        if notifications.status_code == 200 :
            notificationsMessage += paintOK("OK")
        else :
            notificationsMessage += paintError("ERROR %i" %(notifications.status_code))
        print(notificationsMessage)
    except:
        print(paintError("The Notifications Service is not running"))
        _notifications = False

    #KEYROCK TEST
    try:  
        key = requests.get('http://0.0.0.0:5000', headers={'X-Auth-token': 'ADMIN'})
        keyMessage = "KeyRock "
        if key.status_code == 300 :
            keyMessage += paintOK("OK")
        else :
            keyMessage += paintError("ERROR %i" %(key.status_code))
        print(keyMessage)
    except:
        print(paintError("The KeyRock Service is not running"))
        _key = False
    #SUBSCRIPTIONS 
    if _orion:
        #CREATE DEVICE SUBSCRIPTION TO QL
        with open('Subscriptions/DeviceToQL.json') as json_data:
            deviceSubMessage = "Device Subscription to QL"
            body = json.load(json_data)
            deviceSubs = requests.post("http://0.0.0.0:1026/v2/subscriptions",data=json.dumps(body), headers={"Content-Type":"application/json"})
            if (deviceSubs.status_code == 201) :
                deviceSubMessage += paintOK("CREATED")
            else :
                deviceSubMessage += paintOK("FAILED")
            print(deviceSubMessage)
        #CREATE ALERT SUBSCRIPTION TO QL
        with open('Subscriptions/AlertToQL.json') as json_data:
            alertSubMessage = "Alert Subscription to QL"
            body = json.load(json_data)
            alertSubsQL = requests.post("http://0.0.0.0:1026/v2/subscriptions",data=json.dumps(body), headers={"Content-Type":"application/json"})
            if (alertSubsQL.status_code == 201) :
                alertSubMessage += paintOK("CREATED")
            else :
                alertSubMessage += paintError("FAILED")
            print(alertSubMessage)
        #CREATE ALERT SUSCRIPTION TO NOTIFICATIONS SERVICE
        with open('Subscriptions/AlertToNotifications.json') as json_data:
            alertMessage = "Subscriptions to Notifications Service"
            body = json.load(json_data)
            alertSubsN = requests.post("http://0.0.0.0:1026/v2/subscriptions",data=json.dumps(body), headers={"Content-Type":"application/json"})
            if (alertSubsN.status_code == 201) :
                alertMessage += paintOK("CREATED")
            else :
                alertMessage += paintError("FAILED")
            print(alertMessage)
    #FUNCTIOANLITY TEST
    #CREATE DEVICE ENTITY
    if _orion:
        with open('Orion Entities/Device.json') as json_data:
            deviceMessage = "Device on the Orion"
            body = json.load(json_data)
            device = requests.post("http://0.0.0.0:1026/v2/entities",data=json.dumps(body), headers={"Content-Type":"application/json"})
            if (device.status_code == 201) :
                deviceMessage += paintOK("CREATED")
            else :
                deviceMessage += paintError("FAILED")
            print(deviceMessage)
    
    if _driving:
        #CREATE DEVICE TOKEN ENTITY
        with open('Private Entities/DeviceToken.json') as json_data:
            tokenMessage = "Device Token on the DrivingApp Service"
            body = json.load(json_data)
            deviceToken = requests.post("http://0.0.0.0:4005/api/device/token",data=json.dumps(body), headers={"Content-Type":"application/json"})
            if (deviceToken.status_code == 200) :
                tokenMessage += paintOK("CREATED")
            else :
                tokenMessage += paintError("FAILED")
            print(tokenMessage)
        #CRETA ZONE ENTITY
        with open('Private Entities/Zone.json') as json_data:
            zoneMessage = "Zone on the DrivingApp Service" 
            body = json.load(json_data)
            zone = requests.post("http://0.0.0.0:4005/api/zone",data=json.dumps(body), headers={"Content-Type":"application/json"})
            if (zone.status_code == 201) :
                zoneMessage += paintOK("CREATED")
            else :
                zoneMessage += paintError("FAILED")
            print(zoneMessage)
        if _key:
            #CREATE USER ENTITY
            with open('Private Entities/User.json') as json_data:
                userMessage = "User on the DrivingApp Service"
                body = json.load(json_data)
                user = requests.post("http://0.0.0.0:4005/api/user",data=json.dumps(body), headers={"Content-Type":"application/json"})
                if (user.status_code == 201) :
                    userMessage += paintOK("CREATED")
                else :
                    userMessage += paintError("FAILED")
                print(userMessage)
    


checkServices()
