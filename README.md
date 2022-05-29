# Attendance_Tracker
This is a project done for the Microsoft Engage Program 2022 <br>
**ATTENDANCE TRACKER BY GAHANA R**

It is a web application that may be used to track employee attendance using facial recognition technology. This project was created as part of the 
Microsoft Engage Program 2022, in which mentees were required to create a product with the use of facial recognition.

**Motivation:**<br>
Attendance tracking is vital to all organizations irrespective of size and industry. The management must track and record attendance accurately as it is
directly connected to other HR components like Payroll, leave, etc. Facial recognition is the new generation attendance tracking system widely accepted globally.

**Solved Problem:**<br> 
Employees faces may be accurately scanned using the attendance tracker, which can be downloaded on any device. The device remembers the matched face
for all future check-ins once it has been registered.

**Learnings:**<br> 
Under the skilled direction of my mentor, Mazhar Ali Beg sir, through the Microsoft Engage Mentorship Program 2022. I was able to progress from someone who
could only create static web pages to someone who can create full stack web applications.

# Table of contents	
1. [Features of Applications](#features-of-the-application)
2. [Installation](#installation)
3. [Tech Stack Selection](#tech-stack-selection)
4. [Challenges Faced](#challenges-faced)
5. [Future Scope](#future-scope)
6. [User Interface](#user-interface)
7. [Support and contact](#support-and-contact)

## Features of the Application
1. Login 
2. Confirm user name and password check 
3. Home 
4. Check-in attendance through facial recognition 
5. View attendance report

## Installation
Install [Python](https://www.python.org/) and add it to the environment variable path and make sure you have version 22.1.1 or higher of pip. You can check version using:
``` 
pip --version
```
If not then you can upgrade using:
```
python -m pip install --upgrade pip
```
clone this repository
```
git clone https://github.com/gana2002/Attendance_Tracker.git
```
Go into the repository directory
```
cd Attendance_Tracker/attendance_Tracker
```
Click this [dlib-error resolved](https://github.com/datamagic2020/Install-dlib)

Install the requirements using:
```
pip install -r requirements.txt
```
Now change the path of the images by pasting the path of the images directory inside the attendance_tracker in the file named ml_code.py which is inside main directory.<br><br>
Also change the path of the attendance.csv file in the same way.

### Start the server using:
```
python manage.py runserver
```

## Tech Stack Selection 
Despite all of the smart devices available today, one thing remains constant: online and internet browsers. I choose to make my product a web application so that 
a big number of people may easily use it and connect with one another.

I used HTML, CSS, Javascript, Bootstrap, Tailwind CSS, and PHP for frontend development. I utilised Python, Django, and db.sqlite3 for backend development.
The FACE RECOGNITION 1.3.0 Library was used to recognise faces and distinguish between persons. It's made with deep learning and dlib's state-of-the-art face 
recognition. In the Wild benchmark, this model has a 99.38 percent accuracy on the identified faces.

How to build a facial recognition system in python suing OpenFace and dlib?!

1.	Encode a picture using the HOG algorithm to create a simplified version of the image. Using this simplified image, find the part of the image that most looks 
	  like a generic HOG encoding of a face.
2.	Figure out the pose of the face by finding the main landmarks in the face. Once we find those landmarks, use them to warp the image so that the eyes and mouth 
   	are centered.
3.	Pass the centered face image through a neural network that knows how to measure features of the face. Save those 128 measurements.
4.	Looking at all the faces we’ve measured in the past, see which person has the closest measurements to our face’s measurements. That’s our match!

I divided my entire development process into 4 sprints (each having the duration of 5 days) as shown in the images below. I gave due importance to the bug review and 
fixing part of the development process as it is crucial to offer whatever features you are offering are offered with utmost perfection.

1. I analysed all three problems and decided on facial recognition as the most interesting. And I decided to design an attendance tracking system because it is something. I am more familiar with. Make a list of the highlights. After that, I began with I started the model by using an API that has already been trained on a big dataset, as well as loading and executing the model. I gave the mentor an update on my progress.
2. Consulted with mentor and decided on Django as the framework because it was popular and met all of the requirements. Using Django and Python, I created a whole pipeline. Because I was working on these technologies for the first time, it required some time.
3. The frontend section was created in accordance with the requirements. I attempted to make use of the available frameworks in order to provide a pleasant user experience. Examine and correct the flaws.
4. I completed the documentation as well as the README and submitted it along with the demo video. Adjusting AceHacker Assignments To cater to the assignments provided by the AceHacker platform and also undertake the tasks and suggestions provided by the mentors, I made a separate card where I put these assignments and made sure I was completing them alongside my ongoing sprints.


## Challenges Faced
"If you are not facing challenges while developing an application, you are not considering every possible case for a better experience of your users."<br>
During the development process I faced the following challenges:
1. Understanding the working of the backend side of my application as I had never worked with web backend before. However, thanks to online communities, 
 stackoverflow, my mentors and friends I was able to find resources which helped me in creating this web application.
2. Preparing a feature list. In the beginning I wanted to build an app like no other and incorporate many features. But in the interest of time, I had to narrow down the features to the basic functionalities that are available in an attendance tracking system. 
3. Error while downloading all the ml libraries like [dlib](https://github.com/datamagic2020/Install-dlib)

All these challenges were less of challenges and more of lessons, lessons to help me have an even better development process in the future so that I can incorporate the customers' requests and requirements easily and efficiently.

## User Interface

## Future Scope
1. To make my app more accurate and support large datasets.
2. To make registrations of the new employees through the front end.
3. To make it more scalable and user friendly.

## SUPPORT AND CONTACT 
* EMAIL: [Gahana R](mailto:writetogahana@gmail.com) 
