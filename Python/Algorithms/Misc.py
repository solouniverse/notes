"""
Implement Multiply, Subtraction, Division using only '+'
* - / only '+'

1. m*n + 
-
a-b => a(some operation)b
"""
def multiply(m,n):
	Result=0
	for x in range(n):
		Result+=m
	return Result
	
"""
0101101 +ve
-ve +ve
1101101 -ve
adders 

0-1
1-0

10101
01010
------
11111
------
00001
00000
complement
a+~a+1=0 
(~a+1)=-a
2'c of a
a-b
a+(-b)
a+(2'C b)
a+(~b+1)
"""

def subtract(m,n):
#-ve number is represented as 2' complement of a number
	return (n+(~m+1))

m=10
n=210
def divide(n,m):
	x=0
	result=0
	while(n>=result):
		#print(result,x)
		result+=m 
		x=x+1
	return(x)

#
# Occuraces of word on large string
#

def stringOccurances():
	string="""
	Microsoft Azure
	From Wikipedia, the free encyclopedia
	Microsoft Azure
	Microsoft Azure Logo.svg
	Developer(s)	Microsoft
	Initial release	February 1, 2010; 7 years ago
	Operating system	Linux, Microsoft Windows
	License	Closed source for platform, Open source for client SDKs
	Website	azure.microsoft.com
	Microsoft Azure (formerly Windows Azure) /ˈæʒər/ is a cloud computing service created by Microsoft for building, testing, deploying, and managing applications and services through a global network of Microsoft-managed data centers. It provides software as a service (SaaS), platform as a service and infrastructure as a service and supports many different programming languages, tools and frameworks, including both Microsoft-specific and third-party software and systems.
	Azure was announced in October 2008 and released on February 1, 2010 as "Windows Azure" before being renamed "Microsoft Azure" on March 25, 2014.[1][2]
	Contents  [hide] 
	1	Services
	1.1	Computer
	1.2	Mobile services
	1.3	Storage services
	1.4	Data management
	1.5	Messaging
	1.6	Media services
	1.7	CDN
	1.8	Developer
	1.9	Management
	1.10	Machine Learning
	2	Regions
	3	Design
	3.1	Deployment models
	4	Timeline
	5	Privacy
	6	Significant outages
	7	Certifications
	8	See also
	9	References
	10	Further reading
	11	External links
	Services[edit]
	Microsoft lists over 600 Azure services,[3] of which some are covered below:
	Computer[edit]
	Virtual machines, infrastructure as a service (IaaS) allowing users to launch general-purpose Microsoft Windows and Linux virtual machines, as well as preconfigured machine images for popular software packages.[4]
	App services, platform as a service (PaaS) environment letting developers easily publish and manage Web sites.
	Websites, high density hosting[non sequitur] of websites allows developers to build sites using ASP.NET, PHP, Node.js, or Python and can be deployed using FTP, Git, Mercurial, Team Foundation Server or uploaded through the user portal. This feature was announced in preview form in June 2012 at the Meet Microsoft Azure event.[5] Customers can create websites in PHP, ASP.NET, Node.js, or Python, or select from several open source applications from a gallery to deploy. This comprises one aspect of the platform as a service (PaaS) offerings for the Microsoft Azure Platform. It was renamed to Web Apps in April 2015.[1][6]
	WebJobs, applications that can be deployed to a Web App to implement background processing. That can be invoked on a schedule, on demand or can run continuously. The Blob, Table and Queue services can be used to communicate between Web Apps and Web Jobs and to provide state.[citation needed]
	Mobile services[edit]
	Mobile Engagement collects real-time analytics that highlight users’ behavior. It also provides push notifications to mobile devices.[7]
	HockeyApp can be used to develop, distribute, and beta-test mobile apps[8]
	Storage services[edit]
	Storage Services provides REST and SDK APIs for storing and accessing data on the cloud.
	Table Service lets programs store structured text in partitioned collections of entities that are accessed by partition key and primary key. It's a NoSQL non-relational database.
	Blob Service allows programs to store unstructured text and binary data as blobs that can be accessed by a HTTP(S) path. Blob service also provides security mechanisms to control access to data.
	Queue Service lets programs communicate asynchronously by message using queues.
	File Service allows storing and access of data on the cloud using the REST APIs or the SMB protocol.[9]
	Data management[edit]
	Azure Search provides text search and a subset of OData's structured filters using REST or SDK APIs.
	DocumentDB is a NoSQL database service that implements a subset of the SQL SELECT statement on JSON documents.
	Redis Cache is a managed implementation of Redis.
	StorSimple manages storage tasks between on-premises devices and cloud storage.[10]
	SQL Database, formerly known as SQL Azure Database, works to create, scale and extend applications into the cloud using Microsoft SQL Server technology. It also integrates with Active Directory and Microsoft System Center and Hadoop.[11]
	SQL Data Warehouse is a data warehousing service designed to handle computational and data intensive queries on datasets exceeding 1TB.
	Azure Data Lake is a scalable data storage and analytics service for big-data analytics workloads that require developers to run massively parallel queries.
	Azure HDInsight[12] is a big data relevant service, that deploys Hortonworks Hadoop on Microsoft Azure, and supports the creation of Hadoop clusters using Linux with Ubuntu.
	Azure Stream Analytics is a serverless scalable event processing engine that enables users to develop and run real-time analytics on multiple streams of data from sources such as devices, sensors, web sites, social media, and other applications.
	Messaging[edit]
	The Microsoft Azure Service Bus allows applications running on Azure premises or off premises devices to communicate with Azure. This helps to build scalable and reliable applications in a service-oriented architecture (SOA). The Azure service bus supports four different types of communication mechanisms:[citation needed]
	Event Hubs, which provide event and telemetry ingress to the cloud at massive scale, with low latency and high reliability. For example an event hub can be used to track data from cell phones such as a GPS location coordinate in real time.[citation needed]
	Queues, which allow one-directional communication. A sender application would send the message to the service bus queue, and a receiver would read from the queue. Though there can be multiple readers for the queue only one would process a single message.
	Topics, which provide one-directional communication using a subscriber pattern. It is similar to a queue, however each subscriber will receive a copy of the message sent to a Topic. Optionally the subscriber can filter out messages based on specific criteria defined by the subscriber.
	Relays, which provide bi-directional communication. Unlike queues and topics, a relay doesn't store in-flight messages in its own memory. Instead, it just passes them on to the destination application.
	Media services[edit]
	A PaaS offering that can be used for encoding, content protection, streaming, or analytics.[citation needed]
	CDN[edit]
	A global content delivery network (CDN) for audio, video, applications, images, and other static files. It can be used to cache static assets of websites geographically closer to users to increase performance. The network can be managed by a REST based HTTP API.[citation needed]
	Azure has 30 point of presence locations worldwide (also known as Edge locations) as of December 2016.[13]
	Developer[edit]
	Application Insights[citation needed]
	Visual Studio Team Services[citation needed]
	Management[edit]
	Azure Automation, provides a way for users to automate the manual, long-running, error-prone, and frequently repeated tasks that are commonly performed in a cloud and enterprise environment. It saves time and increases the reliability of regular administrative tasks and even schedules them to be automatically performed at regular intervals. You can automate processes using runbooks or automate configuration management using Desired State Configuration.[1]
	Microsoft SMA (software)
	Machine Learning[edit]
	Microsoft Azure Machine Learning (Azure ML) service is part of Cortana Intelligence Suite that enables predictive analytics and interaction with data using natural language and speech through Cortana.[14]
	Regions[edit]
	Azure is generally available in 36 regions around the world. Microsoft has announced an additional four regions.[15] Microsoft is the first hyper-scale cloud provider that has committed to building facilities on the continent of Africa with two regions located in South Africa.[16]
	Design[edit]
	Microsoft Azure uses a specialized operating system, called Microsoft Azure, to run its "fabric layer":[citation needed] a cluster hosted at Microsoft's data centers that manages computing and storage resources of the computers and provisions the resources (or a subset of them) to applications running on top of Microsoft Azure. Microsoft Azure has been described as a "cloud layer" on top of a number of Windows Server systems, which use Windows Server 2008 and a customized version of Hyper-V, known as the Microsoft Azure Hypervisor to provide virtualization of services.[citation needed]
	Scaling and reliability are controlled by the Microsoft Azure Fabric Controller[citation needed] so the services and environment do not crash, if one of the servers crashes within the Microsoft data center and provides the management of the user's Web application like memory resources and load balancing.[citation needed]
	Azure provides an API built on REST, HTTP, and XML that allows a developer to interact with the services provided by Microsoft Azure. Microsoft also provides a client-side managed class library that encapsulates the functions of interacting with the services. It also integrates with Microsoft Visual Studio, Git, and Eclipse.[citation needed]
	In addition to interacting with services via API, users can manage Azure services using the Web-based Azure Portal, which reached General Availability in December 2015.[17] The portal allows users to browse active resources, modify settings, launch new resources, and view basic monitoring data from active virtual machines and services. More advanced Azure management services are available.[18]
	Deployment models[edit]
	Microsoft Azure offers two deployment models for cloud resources: the "classic" deployment model and the Azure Resource Manager.[19] In the classic model, each Azure resource (virtual machine, SQL database, etc.) was managed individually. The Azure Resource Manager, introduced in 2014,[19] enables users to create groups of related services so that closely coupled resources can be deployed, managed, and monitored together.[20]
	Timeline[edit]

	Ray Ozzie announcing Windows Azure at PDC 2008, October 27
	October 2008 – (PDC LA), Announced the Windows Azure Platform
	March 2009 – Announced SQL Azure Relational Database
	November 2009 – Updated Windows Azure CTP, Enabled full trust, PHP, Java, CDN CTP and more
	February 2010 – Windows Azure Platform commercially available
	June 2010 – Windows Azure Update, .NET Framework 4, OS Versioning, CDN, SQL Azure Update[21]
	October 2010 (PDC) – Platform enhancements, Windows Azure Connect, Improved Dev / IT Pro Experience
	December 2011 – Traffic manager, SQL Azure reporting, HPC scheduler
	June 2012 – Websites, Virtual machines for Windows and Linux, Python SDK, New portal, Locally redundant storage
	April 2014 – Windows Azure renamed to Microsoft Azure[1]
	July 2014 – Azure Machine Learning public preview[22]
	November 2014 – Outage affecting major websites including MSN.com.[23]
	September 2015 – Azure Cloud Switch introduced as a cross-platform Linux distribution.[24]
	Privacy[edit]
	Microsoft has stated that, per the USA Patriot Act, the US government could have access to the data even if the hosted company is not American and the data resides outside the USA.[25] However, Microsoft Azure is compliant with the E.U. Data Protection Directive (95/46/EC)[26][27][contradictory]. To manage privacy and security-related concerns, Microsoft has created a Microsoft Azure Trust Center,[28] and Microsoft Azure has several of its services compliant with several compliance programs including ISO 27001:2005 and HIPAA. A full and current listing can be found on the Microsoft Azure Trust Center Compliance page.[29] Of special note, Microsoft Azure has been granted JAB Provisional Authority to Operate (P-ATO) from the U.S. government in accordance with guidelines spelled out under the Federal Risk and Authorization Management Program (FedRAMP), a U.S. government program that provides a standardized approach to security assessment, authorization, and continuous monitoring for cloud services used by the federal government.[30]
	"""

	"""
	count=0
	for x in string.split():
		if("Azure" in x):
			count+=1

	print(count)
	"""
	def method_1():
		known_words=[]
		words={}
		#max_iterations=[]
		Max=0
		Min=0
		for x in string.split():
			if( x not in words.keys()):
				count=0
				for y in string.split():
					if( x == y):
						count+=1
				words[x]=count

				if(0 == Min):
					Min=count
					MinWord=x
					
				if(count < Min):
					Min=count
					MinWord=x
					
				if(count > Max):
					Max=count
					MaxWord=x
					

		print(words)
		print("\n\n----------------------\n\n")
		print(MaxWord, Max)
		print(MinWord, Min)

	def method_2():
		known_words=[]
		words={}
		#max_iterations=[]
		Max=0
		Min=0
		stringList=string.split()
		
		for x in stringList:
			if( x not in words.keys()):
				count=0
				for y in stringList:
					if( x == y):
						count+=1
				words[x]=count

				if(0 == Min):
					Min=count
					MinWord=x
					
				if(count < Min):
					Min=count
					MinWord=x
					
				if(count > Max):
					Max=count
					MaxWord=x

					

		print(words)
		print("\n\n----------------------\n\n")
		print(MaxWord, Max)
		print(MinWord, Min)

	import cProfile
	cProfile.run("method_1()")
	cProfile.run("method_2()")



#
# Print number in words
#

Number="199919"
TenPlus=["Ten","Eleven", "Twelve", "Thirten", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
Tens=["","","Twenty", "Thirty","Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"]
Positions=["Thousand", "Hunderd","",""]
NumberDic={'1':'One', '2':'Two', '3':'Three', '4': 'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine'}
StrNum=str(Number)
len_StrNum=len(StrNum)

for x in range(len_StrNum):
	#print(NumberDic[x], end=" ")
	if(StrNum[x] != '0'):
		if(x == len_StrNum-6):
			print(NumberDic[StrNum[x]],"Laks", end=" ")
		elif(x == len_StrNum-5):
			print(Tens[int(StrNum[x])], end=" ")
		elif(x == len_StrNum-2):
			if(StrNum[x] == '1'):
				if(len_StrNum>2):
					print("and", end=" ")
				print(TenPlus[int(StrNum[x+1])], end=" ")
				break
			else:
				print(Tens[int(StrNum[x])], end=" ")
		else:
			print(NumberDic[StrNum[x]],Positions[-(len_StrNum-x)], end=" ")

