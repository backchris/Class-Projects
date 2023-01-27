# This is my final project for 
# ITSS 4312.501 - Mobile Web Application Development - F22

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


#######
Description of files


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


