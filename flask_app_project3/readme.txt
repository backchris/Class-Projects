# This is flask_app_hello_v3 for 
# ITSS 4312.501 - Mobile Web Application Development - F22
# modified date: 11/1/2022 9:55 PM

########################################################
########################################################
# To execute this project on WINDOWS,  
# Create a local virtual environment
python -m venv venv

# Activate this virtual environment
.\venv\Scripts\activate

# Install all the packages in requirements.txt
pip install -r requirements.txt

########################################################
########################################################
# To execute this project on MAC,  
# Create a local virtual environment
python3 -m venv venv

# Activate this virtual environment
source venv/bin/activate

# Install all the packages in requirements.txt
pip3 install -r requirements.txt


########################################################
########################################################
# To create a local database, execute the following commands:

$flask db init
$flask db migrate -m "users table"
$flask db upgrade


$flask db init
$flask db migrate -m "Initial migration"
$flask db upgrade