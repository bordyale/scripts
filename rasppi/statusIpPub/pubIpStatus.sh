#!/bin/bash

/usr/bin/curl -4 icanhazip.com 1>> /home/pi/scripts/statusIpPub/pubIp.status 2> /dev/null
echo 1>> /home/pi/scripts/statusIpPub/pubIp.status 2> /dev/null
echo 1>> /home/pi/scripts/statusIpPub/pubIp.status 2> /dev/null
