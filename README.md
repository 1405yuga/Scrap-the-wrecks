# Scrap-the-wrecks
Scrap the wrecks is the python system which detects the vehicle's number plate and notify the owner if vehicle's age is more than 15 years. Vehicle's number plate is extracted using opencv of python. Owner is notified with sms on registered phone number. Project is coded in python where twilio library is used for sending sms.

## Guide
### Database:
Since there is no direct access to all the information of database of vehicle a sample database is created. In cloud firestore a sample database is created where vehicle’s number and corresponding owner’s name, mobile number and vehicle’s registration date is stored.

<img src="https://github.com/1405yuga/Scrap-the-wrecks/assets/82303711/b885550f-8ba9-4ced-b39b-9017cb52aa03"  width="800" height="460">

### Camera:
Mobile camera of IP Webcam application is connected to python project which captures video and each frame is analysed. Here vehicle's number plate is detected. Later, it dectects the alpha-numeric characters associated with it.

<img src="https://github.com/1405yuga/Scrap-the-wrecks/assets/82303711/d7af616d-fcf8-4103-8bae-042b324ff716"  width="500" height="260">

### Console output:
If vehicle's age is more tha 15 years this project prints the vehicle number, owner’s name ,mobile number, vehicle’s registration date ,vehicle’s age and sms code in the console.

<img src="https://github.com/1405yuga/Scrap-the-wrecks/assets/82303711/7297ccf8-eeb5-41d4-8890-b9c56b568a9e"  width="800" height="460">

### Sms:
If the vehicle's age is more than 15 years than sms is received on vehicle's registered mobile number.

<img src="https://github.com/1405yuga/Scrap-the-wrecks/assets/82303711/4d36397e-1fa6-4470-a282-fcf7df033622"  width="250" height="500">
