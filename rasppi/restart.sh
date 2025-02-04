#!/bin/bash

logbasedir=/home/pi/scripts/
email="alessio.bordignon@gmail.com"
/usr/sbin/ssmtp $email < "$logbasedir"restart-log.txt
