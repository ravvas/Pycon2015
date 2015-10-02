#!/bin/bash
filename=$1
while read LINE
do
wget https://dumps.wikimedia.org/other/pagecounts-raw/2015/2015-07/$LINE
gunzip $LINE
unzipfile=`echo $LINE| rev | cut -c 4- | rev `
aws s3 cp $unzipfile s3://wikisample/$unzipfile
rm $unzipfile
echo "$unzipfile"
done < $filename
