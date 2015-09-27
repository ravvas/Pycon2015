#!/bin/bash
filename=$1
aws s3 cp s3://perftestmap/output/ imroutput --recursive
cat /home/ec2-user/scripts/imroutput/* > emrout1
sort -k2nr emrout1 > emrout2
head -25 emrout2 > emrout3
awk '{$1=$1}1' OFS="," emrout3 > emrout4.csv
aws s3 cp emrout2 s3://hariemrresults/final$filename
aws s3 cp emrout4.csv s3://hariemrresults/top25$filename.csv
rm emrout*
rm -r imroutput
