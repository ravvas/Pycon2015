# Explore Big Data using Simple Python Code and Cloud Environment
Presentation deck and other supporting material for Pycon 2015 talk on "Explore Big Data using Simple Python Code and Cloud Environment". 
You can learn Hadoop Map reduce using real Big data with less effort and cost. 

Below is the step by step procedure to setup the environment for Running Hadoop cluster in amazon aws and also supporting scripts used for both extracting the data from wikipedia and other automation of activities.

Note : Currently this is in Draft mode. 


1) Launch an Amazon EC2 instance ( Linux instance)  
2) Configure AWS S3 in amazon ec2 instance  ..This will let you copy files between s3 and amazon ec2.
3) Download Compressed logs from wikipedia to amazon ec2
4) unzip the log files in amazon ec2 machine and transfer them  to s3 ( Amazon storage)
5) Create mapper and reducer for the problem statement 
6) Upload the mapper and reducer to s3
7) Setup buckets in s3 for input,scripts,output
6) launch EMR ( Hadoop cluster) and Run Map reducer using Hadoop streaming. 
7) Process the output files using a shell script in ec2. 
8) Push the results to s3

Tools we use for the case study : 
1) AWS CLI  - Command level interface to launch the amazon aws 
2) Putty 
3) Python 
4) IPython 
5) 


