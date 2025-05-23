#!/bin/sh
#THIS SCRIPT CONNECTS TO THE FTP SERVER


HOST='ftp.alma-ag.it'
USER='6677477@aruba.it'
PASSWD='Fiordaliso1-'
FILE='pubIpVF.status'
#FILETEST='pubIpVFtest.status'
LDIR='/home/vulkan'
BACKDIR='/home/vulkan/backupmysql/vserv'
DIR_DEST='/home/ale/Dropbox/backupMySql/vserv'


#cp $full_file . 1> /dev/null 2> /dev/null
#ftp -niv $HOST<<EOF 1> /dev/null 2> /dev/null
#user $USER $PASSWD
#binary
#passive
#cd alma-ag.it
#lcd $LDIR
#get $FILE
#bye
#EOF

input="$LDIR/$FILE"
rm -rf $input
wget --user=$USER --password=$PASSWD --directory-prefix=$LDIR ftp://$HOST/alma-ag.it/$FILE

echo >> $input

IP=''
while IFS= read -r line
do
  echo "$line" 
  IP="$line"
done < "$input"

echo "read ip:"
echo $IP


USER='ale'
PASSWD='alessio1A'
#IP='84.0.224.154'
DBS="$(ls -t $BACKDIR | head -n 3)"
echo $DBS

IP='192.168.1.250'
PORT='22'
for fil in $DBS
do
	full_file="$BACKDIR/$fil"
	echo $full_file
	echo "Uploading file to remote server..."
	sshpass -p "$PASSWD" scp -P $PORT -o StrictHostKeyChecking=no -rC $full_file $USER@$IP:$DIR_DEST
	echo "File upload to remote server completed!"
done
