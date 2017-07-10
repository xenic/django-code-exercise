# django-code-exercise
A code exercise for assessing Django skills.

# Introduction
The purpose of this exercise is to assess Django proficiency, understanding of MVT web application structure, object oriented programming with models, handling HTTP transactions with views, URL routing and design, but not be a brain teaser or esoteric. Use the Django web application framework to create a web application that allows teachers to track student attendance. The specifications are intentionally flexible, we want to see your personal style and the decisions you make as a developer and engineer. The exercise is open ended, we don’t expect anyone to fulfill all of the specifications, and the quality of work will be more important than quantity.

## Description and specifications
The student attendance application will be used in high school and middle school settings, so the application will need to be able to do the following.

* map a many-to-many relationship between students and teachers
* map a many-to-many relationship between students and classes
* map a many-to-many relationship between classes and teachers
* view student attendance by class
* view student attendance by grade
* view student attendance for the entire school
* view a specific student’s attendance
* allow the administration to enter a new student to the attendance role
* allow the administration to enter a new teacher
* allow the administration to create a new class
* allow the administration to add/enroll a student in a class
* allow the administration to mark a student absent, tardy or present for a class on a given day

A ‘class’ would be something like ‘3rd period 6th grade math’ or ‘5th period 7th grade art’. The administration can be a single privileged user or interface, and don’t worry about login’s or authentication authorization for this application. 


# Instructions
Fork this repository in GitHub, clone the repository to your local system, create a Django project with accompanying apps using a currently supported version of Django (1.7 – 1.11). Using the Django admin application and 3rd party packages is acceptable and encouraged. Also, along with writing unit tests, following PEP-8 and PEP-257, using PyLint and ReSTful URL design.

There is a lot of work here, we don’t expect you to complete the project. Where would you start? Show us what you got?
