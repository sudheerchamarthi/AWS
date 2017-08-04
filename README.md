# AWS Tutorial

### Follow these Blogs Post DAILY
Every now and then AWS adds/extends the functionality of the services. So it is good to know what has been changed and helps us to keep up to date.
```
https://aws.amazon.com/blogs/aws/
https://aws.amazon.com/about-aws/whats-new/
```
##

### ALWAYS FOLLOW AMAZON DOCUMENTATION

ALWAYS FOLLOW AMAZON DOCUMENTATION ONLY(http://docs.aws.amazon.com). Other blog posts may contain Outdated Information. So always follow official documentation only.


##


## EC2

EC2 is a service where we can create and maintain the Virtual Servers.

## Technical Terms To remember in EC2 :

 * Regions - AWS Infrastructure is hosted in multiple parts of the world. Each region is a separate geographic area and has multiple isolated locations called ava Zones. Each region is completely independent.
 * Availability Zones(AZ) - Availability Zones are isolated locations in a region.
 * **
  The following diagram illustrates the relationship between regions and Availability Zones.
 
 
![alt text](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/aws_regions.png)

  * **
* Instance -  Virtual Server or Virtual Machine.
* Tags - Metadata about the resource using which we can easily identify.
* On Demand Instance - Default Instance pricing model where we will not get any discount.
* Reserved Instance - Provides discounts 30-40% when you reserve for 1 year and up to 75% when Reserved for 3 years. Suggested for long running workloads.
* Spot Instance - Provides up to 90% discounts but Instance may terminate at any point of time without any notice when bid price is increased. Never use these in Production.
* AMI - Amazon Machine Image. It is a template that provides the information to a Launch an Instance. Used to take backups of the existing instances, using which we can restore if anything happens to the live Instance.
* EBS Volumes - Storage device that can be attached to one instance at a time. Allows you to store or install anything.
* Snapshots - Snapshot is a replica/backup of EBS volume. Snapshot will be saved to S3 thereby there is no way to loose the backups since S3 provides 99.99999999999 (11 nines) durability.
* Elastic IP - Fixed Static IP which will not change.
* Placement Groups - Logical grouping of instances with a single AZ, for tightly coupled, node-to-node communication.
* Key Pairs - SSK Key pair used to login to a Linux Machine or decrypt password for a Windows Machine.
* Security Groups - A virtual fall using which we can control the traffic into the instance.
* Elastic Load Balancers - Single point of contact for clients and distributes all the incoming application traffic across multiple EC2 instances, in multiple Availability Zones. This increases the fault tolerance of our applications.
* Auto scaling Groups - Scale up and down based on the conditions that we define in cloud watch.

  
 * Ctrl+Shift+S / Cmd+Shift+S to choose to save as Markdown or HTML
 * Drag and drop a file into here to load it
 * File contents are saved in the URL so you can share files



### Practice the following Assignment:

Follow the Below URL's and Practise.

 1 [Launch a Linux Instance](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
 
 * [Create EBS volume and attach to Instance ](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html)
 * [Make EBS Volume available for use Linux](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html)
 
 2 [Launch a Windows Instance]( http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/EC2_GetStarted.html)
 
  * [Create EBS volume and attach to Instance ](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html)
  * [Make EBS Volume available for use Windows](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-using-volumes.html)

3 Modify the EBS Volume Size and type in both Linux and Windows Machines.
  * [Linux](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-expand-volume.html)
  * [Windows](http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-expand-volume.html)
  
4 [Create an AMI of the machine](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)

5 [Create a Snapshot](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html)

6 [Create a ELB](http://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-getting-started.html)

7 [Create Auto Scaling Groups](http://docs.aws.amazon.com/autoscaling/latest/userguide/GettingStartedTutorial.html)

8 [STATUS Checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html?icmpid=docs_ec2_console)

# LABS

## Complete the below Labs one by one

* LAB 1 - [Installing a LAMP Web Server on Amazon Linux](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html) 
* LAB 2 - [Hosting a WordPress Blog with Amazon Linux](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hosting-wordpress.html) 
* LAB 3 - [Apply a SSL Certificate to Webserver](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SSL-on-an-instance.html) 
* LAB 4 - [Use ELB and route Traffic to the Instances] (http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-increase-availability.html) 
* LAB 5: [Install and Configure AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
* LAB 6: [Use AWS CLI and create an EC2 Instance](http://docs.aws.amazon.com/cli/latest/reference/ec2/)
##

### DO The Below Assignment
##

* Use auto scaling groups and deploy a highly available and very secured WordPress site behind ELB.
* Create a Architecture diagram for this entire setup. 
* Additional credits if you can make a step by step document for this without copying from anywhere which will increase your documentation skills.

##


### EC2 FAQ:

I copied this FAQ from - https://aws.amazon.com/ec2/faqs/. I feel below are few important. Read if you have time.

##
  Q: What is Amazon Elastic Compute Cloud (Amazon EC2)?

  Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable compute capacity in the cloud. It is designed to make web-scale computing easier for developers.

##



  Q: What can I do with Amazon EC2?

  Just as Amazon Simple Storage Service (Amazon S3) enables storage in the cloud, Amazon EC2 enables “compute” in the cloud. Amazon EC2’s simple web service interface allows you to obtain and configure capacity with minimal friction. It provides you with complete control of your computing resources and lets you run on Amazon’s proven computing environment. Amazon EC2 reduces the time required to obtain and boot new server instances to minutes, allowing you to quickly scale capacity, both up and down, as your computing requirements change. Amazon EC2 changes the economics of computing by allowing you to pay only for capacity that you actually use.
  
##
  Q: How quickly can I scale my capacity both up and down?

Amazon EC2 provides a truly elastic computing environment. Amazon EC2 enables you to increase or decrease capacity within minutes, not hours or days. You can commission one, hundreds or even thousands of server instances simultaneously. When you need more instances, you simply call RunInstances, and Amazon EC2 will typically set up your new instances in a matter of minutes. Of course, because this is all controlled with web service APIs, your application can automatically scale itself up and down depending on its needs.

##
Q: What operating system environments are supported?

Amazon EC2 currently supports a variety of operating systems including: Amazon Linux, Ubuntu, Windows Server, Red Hat Enterprise Linux, SUSE Linux Enterprise Server, Fedora, Debian, CentOS, Gentoo Linux, Oracle Linux, and FreeBSD. We are looking for ways to expand it to other platforms.
##
Q: How will I be charged and billed for my use of Amazon EC2?

You pay only for what you use and there is no minimum fee. Pricing is per instance-hour consumed for each instance type. Partial instance-hours consumed are billed as full hours. Data transferred between AWS services in different regions will be charged as Internet Data Transfer on both sides of the transfer. Usage for other Amazon Web Services is billed separately from Amazon EC2.
##
Q: If I have two instances in different availability zones, how will I be charged for regional data transfer?

Each instance is charged for its data in and data out at corresponding Data Transfer rates. Therefore, if data is transferred between these two instances, it is charged at "Data Transfer Out from EC2 to Another AWS Region" for the first instance and at "Data Transfer In from Another AWS Region" for the second instance.
##
Q. If I have two instances in different regions, how will I be charged for data transfer?

Each instance is charged for its data in and data out at Internet Data Transfer rates. Therefore, if data is transferred between these two instances, it is charged at Internet Data Transfer Out for the first instance and at Internet Data Transfer In for the second instance.
##
Q: How do I select the right instance type?

Amazon EC2 instances are grouped into 5 families: General Purpose, Compute Optimized, Memory Optimized, GPU, and Storage Optimized instances. General Purpose Instances have memory to CPU ratios suitable for most general purpose applications and come with fixed performance (M4 and M3 instances) or burstable performance (T2); Compute Optimized instances (C4 and C3 instances) have proportionally more CPU resources than memory (RAM) and are well suited for scale out compute-intensive applications and High Performance Computing (HPC) workloads; Memory Optimized Instances (R3 and R4 instances) offer larger memory sizes for memory-intensive applications, including database and memory caching applications; GPU Compute instances (P2) take advantage of the parallel processing capabilities of NVIDIA Tesla GPUs for high performance parallel computing; GPU Graphics instances (G3) offer high-performance 3D graphics capabilities for applications using OpenGL and DirectX; Storage Optimized Instances include I3 and I2 instances that provide very high, low latency, I/O capacity using SSD-based local instance storage for I/O-intensive applications and D2, Dense-storage instances, that provide high storage density and sequential I/O performance for data warehousing, Hadoop and other data-intensive applications. When choosing instance types, you should consider the characteristics of your application with regards to resource utilization (i.e. CPU, Memory, Storage) and select the optimal instance family and instance size.
##
Q: Why am I charged when my Elastic IP address is not associated with a running instance?

In order to help ensure our customers are efficiently using the Elastic IP addresses, we impose a small hourly charge for each address when it is not associated to a running instance.
##
Q: How isolated are Availability Zones from one another?

Each Availability Zone runs on its own physically distinct, independent infrastructure, and is engineered to be highly reliable. Common points of failures like generators and cooling equipment are not shared across Availability Zones. Additionally, they are physically separate, such that even extremely uncommon disasters such as fires, tornados or flooding would only affect a single Availability Zone.
##
Q: What is a Reserved Instance?

A Reserved Instance (RI) is an EC2 offering that provides you with a significant discount on EC2 usage when you commit to a one-year or three-year term.
##
Q: What are the differences between Standard RIs and Convertible RIs?

Standard RIs offer a significant discount on EC2 instance usage when you commit to a particular instance family. Convertible RIs offer you the option to change your instance configuration during the term, and still receive a discount on your EC2 usage. For more information on Convertible RIs.
##
Q: Can I purchase an RI for a running instance?

Yes, AWS will automatically apply an RI’s discounted rate to any applicable instance usage from the time of purchase.
##
Q: Can I control which instances are billed at the discounted rate?

No. AWS automatically optimizes which instances are charged at the discounted rate to ensure you always pay the lowest amount. For information about hourly billing, and how it applies to RIs,
##
Q: How does instance size flexibility work?

EC2 uses the scale shown below, to compare different sizes within an instance family. In the case of instance size flexibility on RIs, this scale is used to apply the discounted rate of RIs to the normalized usage of the instance family. For example, if you have an m4.2xlarge RI that is scoped to a region, then your discounted rate could apply towards the usage of 1 m4.2xlarge or 2 m4.xlarge instances.

| Instance Size 	       | Normalization Factor           
| ------------- |:-------------:
| nano     | 0.25
|micro 	   |    0.5
| small 	|        1
| medium 	|        2
| large 	|        4
| xlarge 	|        8
| 2xlarge 	|      16
| 4xlarge 	|      32
| 8xlarge 	|      64
| 10xlarge 	 |     80
| 16xlarge 	 |     128
| 32xlarge 	 |    256




##
Q: Can I change my RI during its term?

Yes, you can modify the Availability Zone of the RI, change the scope of the RI from Availability Zone to region (and vice-versa), change the network platform from EC2-VPC to EC2-Classic (and vice versa) or modify instance sizes within the same instance family (on the Linux/Unix platform).
##
Q: Can I change the instance type of my RI during its term?

Yes, Convertible RIs offer you the option to change the instance type, operating system, tenancy or payment option of your RI during its term. Please refer to the Convertible RI section of the FAQ for additional information.
##
Q: What are the different payment options for RIs?

You can choose from three payment options when you purchase an RI. With the All Upfront option, you pay for the entire RI term with one upfront payment. With the Partial Upfront option, you make a low upfront payment and are then charged a discounted hourly rate for the instance for the duration of the RI term. The No Upfront option does not require any upfront payment and provides a discounted hourly rate for the duration of the term.
##
Q: When are RIs activated?

The billing discount and capacity reservation (if applicable) is activated once your payment has successfully been authorized. You can view the status (pending | active | retired) of your RIs on the "Reserved Instances" page of the Amazon EC2 Console.
##
Q: Do RIs apply to Spot instances or instances running on a Dedicated Host?

No, RIs do not apply to Spot instances or instances running on Dedicated Hosts. To lower the cost of using Dedicated Hosts, purchase Dedicated Host Reservations.
##
Q: How do RIs work with Consolidated Billing?

Our system automatically optimizes which instances are charged at the discounted rate to ensure that the consolidated accounts always pay the lowest amount. If you own RIs that apply to an Availability Zone, then only the account which owns the RI will receive the capacity reservation. However, the discount will automatically apply to usage in any account across your consolidated billing family.
##
Q. What is a Spot Instance?

Spot instances are a new way to purchase and consume Amazon EC2 Instances. They allow customers to bid on unused EC2 capacity and run those instances for as long as their bid exceeds the current Spot Price. The Spot Price changes periodically based on supply and demand, and customers whose bids meet or exceed it gain access to the available Spot instances. Spot instances are complementary to On-Demand instances and Reserved Instances, providing another option for obtaining compute capacity.
##
Q. How is a Spot instance different than an On-Demand instance or Reserved Instance?

Spot instances provide the ability for customers to purchase compute capacity with no upfront commitment, at hourly rates usually lower than the On-Demand rate. Spot instances allow you to specify the maximum hourly price that you are willing to pay to run a particular instance type. Amazon EC2 sets a Spot Price for each instance type in each availability zone, which is the hourly price all customers will pay to run a Spot instance for that given period. The Spot Price fluctuates based on supply and demand for instances, but customers will never pay more than the maximum price they have specified. If the Spot Price moves higher than a customer’s maximum price, the customer’s instance will be shut down by Amazon EC2. Other than those differences, Spot instances perform exactly the same as On-Demand or Reserved Instances.
##
Q. How often should I expect the Spot price to change?

Amazon EC2 will change the Spot price periodically as new requests are received and as available Spot capacity changes (e.g., due to instance terminations). While the Spot price may change anytime, in general it will change once per hour and in many cases less frequently. We publish the current Spot price and historical prices for Spot instances through the API, and they can also be viewed using the AWS Management Console. This can help you assess the levels and timing of fluctuations in the Spot price over time.
##
Q. Will the price I’m charged for a running Spot instance change during its instance-hour as the Spot price changes?

No. The price per instance-hour for a Spot instance is set at the beginning of each instance-hour for the entire hour. Any changes to the Spot price will not be reflected until the next instance-hour begins.


##
Q. Where can I see my usage history for Spot instances and see how much I was billed?

The AWS Management Console makes a detailed billing report available which shows Spot instance start and termination times for all instances. Customers can check the billing report against historical Spot prices via the API to verify that the Spot price they were billed is correct.
##
Q. Why do Spot prices differ across accounts for the same instance type, operating system, and Availability Zone?

To ensure that resources are distributed across Availability Zones for a region, Availability Zones are independently mapped to identifiers for each account. For example, your Availability Zone us-east-1a might not be the same location as us-east-1a for another account. So, Spot prices for the same Availability Zone identifier may be different in different accounts. Note that there's no way for you to coordinate Availability Zones between accounts.
##
Q: How are Burstable Performance Instances different?

Amazon EC2 allows you to choose between Fixed Performance Instances (e.g. M3, C3, and R3) and Burstable Performance Instances (e.g. T2). Burstable Performance Instances provide a baseline level of CPU performance with the ability to burst above the baseline. T2 instances are for workloads that don’t use the full CPU often or consistently, but occasionally need to burst.

T2 instances’ baseline performance and ability to burst are governed by CPU Credits. Each T2 instance receives CPU Credits continuously, the rate of which depends on the instance size. T2 instances accrue CPU Credits when they are idle, and use CPU credits when they are active. A CPU Credit provides the performance of a full CPU core for one minute. The following table shows the maximum credit balance and baseline performance for each T2 instance size. Each vCPU of a T2 instance can consume CPU Credits at a maximum rate of 60 per hour when bursting to full core performance.
##
Q. When should I use Memory-optimized instances?
Memory-optimized instances offer large memory size for memory intensive applications including in-memory applications, in-memory databases, in-memory analytics solutions, High Performance Computing (HPC), scientific computing, and other memory-intensive applications.
