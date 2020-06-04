# FullThrottleLab_BackendTest
Backend Test - FullThrottle Lab

Author : Mallikarjun J

In this Readme File, the below topics are discussed:
  1.Overview of the requirement(test)
  2.Database
  3.Members and session tables
  4.Superuser Credential
  5.Heroku Deployment
  6.Project Structure


1. Overview of the requirement:
The requirement for the test is to build a simple python/django backend system that reads a data from backend database(here, default SQLite3) data and display the output JSON API format. And to make this project ready to deply on Heroku.

2. Database:
In this project, I use the default SQLite DB. With the help of django Model, two tables are created and populate with sample dummy data:
a. Members
b. Sessions

3A. Memebers table store the following data:
  a. Text_id - eg:W012A3CDE
  b. real_name - eg:real_name
  c. tz - eg:America/Los_Angels

3B. Sessions table store the following data:
  a. text_id (forignkey) - eg:W012A3CDE
  b. start_time - eg: "Mar 1 2020  11:11AM"
  c. end_time - eg: "Mar 1 2020  20:00PM"
  
4. SuperUser Credential
 user : test
 password : test
 
 
5. Heroku Deployment ready.
To make this project ready, the necessary files needs to be created and placed in the project. Below are the steps to do so.


6. Project structure.
  Virtual Environment - venv_FTLabs_test
  Project directory - FT_djangoProject
  Application directory - FT_testApp 
