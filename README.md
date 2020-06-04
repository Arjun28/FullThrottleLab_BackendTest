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
  7.Input URL
  8.Output JSON data


1. Overview of the requirement:
The requirement for the test is to build a simple python/django backend system that reads a data from backend database(here, default SQLite3) data and display the output JSON API format. And to make this project ready to deploy on Heroku.

2. Database:
In this project, I use the default SQLite DB. With the help of django Model, two tables are created and populate with sample dummy data:
a. Members
b. Sessions

3A. Memebers table store the following data:
  a. Text_id - eg:W012A3CDE
  b. real_name - eg:real_name
  c. tz - eg:America/Los_Angels

3B. Sessions table store the following data:
  a. text_id (foreignkey) - eg:W012A3CDE
  b. start_time - eg: "Mar 1 2020  11:11AM"
  c. end_time - eg: "Mar 1 2020  20:00PM"
  
4. SuperUser Credential
 user : test
 password : test
 
 
5. Heroku Deployment ready.
To make this project ready, the necessary files needs to be created and placed in the project. Below are the steps to do so.
a. Install packages in the virtual enviroment - psycopg2==2.7, django-heroku, gunicorn
b. Freezed - requirements.txt 
c. created runtime.txt
d. BuiltProcfile
e. Made according chages to settings.py

6. Project structure.
  Virtual Environment - venv_FTLabs_test
  Project directory - FT_djangoProject
  Application directory - FT_testApp 


7. Input URL:
http://127.0.0.1:8000/getall/ | (localhost:port/url)


8. Output : JSON API 

{
  "ok": true,
  "members": [
    {
      "id": "W012A3CDE",
      "real_name": "Egon Spengler",
      "tz": "America/Los_Angeles",
      "activity_periods": [
        {
          "start_time": "2020-02-01 13:33:00+00:00",
          "end_time": "2020-02-01 13:54:00+00:00"
        },
        {
          "start_time": "2020-03-01 11:11:00+00:00",
          "end_time": "2020-03-01 14:00:00+00:00"
        },
        {
          "start_time": "2020-03-10 06:00:00+00:00",
          "end_time": "2020-03-10 08:00:00+00:00"
        }
      ]
    },
    {
      "id": "W07QCRPA4",
      "real_name": "Glinda Southgood",
      "tz": "Asia/Kolkata",
      "activity_periods": [
        {
          "start_time": "2020-06-04 03:29:49+00:00",
          "end_time": "2020-06-04 12:00:00+00:00"
        },
        {
          "start_time": "2020-06-04 06:00:00+00:00",
          "end_time": "2020-06-04 06:05:00+00:00"
        },
        {
          "start_time": "2020-05-04 02:30:47+00:00",
          "end_time": "2020-05-04 03:31:00+00:00"
        }
      ]
    },
    {
      "id": "W013A4ABC",
      "real_name": "Arjun J",
      "tz": "Asia/Karnataka",
      "activity_periods": [
        {
          "start_time": "2020-06-01 18:00:00+00:00",
          "end_time": "2020-06-04 03:31:39+00:00"
        }
      ]
    },
    {
      "id": "W08QCFPA5",
      "real_name": "Uday Raj",
      "tz": "Asia/Nepal",
      "activity_periods": [
        {
          "start_time": "2020-04-28 08:32:02+00:00",
          "end_time": "2020-04-28 03:32:13+00:00"
        }
      ]
    },
    {
      "id": "W019A5ABX",
      "real_name": "George Smith",
      "tz": "America/Nevada",
      "activity_periods": [
        {
          "start_time": "2020-06-01 03:32:33+00:00",
          "end_time": "2020-06-04 03:32:39+00:00"
        }
      ]
    },
    {
      "id": "W18QCFPA6",
      "real_name": "Justin Worth",
      "tz": "America/Washington",
      "activity_periods": [
        {
          "start_time": "2020-02-26 00:00:00+00:00",
          "end_time": "2020-02-26 12:00:00+00:00"
        },
        {
          "start_time": "2020-06-04 03:33:29+00:00",
          "end_time": "2020-06-04 03:33:32+00:00"
        }
      ]
    },
    {
      "id": "W031CRPAZ",
      "real_name": "Samart P",
      "tz": "Asia/Tamil_Nadu",
      "activity_periods": [
        {
          "start_time": "2020-06-02 12:00:00+00:00",
          "end_time": "2020-06-02 12:00:10+00:00"
        }
      ]
    },
    {
      "id": "W01X89AMQ",
      "real_name": "Sameer Christ",
      "tz": "America/Los_Angeles",
      "activity_periods": [
        {
          "start_time": "2020-05-05 18:00:00+00:00",
          "end_time": "2020-05-05 22:00:00+00:00"
        },
        {
          "start_time": "2020-05-29 03:34:44+00:00",
          "end_time": "2020-05-29 03:55:48+00:00"
        }
      ]
    }
  ]
}
