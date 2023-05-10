# VIRTUAL-ASSISTANT-USING-PYTHON
HALDIA INSTITUTE OF TECHNOLOGY
 Department is
 Master Of Computer Application
 4
th Semester, 2021-23
 UNDER THE GUIDANCE
Professor:- Apratim Mitra
PROJECT REPORT ON
 VIRTUAL ASSISTANT USING PYTHON
SUBMITTED BY :-
Pintoo Kumar Singh
 Roll No:- 10301021026
 Reg No:- 211030571010059
 Saswati Sinha Roy
Roll No:- 10301021041
Reg No:- 211030571010020
Date : 09/05/23
Certificate
This is to certify that the project entitled VIRTUAL ASSISTANT USING 
PYTHON is undertaken at the HALDIA INSTITUTE OF TECHNOLOGY by 
Pintoo Kumar Singh and group in partial fulfillment of MCA degree 
(Semester IV) Examination had not been submitted for any other examination 
and does not form part of any other course undergone by the candidate.
 It is further certified that he has completed all required phases of project.
Name of Students Signatures 
1. Pintoo Kumar Singh ……………………
Roll:- 10301021026 
2. Saswati Sinha Roy 
 Roll:- 10301021041 …………………….
 
Signature of Internal Guide Signature of External
HOD/In -Charge/Co-Ordinator
Acknowledgement
In completing this project report on project titled VIRTUAL ASSISTANT USING 
PYTHON, I had to take the help and guideline of a few respected people, who deserve my 
greatest gratitude.
The completion of this project report gives me much Pleasure. I would like to show 
my gratitude to Prof. Bipasa Biswas for giving me a good guideline for project throughout 
numerous consultations. I would also like to expand my deepest gratitude to all those who 
have directly and indirectly guided us in writing this project report.
We Are grateful to our project guide Mr Pintoo Kumar Singh For the guidance, 
inspiration and constructive suggestions that helpful us is the preparation of this project . 
We also thank our colleagues who have helped in successful completion of the project.
Pintoo Kumar Singh
Signature:-
Roll No:- 10301021026
Table of Contents
Sr. No Title Page No
1 Introduction 1
1.1 Background 2
1.2 Objectives 4
1.3 Purpose, Scope and Applicability 5
2 Survey of Technology 6
3 Requirement and Analysis 8
3.1 Problem Definition 8
3.2 Requirement Specification 9
3.3 Software and Hardware Requirement 11
4 System Design 12
4.1 ER Diagram 12
4.2 Activity Diagram 13
4.3 Class Diagram 14
4.4 Use Case Diagram 15
4.5 Sequence Diagram 16
4.6 Data Flow Diagram 18
4.7 Component Diagram 21
4.8 Deployment Diagram 22
4.9 Data Dictionary 23
4.10 Test Case Design 24
Reference and Bibliography 26
1
VIRTUAL ASSISTANT
1.INTRODUCTION
In today’s era almost all tasks are digitized. We have Smartphone in hands and it is 
nothing less than having world at your finger tips. These days we aren’t even using fingers. 
We just speak of the task and it is done. There exist systems where we can say Text Dad, “I’ll 
be late today.” And the text is sent. That is the task of a Virtual Assistant. It also supports 
specialized task such as booking a flight, or finding cheapest book online from various e￾commerce sites and then providing an interface to book an order are helping automate search, 
discovery and online order operations.
Virtual Assistants are software programs that help you ease your day to day tasks, such 
as showing weather report, creating reminders, making shopping lists etc. They can take 
commands via text (online chat bots) or by voice. Voice based intelligent assistants need an 
invoking word or wake word to activate the listener, followed by the command. For my 
project the wake word is anna. We have so many virtual assistants, such as Apple’s Siri, 
Amazon’s Alexa and Microsoft’s Cortana. For this project, wake word was chosen anna.
This system is designed to be used efficiently on desktops. Personal assistant software 
improves user productivity by managing routine tasks of the user and by providing 
information from online sources to the user. anna is effortless to use. Call the wake word 
‘anna’ followed by the command. And within seconds, it gets executed.
Voice searches have dominated over text search. Web searches conducted via mobile 
devices have only just overtaken those carried out using a computer and the analysts are 
already predicting that 60% of searches will be via voice by 2025.Virtual assistants are turning 
out to be smarter than ever. Allow your intelligent assistant to make email work for you. 
Detect intent, pick out important information, automate processes, and deliver personalized 
responses.
This project was started on the premise that there is sufficient amount of openly 
available data and information on the web that can be utilized to build a virtual assistant that 
has access to making intelligent decisions for routine user activities.
2
1.1 BACKGROUND
There already exist a number of desktop virtual assistants. A few examples of current 
virtual assistants available in market are discussed in this section along with the tasks they can 
provide and their drawbacks.
SIRI from Apple
SIRI is personal assistant software that interfaces with the user thru voice interface, 
recognizes commands and acts on them. It learns to adapt to user’s speech and thus improves 
voice recognition over time. It also tries to converse with the user when it does not identify the 
user request.
It integrates with calendar, contacts and music library applications on the device and 
also integrates with GPS and camera on the device. It uses location, temporal, social and task 
based contexts, to personalize the agent behavior specifically to the user at a given point of 
time.
Supported Tasks
⚫ Call someone from my contacts list
⚫ Launch an application on my iPhone
⚫ Send a text message to someone
⚫ Set up a meeting on my calendar for 9am tomorrow
⚫ Set an alarm for 5am tomorrow morning
⚫ Play a specific song in my iTunes library
⚫ Enter a new note
Drawback
SIRI does not maintain a knowledge database of its own and its understanding comes 
from the information captured in domain models and data models.
3
ReQall
ReQall is personal assistant software that runs on smartphones running Apple iOS or 
Google Android operating system. It helps user to recall notes as well as tasks within a 
location and time context. It records user inputs and converts them into commands, and 
monitors current stack of user tasks to proactively suggest actions while considering any 
changes in the environment. It also presents information based on the context of the user, as 
well as filter information to the user based on its learned understanding of the priority of that 
information.
Supported Tasks
⚫ Reminders
⚫ Email
⚫ Calendar, Google Calendar
⚫ Outlook
⚫ Evernote
⚫ Facebook, LinkedIn
⚫ News Feeds
Drawback
Will take some time to put all of the to-do items in – you could spend more time 
putting the entries in than actually doing the revision.
4
1.2 OBJECTIVES
Main objective of building personal assistant software (a virtual assistant) is using 
semantic data sources available on the web, user generated content and providing knowledge 
from knowledge databases. The main purpose of an intelligent virtual assistant is to answer 
questions that users may have. This may be done in a business environment, for example, on 
the business website, with a chat interface. On the mobile platform, the intelligent virtual 
assistant is available as a call-button operated service where a voice asks the user “What can I 
do for you?” and then responds to verbal input.
Virtual assistants can tremendously save you time. We spend hours in online research 
and then making the report in our terms of understanding. anna can do that for you. Provide a 
topic for research and continue with your tasks while anna does the research. 
One of the main advantages of voice searches is their rapidity. In fact, voice is reputed 
to be four times faster than a written search: whereas we can write about 40 words per minute, 
we are capable of speaking around 150 during the same period of time15. In this respect, the 
ability of personal assistants to accurately recognize spoken words is a prerequisite for them to
be adopted by consumers.
5
1.3 PURPOSE, SCOPE AND APPLICABILITY
Purpose
Purpose of virtual assistant is to being capable of voice interaction, music playback, 
making to-do lists, setting alarms, streaming podcasts, playing audio books, and providing 
weather, traffic, sports, and other real-time information, such as news. Virtual assistants 
enable users to speak natural language voice commands in order to operate the device and its 
apps.
There is an increased overall awareness and a higher level of comfort demonstrated 
specifically by millennial consumers. In this ever-evolving digital world where speed, 
efficiency, and convenience are constantly being optimized, it’s clear that we are moving 
towards less screen interaction.
Scope
Voice assistants will continue to offer more individualized experiences as they get 
better at differentiating between voices. However, it’s not just developers that need to address 
the complexity of developing for voice as brands also need to understand the capabilities of 
each device and integration and if it makes sense for their specific brand. They will also need 
to focus on maintaining a user experience that is consistent within the coming years as 
complexity becomes more of a concern. This is because the visual interface with voice 
assistants is missing. Users simply cannot see or touch a voice interface.
Applicability
The mass adoption of artificial intelligence in users’ everyday lives is also fueling the 
shift towards voice. The number of IoT devices such as smart thermostats and speakers are 
giving voice assistants more utility in a connected user’s life. Smart speakers are the number 
one way we are seeing voice being used. Many industry experts even predict that nearly every 
application will integrate voice technology in some way in the next 5 years.
The use of virtual assistants can also enhance the system of IoT (Internet of Things). 
Twenty years from now, Microsoft and its competitors will be offering personal digital 
assistants that will offer the services of a full-time employee usually reserved for the rich and 
famous.
6
2. SURVEY OF TECHNOLOGY
Python
Python is an OOPs (Object Oriented Programming) based, high level, interpreted 
programming language. It is a robust, highly useful language focused on rapid 
application development (RAD). Python helps in easy writing and execution of codes. Python 
can implement the same logic with as much as 1/5th code as compared to other OOPs 
languages.
Python provides a huge list of benefits to all. The usage of Python is such that it cannot 
be limited to only one activity. Its growing popularity has allowed it to enter into some of the 
most popular and complex processes like Artificial Intelligence (AI), Machine Learning (ML), 
natural language processing, data science etc. Python has a lot of libraries for every need of 
this project. For anna, libraries used are speech recognition to recognize voice, Pyttsx for text 
to speech, selenium for web automation etc.
Python is reasonably efficient. Efficiency is usually not a problem for small examples. 
If your Python code is not efficient enough, a general procedure to improve it is to find out 
what is taking most the time, and implement just that part more efficiently in some lower-level 
language. This will result in much less programming and more efficient code (because you 
will have more time to optimize) than writing everything in a low-level language.
DBpedia
Knowledge bases are playing an increasingly important role in enhancing the 
intelligence of Web and enterprise search and in supporting information integration. The 
DBpedia leverages this gigantic source of knowledge by extracting structured information 
from Wikipedia and by making this information accessible on the Web. The DBpedia 
knowledge base has several advantages over existing knowledge bases: it covers many 
domains; it represents real community agreement; it automatically evolves as Wikipedia 
changes, and it is truly multilingual.
7
The DBpedia knowledge base allows you to ask quite surprising queries against 
Wikipedia for instance “Give me all cities in New Jersey with more than 10,000 inhabitants” 
or “Give me all Italian musicians from the 18th century”.
Quepy
Quepy is a python framework to transform natural language questions to queries in a 
database query language. It can be easily customized to different kinds of questions in natural 
language and database queries. So, with little coding you can build your own system for 
natural language access to your database.
Pyttsx
Pyttsx stands for Python Text to Speech. It is a cross-platform Python wrapper for text￾to-speech synthesis. It is a Python package supporting common text-to-speech engines on Mac 
OS X, Windows, and Linux. It works for both Python2.x and 3.x versions. Its main advantage 
is that it works offline.
Speech Recognition
This is a library for performing speech recognition, with support for several engines 
and APIs, online and offline. It supports APIs like Google Cloud Speech API, IBM Speech to 
Text, Microsoft Bing Voice Recognition etc.
SQLite
SQLite is a capable library, providing an in-process relational database for efficient 
storage of small-to-medium-sized data sets. It supports most of the common features of SQL 
with few exceptions. Best of all, most Python users do not need to install anything to get 
started working with SQLite, as the standard library in most distributions ships with the sqlite3 
module.
SQLite runs embedded in memory alongside your application, allowing you to easily 
extend SQLite with your own Python code. SQLite provides quite a few hooks, a reasonable 
subset of which are implemented by the standard library database driver.
8
3. REQUIREMENT AND ANALYSIS
System Analysis is about complete understanding of existing systems and finding 
where the existing system fails. The solution is determined to resolve issues in the proposed 
system. It defines the system. The system is divided into smaller parts. Their functions and 
inter relation of these modules are studied in system analysis. The complete analysis is 
followed below.
3.1 Problem definition
Usually, user needs to manually manage multiple sets of applications to complete one 
task. For example, a user trying to make a travel plan needs to check for airport codes for 
nearby airports and then check travel sites for tickets between combinations of airports to 
reach the destination. There is need of a system that can manage tasks effortlessly.
We already have multiple virtual assistants. But we hardly use it. There are number of 
people who have issues in voice recognition. These systems can understand English phrases 
but they fail to recognize in our accent. Our way of pronunciation is way distinct from theirs. 
Also, they are easy to use on mobile devices than desktop systems. There is need of a virtual 
assistant that can understand English in Indian accent and work on desktop system.
When a virtual assistant is not able to answer questions accurately, it’s because it lacks 
the proper context or doesn’t understand the intent of the question. Its ability to answer 
questions relevantly only happens with rigorous optimization, involving both humans and 
machine learning. Continuously ensuring solid quality control strategies will also help manage 
the risk of the virtual assistant learning undesired bad behaviors. They require large amount of 
information to be fed in order for it to work efficiently.
Virtual assistant should be able to model complex task dependencies and use these 
models to recommend optimized plans for the user. It needs to be tested for finding optimum 
paths when a task has multiple sub-tasks and each sub-task can have its own sub-tasks. In such 
a case there can be multiple solutions to paths, and the it should be able to consider user 
preferences, other active tasks, priorities in order to recommend a particular plan.
9
3.2 REQUIREMENT SPECIFICATION
Personal assistant software is required to act as an interface into the digital world by 
understanding user requests or commands and then translating into actions or 
recommendations based on agent’s understanding of the world.
anna focuses on relieving the user of entering text input and using voice as primary 
means of user input. Agent then applies voice recognition algorithms to this input and records 
the input. It then use this input to call one of the personal information management 
applications such as task list or calendar to record a new entry or to search about it on search 
engines like Google, Bing or Yahoo etc. Focus is on capturing the user input through voice, 
recognizing the input and then executing the tasks if the agent understands the task. Software 
takes this input in natural language, and so makes it easier for the user to input what he or she 
desires to be done.
Voice recognition software enables hands free use of the applications, lets users to 
query or command the agent through voice interface. This helps users to have access to the 
agent while performing other tasks and thus enhances value of the system itself. 
Virtual assistants must provide a wide variety of services. These include:
⚫ Providing information such as weather, facts from e.g. Wikipedia etc.
⚫ Set an alarm or make to-do lists and shopping lists.
⚫ Remind you of birthdays and meetings.
⚫ Play music from streaming services such as Saavn and Gaana.
⚫ Play videos, TV shows or movies on televisions, streaming from e.g. Netflix or 
Hotstar.
⚫ Book tickets for shows, travel and movies.
10
Feasibility Study 
Feasibility study can help you determine whether or not you should proceed with 
your project. It is essential to evaluate cost and benefit. It is essential to evaluate cost and 
benefit of the proposed system. Five types of feasibility study are taken into consideration.
1. Technical feasibility: It includes finding out technologies for the project, both 
hardware and software. For virtual assistant, user must have microphone to convey 
their message and a speaker to listen when system speaks. These are very cheap now a 
days and everyone generally possess them. Besides, system needs internet connection. 
While using anna, make sure you have a steady internet connection. It is also not an 
issue in this era where almost every home or office has Wi-Fi.
2. Operational feasibility: It is the ease and simplicity of operation of proposed system. 
System does not require any special skill set for users to operate it. In fact, it is 
designed to be used by almost everyone. Kids who still don’t know to write can read 
out problems for system and get answers.
3. Economical feasibility: Here, we find the total cost and benefit of the proposed 
system over current system. For this project, the main cost is documentation cost. User 
also would have to pay for microphone and speakers. Again, they are cheap and 
available. As far as maintenance is concerned, anna won’t cost too much.
4. Organizational feasibility: This shows the management and organizational structure 
of the project. This project is not built by a team. The management tasks are all to be 
carried out by a single person. That won’t create any management issues and will 
increase the feasibility of the project.
5. Cultural feasibility: It deals with compatibility of the project with cultural 
environment. Virtual assistant is built in accordance with the general culture. The 
project is named anna technically feasible with no external hardware requirements. Also it is 
simple in operation and does not cost training or repairs. Overall feasibility study of the project 
reveals that the goals of the proposed system are achievable. Decision is taken to proceed with 
the project.
11
3.3 HARDWARE AND SOFTWARE REQUIREMENTS 
The software is designed to be light-weighted so that it doesn’t be a burden on the 
machine running it. This system is being build keeping in mind the generally available 
hardware and software compatibility. Here are the minimum hardware and software 
requirement for virtual assistant.
Hardware: 
⚫ Pentium-pro processor or later.
⚫ RAM 512MB or more.
Software: 
⚫ Windows 7(32-bit) or above.
⚫ Python 2.7 or later
⚫ Chrome Driver
⚫ Selenium Web Automation
⚫ SQLite
12
4. SYSTEM DESIGN 
4.1 ER DIAGRAM 
The above diagram shows entities and their relationship for a virtual assistant system. 
We have a user of a system who can have their keys and values. It can be used to store any 
information about the user. Say, for key “name” value can be “Jim”. For some keys user might 
like to keep secure. There he can enable lock and set a password (voice clip).
Single user can ask multiple questions. Each question will be given ID to get 
recognized along with the query and its corresponding answer. User can also be having n 
number of tasks. These should have their own unique id and status i.e. their current state. A 
task should also have a priority value and its category whether it is a parent task or child task 
of an older task.
13
4.2 ACTIVITY DIAGRAM 
Initially, the system is in idle mode. As it receives any wake up cal it begins execution.
The received command is identified whether it is a questionnaire or a task to be performed. 
Specific action is taken accordingly. After the Question is being answered or the task is being 
performed, the system waits for another command. This loop continues unless it receives quit 
command. At that moment, it goes back to sleep.
14
4.3 CLASS DIAGRAM 
The class user has 2 attributes command that it sends in audio and the response it 
receives which is also audio. It performs function to listen the user command. Interpret it and 
then reply or sends back response accordingly. Question class has the command in string form 
as it is interpreted by interpret class. It sends it to general or about or search function based on 
its identification.
The task class also has interpreted command in string format. It has various functions 
like reminder, note, mimic, research and reader.
15
4.4 USE CASE DIAGRAM 
In this project there is only one user. The user queries command to the system. System 
then interprets it and fetches answer. The response is sent back to the user.
16
4.5 SEQUENCE DIAGRAM 
4.5.1 Sequence diagram for Query-Response
The above sequence diagram shows how an answer asked by the user is being fetched 
from internet. The audio query is interpreted and sent to Web scraper. The web scraper 
searches and finds the answer. It is then sent back to speaker, where it speaks the answer to 
user.
17
4.5.2 Sequence diagram for Task Execution
The user sends command to virtual assistant in audio form. The command is passed to 
the interpreter. It identifies what the user has asked and directs it to task executer. If the task is 
missing some info, the virtual assistant asks user back about it. The received information is 
sent back to task and it is accomplished. After execution feedback is sent back to user.
18
4.6 DATA FLOW DIAGRAM 
4.6.1 DFD Level 0 (Context Level Diagram)
4.6.2 DFD Level 1
19
4.6.3 DFD Level 2
Data Flow in Assistance
Managing User Data
20
Data Flow in Kid Zone
Settings of virtual Assistant
21
4.7 COMPONENT DIAGRAM
The main component here is the Virtual Assistant. It provides two specific service, 
executing Task or Answering your question.
22
4.8 DEPLOYMENT DIAGRAM
The user interacts with SQLite database using SQLite connection in Python code. The 
knowledge database DBPedia must be accessed via internet connection. This requires LAN or 
WLAN / Ethernet network.
23
4.9 DATA DICTIONARY
User
Key Text
Value Text
Lock Boolean
Password Text
Question
Qid Integer PRIMARY KEY
Query Text
Answer Text
Task
Tid Integer PRIMARY KEY
Status Text (Active/Waiting/Stopped)
Level Text (Parent/Sub)
Priority Integer
Reminder
Rid Integer PRIMARY KEY
Tid Integer FOREIGN KEY
What Text
When Time
On Date
Notify before Time
Note
Nid Integer PRIMARY KEY
Tid Integer FOREIGN KEY
Data Text
Priority Integer
24
4.10 TEST CASE DESIGN
• Test Case 1
Test Title: Response Time
Test ID: T1
Test Priority: High
Test Objective: To make sure that the system respond back time is efficient.
Description:
Time is very critical in a voice based system. As we are not typing inputs, we are 
speaking them. The system must also reply in a moment. User must get instant response of the 
query made.
• Test Case 2 
Test Title: Accuracy 
Test ID: T2
Test Priority: High
Test Objective: To assure that answers retrieved by system are accurate as per gathered data.
Description:
A virtual assistant system is mainly used to get precise answers to any question asked. 
Getting answer in a moment is of no use if the answer is not correct. Accuracy is of utmost 
importance in a virtual assistant system.
25
• Test Case 3
Test Title: Approximation
Test ID: t3
Test priority: Moderate
Test Objective: To check approximate answers about calculations.
Description:
There are times when mathematical calculation requires approximate value. For 
example, if someone asks for value of PI the system must respond with approximate value and 
not the accurate value. Getting exact value in such cases is undesirable.
Note: There might include a few more test cases and these test cases are also subject to change 
with the final software development.
26
REFERENCE AND BIBLIOGRAPHY
• Websites referred
▪ www.stackoverflow.com
▪ www.pythonprogramming.net
▪ www.codecademy.com
▪ www.tutorialspoint.com
▪ www.google.co.in
• Books referred
▪ Python Programming - Kiran Gurbani
▪ Learning Python - Mark Lutz
• YouTube Channels referred
▪ CS Dojo
▪ edureka!
▪ CodeWithHarry
• Documents referred
▪ Designing Personal Assistant Software for Task Management using Semantic 
Web Technologies and Knowledge Databases
- Purushotham Botla
▪ Python code for Artificial Intelligence: Foundations of Computational Agents
- David L. Poole and Alan K. Mackworth
THANK YOU

youtube link: https://www.youtube.com/watch?v=Lp9Ftuq2sVI
