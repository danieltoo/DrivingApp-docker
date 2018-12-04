echo "Checking the Orion"
curl -X GET http://0.0.0.0:1026/version -H 'Accept: application/json'
echo "Checking the QL"
curl -X GET http://0.0.0.0:8668/v2/version -H 'Accept: application/json'
echo "Checking the DrivingApp Service /api"
curl -X GET http://0.0.0.0:4005/api -H 'Accept: application/json'
echo "Checking the DrivingApp Service /service"
curl -X GET http://0.0.0.0:4005/service -H 'Accept: application/json'
echo "Checking the DrivingApp Service /crate"
curl -X GET http://0.0.0.0:4005/crate -H 'Accept: application/json'
echo "Checking the Notifications Service"
curl -X GET http://0.0.0.0:3001/
echo "Checking the KeyStone"
curl -X GET http://0.0.0.0:5000/ -H 'Accept: application/json' -H 'X-Auth-token: ADMIN'
echo "Creating Device Subscriptions to QL"
curl -iX POST http://0.0.0.0:1026/v2/subscriptions -d @Subscriptions/DeviceToQL.json --header "Content-Type: application/json"
echo "Creating Alert Subscriptions to QL"
curl -iX POST http://0.0.0.0:1026/v2/subscriptions -d @Subscriptions/AlertToQL.json --header "Content-Type: application/json"
echo "Creating Alert Subscriptions to Notifications"
curl -iX POST http://0.0.0.0:1026/v2/subscriptions -d @Subscriptions/AlertToNotifications.json --header "Content-Type: application/json"
echo "Creating Device Entity in Orion"
curl -iX POST http://0.0.0.0:1026/v2/entities -d @"Orion Entities/Device.json" --header "Content-Type: application/json"
echo "Creating Device Token Entity in Driving Service"
curl -iX POST http://0.0.0.0:4005/api/device/token -d @"Datamodels Entities/DeviceToken.json" --header "Content-Type: application/json"
echo "Creating Zone Entity in Driving Service"
curl -iX POST http://0.0.0.0:4005/api/zone  -d @"Datamodels Entities/Zone.json" --header "Content-Type: application/json"
echo "Creating User Entity in Driving Service"
curl -iX POST http://0.0.0.0:4005/api/user  -d @"Datamodels Entities/User.json" --header "Content-Type: application/json"
echo "Creating Alert"
curl -iX POST http://0.0.0.0:1026/v2/entities -d @"Orion Entities/Alert.json" --header "Content-Type: application/json"