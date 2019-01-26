# ContactBox_Warsztat_3_2
Simple contact box for craeting and managing your contacts.

## Prerequisites
Check if there is Postgres installed on your machine:
```
$ psql --version
```
If don't, install it:
```
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get -y install postgresql-10
```
If above commands didn't succeed, it means that your distro's repos don't have Postgres included. You need to add Postgres' repo to the list of used repos (follow this steps: https://wiki.postgresql.org/wiki/Apt) and run above commands once again.

Log in as user named "postgres" and create new database called "moviebase":
```
$ sudo -u postgres -i
$ createdb moviebase
```

Access any database (eg. just created "moviebase") and set password "coderslab" for user named "postgres":
```
$ psql moviebase
# \password postgres
```

Leave psql and return to your regular user account:
```
# \q
$ exit
```

## Setting up project
Navigate to directory you want project to be placed, and create local copy of repo on your machine using git:
```
$ cd path/to/directory/you/want/to/place/project/in
$ git clone https://github.com/AndrzejSzeszko/MovieBase_REST_API.git
```
or download and unzip compressed version (button "clone or download" -> "download zip" on project's main page).

Navigate to directory that contains "requirements.txt" file:
```
$ cd path/to/directory/that/contains/metioned/file
```
Install required packages:
```
$ pip install -r requirements.txt
```

Navigate to directory that contains "manage.py" file:
```
$ cd path/to/directory/that/contains/metioned/file
```
Populate database with project's tables:
```
$ python manage.py makemigrations
$ python manage.py migrate
```
Create superuser:
```
$ python manage.py createsuperuser
```
Run server locally:
```
$ python manage.py runserver
```
Project is ready to use. Visit http://127.0.0.1:8000/ page.

## To do:
- access control (logging in)
- password resetting via email
- add some Bootstrap
- pagination where needed
