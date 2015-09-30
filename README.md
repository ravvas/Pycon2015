# Explore Big Data using Simple Python Code and Cloud Environment
Presentation deck and other supporting material on "Explore Big Data using Simple Python Code and Cloud Environment". 
You can learn Hadoop Map reduce using real Big data with less effort and cost. 

Below is the step by step procedure to setup the environment for Running Hadoop cluster in amazon aws and also supporting scripts used for both extracting the data from wikipedia and other automation of activities.

#Note : Currently this is in Draft mode. 

1) Installation of Python and Ipython in local windows computer. Follow the steps in the document named "Python and IPython Installation"  

1) Pre-requisites in Amazon AWS.
   go thru this link http://docs.aws.amazon.com/ElasticMapReduce/latest/ManagementGuide/emr-gs-prerequisites.html for  
i) Create Amazon AWS account  
ii) create Amazon S3 Bucket( Storage) for storing input,output and map reducer scripts etc.    
iii) create an Amazon EC2 Key pair to connect to the nodes in amazon ec2 and EMR thru secure Shell(SSH).  
iv) Create IAM Profile : This is required for accessing S3 storage from Ec2. Follow the steps at http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html#cli-signup. 
v) Provide AmazonS3FullAccess previlages to the above created IAM Provide by going to IAM -> Users, click on the user and attach policy called AmazonS3FullAccess. Now using the IAM provide we can access S3 from Ec2.
v) To Install Putty and Puttygen  and for converting the private key pair to putty format follow steps at http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html

With the above steps we are ready to start actual process :) 

2) Launch an Amazon EC2 instance ( Linux instance) to download wikifiles , unzip and upload them to s3( Amazon Storage)  
i) Launching a simple micro instance loaded with python software etc : login to aws.amazon.com, in services select EC2. Click on Launch Instance , select Amazon Linux AMI from "Chose an Amazon Machine Image" step. select t2.micro in step 2 of " Choose an Instance Type". Click on "Review and Launch". Then in step 7, click on Launch. Before clicking on Launch, ensure that in step 7, under security groups port 22 is enabled which is required to connect to this instance from putty ssh. 
After clicking on launch, select the keypair you created in the above steps and click on Launch instances. 
Now click on View Instances. Once the instance status changes to "Running" , select the instance at bottom under description copy the public IP address. 
Now launch putty session with hostname as ec2-user@IP-Adrress. Now you will be able to login to ec2 instance you created. 
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


