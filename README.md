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



















