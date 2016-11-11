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
  # `CREATE ROLE your_snippets_user WITH LOGIN ENCRYPTED PASSWORD '<a good password goes here>' CREATEDB;`
  * `GRANT ALL PRIVILEGES ON DATABASE your_snippets TO your_snippets_user;`
  * `\q`
  * `exit`
* Update the DATABASE CONFIGURATION section of your `settings/common.py` file
  * ie: `'default': env.db('DATABASE_URL', default='postgres://your_snippets_user:<your good password>@localhost:5432/your_snippets')`
