# Design Notes
- Need Student, Teacher, Class, and Attendance tables.  Classes will act as the map between teachers and students.
- Would be nice to have a few additional support tables like Status, and Grade
- Student m2m Class
- Teacher m2m Class
- Attendance has FK to Student, Class, and Status, and a date field.
- Build ReST api endpoints for each model, though in phase 1, just use the built in Django Admin for creating students, teachers and classes.
- Build additional views/endpoints/filters for all viewing needs (students by class, students by grade, all students attendance, etc)
- Build a UI for displaying these.  For phase 1, a single page api endpoint with javascript navigation to hit endpoints and display results

- Next step to MVP: on select of status, submit a put/patch for that student's attendance for that class/day.
- Figure out ways to display attendance data in an interesting and useful fashion.


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
* allow the teacher for a class to mark a student absent, tardy or present for their class on a given day

Examples of a ‘class’ are ‘3rd period 6th grade math’ or ‘5th period 7th grade art’. The administration can be a single privileged user or interface. The ‘users’ of the application will be the teachers but don’t worry about login or authentication authorization for this application. 


# Instructions
Fork this repository in GitHub, clone the repository to your local system, create a Django project with accompanying apps using a currently supported version of Django (1.7 – 1.11). Using the Django admin application and 3rd party packages is acceptable and encouraged. Also, using unit tests, following PEP-8 and PEP-257, using PyLint and ReSTful URL design is encouraged.

As for the data store layer the default SQLite database is preferred, and using the Django template engine is also preferred. In addition, concentrate on the server side implementation verses the client side development. Simple HTML templates and forms are expected.

There is a lot of work here, we don’t expect you to complete the project. After getting the basic Django project and app structure created, take 2 – 3 hours and see what you can get done. Where would you start? How would you go about tackling this project? Show us what you got?
