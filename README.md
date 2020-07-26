# Horus Challenge - Backend

## :page_with_curl: Summary

This project was developed as a prerequisite in the selection process for a fullstack developer vacancy. The purpose of the project is to provide an API to manage a contact list.

## :necktie: The Business Roles

- Create a small application for a user to manage a contact list.

- Contact must have name and phone number only.

- The user can add, update, view all contacts and delete.

- The deleted contact cannot be deleted from the database (soft delete).

- There can be no duplicate phone, either during registration or updating.

## :arrow_forward: Environment

You can run the application directly on your computer. Just have python 3+ installed, postgresql 9.6 and Pipenv.

## :fire: Getting Started

These instructions will get this project up and running in your machine.

### :computer: Using your computer

### :wave: Prerequisites

> [Python 3.X](https://www.python.org/downloads/)

> [Postgresql](https://www.postgresql.org/download/)

> [Pipenv](https://pypi.org/project/pipenv/)

### :rocket: Installing

- Run the command on the terminal
 ```sh
$ pip install pipenv
```

 - Clone the project:
```sh
$ git clone https://github.com/rdouglas10/horus.git 
```
  
- Access the project folder (terminal)
 ```sh
$ cd horus
$ pipenv --three
```
running pipenv --three will create a virtual environment if not already created using python3.

- Activate the project virtual environment with the following command.
```sh
$ pipenv shell
```

- Install all packages
```sh
$ pip install -r requirements.txt
```

- Create the following environment variables
```sh
$ export FLASK_ENV=development
$ export DATABASE_URL='postgresql+psycopg2://<user>:<password>@<host>/<db>'
``` 

- To execute the database settings access the project root and run:
```sh
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```

- To execute access the project root run:
```sh
$ python run.py
```

## :robot: API and Endpoints

The API has the following endpoints:

- `[POST] /api/v1/contacts/`: Endpoint to create a contact in phonebook.
- `[GET] /api/v1/contacts/`: Endpoint to obtain all contacts of the phonebook.
- `[GET] /api/v1/contacts/<int:contact_id>`: Endpoint to obtain the contact informed by parameter.
- `[DELETE] /api/v1/contacts/<int:contact_id>`: Endpoint to delete the contact of phonebook informed by parameter.
- `[PUT] /api/v1/contacts/<int:contact_id>`: Endpoint to update the contact selected of phonebook.

## :key: Input Parameters

| Field Name | Type
|-----|-----
| name | string 
| phone | string 

## :battery: Future improvements and features

 - [ ] :cold_sweat: Implement mask in the phone field.
 - [ ] Create tests cases.
 
 ## :foggy: Presentation layer
 
 > [Frontend repository](https://github.com/rdouglas10/horus-frontend)
