# This is my final project for 
# ITSS 4312.501 - Mobile Web Application Development - F22

(Most of the effort on this project was spent on the backend components, frontend/UI effort was minimal!)

# Instructions to run file

To execute this project on MAC,  
Create a local virtual environment
python3 -m venv venv

Activate this virtual environment
source venv/bin/activate

Install all the packages in requirements.txt (I've updated this)
pip3 install -r requirements.txt

########################################################
########################################################
# To create a local database, execute the following commands:

$flask db init
$flask db migrate -m "users table"
$flask db upgrade

# If you delete the migrations and instance folder, follow the local
database creation steps above to create database again.

#######
Personal Touch

Used an API from unsplash.com to have a dynamically changing nature 
background embedded into CSS.

# Assignment
In this project, you will build on a website using Python with Flask, which organizes online groups that host in-person events for people with similar interests. Users will be able to sign in your site, create a group along with events under the group, as well as check and join existing groups and events. Once a group is selected, users will be able to see all the relative events with date, time, title, online/face-to-face, and the number of attendees. Users can further click to attend an event. (similar to Meetup)

Essential Requirements
Write a Meetup web app using Flask and Python. The appearance and design of the pages are entirely up to you. However, your website has to meet the following requirements:

User Authentication: When a user visits your web application for the first time, they should be able to sign up with a unique email and password. 
User Profile: Once a user logged in, they should be able to see their profiles listed with name, location, joined date, and an optional bio. 
Group List: Users should be able to see a list of all current groups, and selecting one should allow the user to view the group. You may decide how to display the list.
Group Creation: Any authorized user should be able to create a group with a unique group name.
Event View: Once a group is selected, the user should see any events that have already been created in the group. All the events should be grouped by day and listed in ascending order of time.
Attending Events: Once in an event, users should be able to see event title, time, location, host, description, and a list of all attendees, up to a maximum of 8 attendees. However, you should provide a See all link for showing all attendees of the event.


# Description of files


app.py

#
This contains all the entity/table definitions, starting from line 43. 
Each entity represents a table with attributes, some of which are 
relationships that link the entity to other entities. Each entity is 
represented by a class.

#
Starting from line 117, is all the form definitions defined as classes
with the Flask Form package.

#
Starting from line 151, app.py contains all the routings for each URL.
Each route leads to an html page. Every page that is shown after 
a user is logged in is designated with @login_required

#
From line 201, is all the routings after login is required


Templates

#layout.html
This is the main template/html page, and also serves as the home page
where the URL / routes to. All other html pages extend this (besides
the ones that start with _)

#_pages
These pages are used with the Jinja include function to show embedded
lists in other html pages

#user_home.html
This extends layout.html, and is the first landing page after a user logs 
in. It shows the user's name and groups. The nav bar changes and reflects
all the pages that are available after user is logged in

#profile.html, viewGroup.html, groups.html, event.html, attending.html, creatEvent.html, createGroup.html
Self explanatory pages that user can navigate through after they are logged in.

#first.html
This is a dummy page 

######

site.css
#This has all the styling elements, and is imported in all the html pages

![Screen Shot 2023-01-27 at 2 00 40 AM](https://user-images.githubusercontent.com/70988841/215037306-8346aa9a-6cb6-450d-8df5-7af3f408c22b.png)
![Screen Shot 2023-01-27 at 1 59 32 AM](https://user-images.githubusercontent.com/70988841/215037418-d9d1ca2f-e774-49f1-847b-478cde8c98c4.png)
![Screen Shot 2023-01-27 at 2 00 10 AM](https://user-images.githubusercontent.com/70988841/215037477-0e93eb04-a8f5-4259-8319-987576c777d8.png)
![Screen Shot 2023-01-27 at 2 00 18 AM](https://user-images.githubusercontent.com/70988841/215037488-c58e3c7a-8548-4a86-aa18-3821d294889c.png)
![Screen Shot 2023-01-27 at 2 00 28 AM](https://user-images.githubusercontent.com/70988841/215037510-9b948541-dbcf-45bd-8ea5-6985999d3db1.png)
![Screen Shot 2023-01-27 at 2 00 47 AM](https://user-images.githubusercontent.com/70988841/215037524-42f74579-86f3-40cd-8390-720ef9283025.png)
![Screen Shot 2023-01-27 at 2 06 03 AM](https://user-images.githubusercontent.com/70988841/215037792-894d224d-80c8-4e90-8f71-640b083daf0a.png)
![Screen Shot 2023-01-27 at 2 06 10 AM](https://user-images.githubusercontent.com/70988841/215037806-3a43596e-e9e6-43c5-a3ad-948eb1318592.png)
![Uploading Screen Shot 2023-01-27 at 2.06.19 AM.png…]()
