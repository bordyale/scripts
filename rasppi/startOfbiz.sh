#!/bin/bash
#To execute in /etc/rc.local boot and reboot as well!!not working
#export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_202
logbasedir=/home/pi/scripts/
/bin/date >> "$logbasedir"restart-log.txt
cd /home/pi/ofbiz/apache-ofbiz-17.12.09
#bash gradlew ofbiz &
bash gradlew ofbiz --offline -x test
