# Break-reCaptcha

Term Project Subject: Break reCaptcha
Alexander Hohl, Ali Mohammad, Bijan Razavi, Jeongwan Park

Problem definition
 
A.   What is reCaptcha?

reCAPTCHA is a free service that protects your website from spam and abuse. reCAPTCHA uses an advanced risk analysis engine and adaptive CAPTCHAs to keep automated software from engaging in abusive activities on your site. It does this while letting your valid users pass through with ease.
 
B.	Project mission

We conducted research to pass reCAPTCHA through a non-human machine. Especially, we will collect the test data automatically and learn the test data collected by applying the machine learning concept of artificial intelligence, which is the most popular technology in recent years; so that the computer can judge the word presented by Google itself and select the picture. To do so, We first thought about how to read the mouse position where the picture is located through machine learning, and then move the mouse to that position automatically. If the project is successful, we will get ideas to bypass the latest security technologies. Through this, we think that we can prepare for security threat using artificial intelligence in the future, and can suggest ideas to prepare against cyber threats in corporation or public institution. For a short period of time, there was a lot of difficulty in learning and implementing languages and tools related to machine learning such as Python and TensorFlow. Even after the semester ends, we will continue to research and develop the project.
 
C.	Project Roadmap

We divided the project into three parts as shown below. We had meetings every week. We also developed the project by implementing a test program.
 
1. Implement mouse movement like a human moves, read the x and y positions
                            on the actual screen, move to the position and perform a click event
2. Using the web crawler to collect images and screenshot to split
3. Image classification and machine learning using the TensorFlow
 
TensorFlow: Open source software library for machine learning(AI) used in Google products. It was created by the Google Brain Team for Google research and product development and was released as an Apache 2.0 open source license on November 9, 2015

Feasibility Study Document
 
The three ideas we tried for Break reCaptcha (1. Automatic mouse movement, 2. Image analysis using machine learning, 3. Automatic image collection using web crawler) are unique ideas for team projects. The system that we have completed by combining the three methods is a new system. Of course, there have been many studies to break reCaptcha in the past, but we set up a roadmap in three major ways to study and implement machine learning in a limited project period.
 
Each detail topic is an extension and development of the existing technology.
 
Mouse Movement

Utilizes an automated GUI library, such as pyauto, to implement mouse movements like human motion.
PyAuto is a python interface to Chromium's automation framework. PyAuto brings the Automation Proxy interface to python. It can be used to launch the browser, navigate to a URL, query the state of tabs, windows, etc. Therefore, it can be used to automate functional tests. Additionally, since python can be used interactively in a shell, PyAuto allows you to play around with chromium using a scripting framework.

      2.     Utilize the Google Tensor Flow Machine Learning Library

Learning and classifying images using CNN (Convolutional neural network), an image recognition algorithm of TensorFlow
CNN : In machine learning, a convolutional neural network (CNN, or ConvNet) is a class of deep, feed-forward artificial neural networks that has successfully been applied to analyzing visual imagery.
 
      3.     Automatic Image Collection with WebCrawler and Screenshot

Automatically collects specific images from web pages by implementing and utilizing web crawler and take screenshot using pyscreenshot and pillow library.
Web crawler: A web crawler is a computer program that navigates the World Wide Web in an organized, automated way. The work that a web crawler does is called web crawling or spidering. Many sites, such as search engines, crawl the web to keep the data up-to-date. Web crawlers are often used to create copies of all the pages of a visited site, and the search engine indexes these pages for faster searching. The crawler is also used for automatic maintenance of websites, such as link checking and HTML code verification, and is also used to collect certain types of information on web pages, such as automatic e-mail collection. Web crawlers are a form of bot or software agent. Web crawlers usually start with a list of URLs, called seeds, that recognize all hyperlinks on the page and update the list of URLs. The updated URL list recursively visits again.


Software requirements specification document

1.	Functional requirements

a. 	The user executes the break reCaptcha program. The program automatically recognizes Google's reCaptcha program
b.	The Break reCaptcha program uses the human like mouse movement to click on the <I'm not a robot>in the reCaptcha 
c. 	When the image recognition process of the reCaptcha program is performed, it screenshot the image (3X3) and splits each image
d.	Confirm whether the split image is a picture of the presented word through a machine learning program using TensorFlow. If the picture is correct, click on the human like mouse movement, or go to the next picture
e.  Finally, we can bypass the Google reCaptcha
 
2.	Use Case Diagram

Use case name
Execute break reCaptcha 
Actor
User or Developer
Action
User execute break reCaptcha program
Precondition
 
Post condition
 
 
Use case name
Mouse movement
Actor
Break reCaptcha program
Action
Human like mouse movement to click reCaptcha 
Precondition
Using reCaptcha test page
Post condition
Execute Google reCaptcha 
 
Use case name
Image recognition
Actor
Break reCaptcha program
Action
Determine if the picture is correct through machine learning
Precondition
Recognize each split image
Post condition
Returns whether the recognized image is correct
 
Use case name
Image screenshot
Actor
Break reCaptcha program
Action
User execute break reCaptcha program
Precondition
Execution of Google reCaptcha 
Post condition
Split image into machine learning program
 
Use case name
Click or Pass image
Actor
Break reCaptcha program
Action
If it is a image that matches the proposal, click or pass
Precondition
Determine if the image is correct through machine learning process
Post condition
Google reCaptcha bypass
 
  
3.	System constraints

Python is used as development language, and Python and TensorFlow library(pyauto, pyscreenshot, pillow, numpy and etc) is used. We need a high-performance GPU to shorten the machine learning process time because we need image classification and learning using a TensorFlow to bypass the Google's reCaptcha program that is being used on the website.

4.	Design specification 

a. Software architecture

b. Use Case diagram



b. Sequence diagram


Comments: 
IMNAR position: position of the checkbox “I’m not a robot”
CI positions: positions of the images whose classification matches the search term (i.e. “car”)
V position: position of the “Verify” button 


c. Complete class diagram with all the classes and their relationships


d. Component diagram




e. Deployment diagram


Technical Document

1.	Programming languages

Python: Python is an advanced programming language released by Guido van Rossum in 1991 and is a platform independent, interpreter, object-oriented, dynamically typed ) Is an interactive language. The name Python comes from Guido's favorite comedy, "Monty Python's Flying Circus."
 Python is becoming the standard programming language for data science. Python combines the benefits of a general-purpose programming language with the convenience of a scripting language for specific areas such as MATLAB and R. Python has libraries for data loading, visualization, statistics, natural language processing, and image processing. Many of these tools are very handy for implementing machine learning. So we decided to use Python to run the project.
TensorFlow: Made by Google as a package for machine learning. We can implement machine learning using the package in Python. TensorFlow is widely used in the field of machine learning (deep running) because of its ease of use and the ability to process a lot of data.
 
2.	Reused algorithms and programs

Machine Learning Algorithm CNN (Convolutional Neural Network): Use CNN algorithm for project image classification and learning. The CNN algorithm (Convolutional Neural Network, CNN) is a type of Multiplayer perception designed to use minimal preprocessing. It consists of one or several Convolutional layers and the ANN layers on top of them, and utilizes additional weighting and pooling layers. This structure provides good performance in both video and voice fields compared to other deep-running structures.
 
3.	Tools and environments

Development environment: We are using ATOM Editor and PyCharm IDE. ATOM is a text editor created by Github, developed as open source and first released under MIT license in 2014. And, PyCharm is an IDE used in computer programming, specifically for the Python language. It is developed by JetBrains. Use the Pycharm IDE and ATOM Editor as the Python development environment for the Break reCaptcha project.
Version and configuration management: Using Github. Github is a version control system that records changes in files in a step-by-step version. Create a project in Github to manage the configuration and share and manage the modules developed by each team member.
 
Url: https://cci-git.uncc.edu/brazavi/Break-reCaptcha

 
4.	Database system(not use)
5.	Text files(not use)



