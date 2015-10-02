# Explore Big Data using Simple Python Code and Cloud Environment
Presentation deck and other supporting material on "Explore Big Data using Simple Python Code and Cloud Environment". 
You can learn Hadoop Map reduce using real Big data with less effort and cost. 

Below is the step by step procedure to setup the environment for Running Hadoop cluster in amazon aws and also supporting scripts used for both extracting the data from wikipedia and other automation of activities.

#Note : Formatting remaining. 

1.  Installation of Python and Ipython in local windows computer. Follow the steps in the document named "Python and IPython Installation"  
2.  Pre-requisites in Amazon AWS.
   go thru this link http://docs.aws.amazon.com/ElasticMapReduce/latest/ManagementGuide/emr-gs-prerequisites.html for  
   i.  Create Amazon AWS account  
   ii. create Amazon S3 Bucket( Storage) for storing input,output and map reducer scripts etc.    
   iii.  create an Amazon EC2 Key pair to connect to the nodes(Virtual servers)  in amazon ec2 and EMR thru secure Shell(SSH).  
   iv. Create IAM Profile : This is required for accessing S3 storage from Ec2. Follow the steps at  http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html#cli-signup.  
   v.  Provide AmazonS3FullAccess previlages to the above created IAM Provide by going to IAM -> Users, click on the user and   attach policy called AmazonS3FullAccess. Now using the IAM credentials we can access S3 from Ec2. Only step remaining is once  you loginto the virtual server(ec2) , you need to do "aws configure"  
   vi. To Install Putty and Puttygen  and for converting the private key pair to putty format follow steps at  http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html  

3.  Launch an Amazon EC2 instance ( Linux instance) to download wikifiles , unzip and upload them to s3( Amazon Storage)  
  i.  Launching a simple micro instance loaded with python software etc : login to aws.amazon.com, in services select EC2. Click on Launch Instance , select Amazon Linux AMI from "Chose an Amazon Machine Image" step.   
  select t2.micro in step 2 of " Choose an Instance Type". Click on "Review and Launch".   
  Then in step 7, click on Launch. Before clicking on Launch, ensure that in step 7, under security groups port 22 is enabled   which is required to connect to this instance from putty ssh.  
  After clicking on launch, select the keypair you created in the above steps and click on Launch instances.   
  Now click on View Instances. Once the instance status changes to "Running" , select the instance , at bottom under       description copy the public IP address. 
Now launch putty session with hostname as ec2-user@IP-Adrress. Now you will be able to login to ec2 instance you created.   
  ii.  Configure AWS S3 in amazon ec2 instance  ..This will let you copy files between s3 and amazon ec2. 
    For this type "aws configure" , in the prompt enter credentials you copied when create IAM profile. for region and output format, leave blank.  
  iii.   download index file containing links for each hour in  a month.  say you want to extract september month log files. Type in shell prompt : wget https://dumps.wikimedia.org/other/pagecounts-raw/2015/2015-09/   
    Now you have index.html file copied to the directory. 
   iv.  This index file have all the links for the September month log files. So to extract the log file names from the index.html, execute the python program extractgz.py from "Extract data" folder by copying that to ec2 and typing "python extractgz.py > allfilenames" . Now a file called "allfilenames" created in the same directory with all the file names.  
   v.   update the bucket name you create with <your buckethere> " in the sh file. Execute the shell script by typing "bash downloadwikifiles.sh allfilenames". This will download each of the file ( sequentially) unizip the file, upload it to s3 and remove local file.  Normally Amazon downloads these files at the rate of 2MB by sec and each file download time is approximately 50 to 60 sec. So approximately it will take 12 hours to download the files. So run the shell script in background so that even after disconnecting the putty session, the script execution will continue. To check whether all the files are downloaded , check the S3 bucket periodically and once all the files are downloaded , you can terminate the ec2 session by going to ec2 services and terminate the instance.  

4. In the s3 bucket you created, create folders called input, logfiles, output, scripts and output. 
5. Upload the mapper and reducer scripts from "mapreduce scripts" folder in github to scripts folder in your s3 bucket.
6. Launch EMR ( Hadoop cluster) and Run Map reducer using Hadoop streaming. 
 Before Launching EMR cluster, please check how much it will cost per hour in the page  https://aws.amazon.com/elasticmapreduce/pricing/ . 
  i.  After loginto your aws account , select EMR under Service -> Analytics.   
  ii. Click on Create Cluster, select 'Go to Advanced Options"  
  iii.  Give any thing for cluster name  
  iv.  For log folder s3 location , select logfiles from the s3 bucket you created and append some unique logfile folder which will be created by EMR. So your log file location should belike this "s3://<yourbucket>/logfiles/<unique folder>  
  vi. In Hardware configuration section , for master go with m3.medium, for core select a Instance type. If you want to experiemnt to process 2-3 days files instead of one month, start with m3.xlarge with 2 or 3 count.   
  vi.  Under security and access section, select the keypair you created initially. So that you will be able to login to Master node after cluster created.   
  vii. Under steps, select step, "streaming Program" and click on configure and add.   
  viii. Give any name for Name of the step, provider mapper, reducer scripts to mapper and reducer.   
   ix.  For Input s3 location, provide the folder of input files. If you want to start with 2-3 days files, create another folder in your bucket and copy those files to that folder and assign that folder in this field.   
   x.  output s3 location will be your ouput folder and add an unique name after that. If you provide existing folder , the step will fail. So location should be like s3://<your bucket>/output/<New folder name>   
   xi.   Now click "add" . This step/job will be executed after the cluster is created.   
   xii.  You are ready to create cluster by clicking on "create cluster". Wait ..there is one more step remaining.   
   xiii.  For monitoring the status of the jobs and counters/configuration etc , hadoop will be pushing data to a web server in Master Node. To access the same from your local computer , you need to create a proxy tunnel. Steps for the same :   
   xiv.  Then proceed by clicking on "create cluster".   
7.   There are many things you can check while job is running     
   i.  Cluster will not create immediately after you click on create cluster. Amazon will take approximately 5-8 minutes to provision virtual servers, install required software, configure master and core/slave nodes.   
   ii.  As soon as the status of master in summary changes from provisioning to bootstrapping, master public DNS Ip address will be appeared. You can proxy throttle to that using putty as mentioned in above steps. Then in your firefox/chrome, you can type "http://<Master Ip Address>:8088" . And you are ready to monitor and review Cluster configuration, counters, jobs etc. Some time when you click on some links you may get can not access message, then in the URL bar replace the Internal Ip adress with Master Public IP address.   
   iii.   Once the status of both Master and Core changes to "running" , under the steps first hadoop debugging step will complete. Then the job/step you created will execute.   
   iv.  You can monitor the step status by clickon on view jobs against the step, and click on view tasks. You can see how many total tasks, pending tasks, completed tasks and running tasks.   
   v.   Once the job completed, the out put will be stored in output folder you assigned while creating the task   

8.  Each reducer will create one out put file. Hence your results are not stored in one file. To merge all the output files and sort by number of requests  
   i. login to EC2 micro instance ( same procedure when did for extracting data from wiki) , do aws configure. 
   ii. Copy the shell script "processout.sh" from github folder "process output" to ec2. 
   iii.  Execute the shell script by editing the fields with actual values. 
   iv.  Execute the script by typing "bash processout.sh <filename>" . Filename will be the file name you want to name for the results. 
   v.  Now in results folder there are two files created :  top25<filename>.csv and  one with top 25 pages and another final<filename> all pages sort by number of requests in descending order. These files will be created in results folder in your bucket in s3.

Tools we use for the case study : 
1) AWS CLI  - Command level interface to launch the amazon aws  
2) Putty   
3) Python   
4) IPython   



