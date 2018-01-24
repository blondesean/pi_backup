~/Desktop/alexa-avs-sample-app/samples
#!/bin/bash

#Start the companion service
echo "Starting the companion servies"
cd ~/Desktop/alexa-avs-sample-app/samples
cd companionService && npm start&
echo "Started the companion services"

#Run the sample app
echo "Starting the sample app"
cd ~/Desktop/alexa-avs-sample-app/samples
cd javaclient && mvn exec::exec&
echo "When finished "
read -n1 -r -p "Press space to continue..." key

#Run the wake word enginge
cd ~/Desktop/alexa-avs-sample-app/samples
cd wakeWordAgent/src && ./wakeWordAgent -e kitt_ai&
