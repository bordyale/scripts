#!/bin/sh
#THIS SCRIPT CONNECTS TO THE FTP SERVER


HOST='ftp.alma-ag.it'
USER='6677477@aruba.it'
PASSWD='Fiordaliso1-'
FILE='pubIpVF.status'
#FILETEST='pubIpVFtest.status'
LDIR='/home/pi'
BACKDIR='/home/pi/backupmysql/mysql'


#cp $full_file . 1> /dev/null 2> /dev/null
ftp -niv $HOST<<EOF 1> /dev/null 2> /dev/null
user $USER $PASSWD
binary
passive
cd alma-ag.it
lcd $LDIR
get $FILE
bye
EOF



input="$LDIR/$FILE"
echo >> $input
IP=''
while IFS= read -r line
do
  echo "$line" 
  IP="$line"
done < "$input"

 echo $IP


USER='ale'
PASSWD='alessio1A'
#IP='84.0.224.154'
DBS="$(ls -t $BACKDIR | head -n 3)"
#echo $DBS


for fil in $DBS
do
	full_file="$BACKDIR/$fil"
	echo $full_file
lftp<<END_SCRIPT
		set sftp:auto-confirm "yes"
		open -p 5000 sftp://$IP
		user $USER $PASSWD
		cd Dropbox/backupMySql/pi
		put $full_file
		bye
END_SCRIPT
done
