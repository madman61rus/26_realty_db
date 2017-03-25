# Real Estate Site

Real estate site project

## Install necessary packages

This site need special add-ons of Flask. To install them, from the site
directory run the following command:

    $ pip install -r requirements.txt

## Create database and apply migrations

This site work with a database. After you install site and necessary packages,
you need to create a database an apply migrations to it.

But, before you create the database, you need to setup environment variable
FLASK_APP. Specify in it a path to file server.py :

        export FLASK_APP="./server.py"

Next, you need run these commands:

    # flask db init
    # flask db migrate
    # flask db upgrade


## Load data to th database

Loading of ads into the database is made from a file. To load data, you need to
create a text file that contains data in the JSON format.

Then, using the load_data.py utility, you can do it. For this, you must
run the command :

    python load_data.py -f data.json

where data.json is file with the data

## Running the site

For run the site, you need to run command :

    python server.py

from the directory of site


# Project Goals

The code is written for educational purposes. Training course for web-developers - DEVMAN.org
