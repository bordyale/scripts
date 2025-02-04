#!/bin/bash

WPATH="/home/ale/scripts/statusIpPub/"
IPFILE="pubIpMail.status"
MSGTEMP="msg.txt"
MSGTOSEND="msg-to-send.txt"
EMAIL="alessio.bordignon@gmail.com"
/usr/bin/curl ipinfo.io/ip 1> $WPATH$IPFILE 2> /dev/null
cp $WPATH$MSGTEMP $WPATH$MSGTOSEND
cat $WPATH$IPFILE >> $WPATH$MSGTOSEND
/usr/sbin/ssmtp $EMAIL < $WPATH$MSGTOSEND
