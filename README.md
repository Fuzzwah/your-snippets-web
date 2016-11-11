# Your Snippets

A place to collect snippets and images from the web.

[![Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

## Requirements

* Linux server
* Nginx
* PostgreSQL 9.5
* Python 3

## Installation

* Clone this repo: `git clone https://github.com/Fuzzwah/your-snippets-web.git`
* Change into the project's directory: `cd your-snippets-web`
* Create a virtualenv for the project: `python3 -m virtualenv -p python3 .env`
* Activate the virtualenv: `. .env/bin/activate`
* Grab the requirments via pip: `pip install -r requirements/local.txt`
* Setup your database:
  * `sudo su - postgres`
  * `psql`
  * `CREATE DATABASE your_snippets;`
  * `CREATE ROLE your_snippets_user WITH LOGIN ENCRYPTED PASSWORD '<a good password goes here>' CREATEDB;`
  * `GRANT ALL PRIVILEGES ON DATABASE your_snippets TO your_snippets_user;`
  * `\q`
  * `exit`
* Copy the example environment file into the required location: `cp env.example config/settings/.env`
* Edit this file and configure your database connection string.
  * ie: `DATABASE_URL=postgres://postgresuser:mysecretpass@localhost:5432/your_snippets
`
* Set up django database schema: `python manage.py migrate`
* Create your superuser: `python manage.py createsuperuser`
* Collect up the static files: `python manage.py collectstatic`
* Set up gunicorn and nginx: [follow this guide](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-centos-7#create-a-gunicorn-systemd-service-file) and alter details and locations as required.
* Create a gunicorn_start bash script which includes the exporting of your various config requirements, such as database details

