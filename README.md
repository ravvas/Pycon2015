# Explore Big Data using Simple Python Code and Cloud Environment
Presentation deck and other supporting material for Pycon 2015 talk on "Explore Big Data using Simple Python Code and Cloud Environment". 
You can learn Hadoop Map reduce using real Big data with less effort and cost. 

Below is the step by step procedure to setup the environment for Running Hadoop cluster in amazon aws and also supporting scripts used for both extracting the data from wikipedia and other automation of activities.

Note : Currently this is in Draft mode. 


1) Pre-requisites in Amazon AWS. 
   go thru this link http://docs.aws.amazon.com/ElasticMapReduce/latest/ManagementGuide/emr-gs-prerequisites.html for 
i) Create Amazon AWS account 
ii) create Amazon S3 Bucket( Storage) for storing input,output and map reducer scripts etc. 
iii) create an Amazon EC2 Key pair to connect to the nodes in amazon ec2 and EMR thru secure Shell(SSH). 
iv) Create IAM Profile 
v) Install Putty and Puttygen
2) Launch an Amazon EC2 instance ( Linux instance) to download wikifiles , unzip and upload them to s3( Amazon storage)
i) Launching a simple micro instance loaded with python software etc. 
ii) Configure AWS S3 in amazon ec2 instance  ..This will let you copy files between s3 and amazon ec2.
iii) download index file containing links for each hour in  a month. 
iv) Run python script to extract links from the index file
v) Run shell script that downloads the files from wikipedia, unizip the file, upload it to s3 and remove local file 
TODO Ipython to test locally
3) Create mapper and reducer for the problem statement and upload them to s3
4) Setup buckets in s3 for input,scripts,output
5) launch EMR ( Hadoop cluster) and Run Map reducer using Hadoop streaming. 
6) Process the output files using a shell script in ec2. 
7) Push the results to s3

Tools we use for the case study : 
1) AWS CLI  - Command level interface to launch the amazon aws 
2) Putty 
3) Python 
4) IPython 
5) 


