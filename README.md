# neighborhd
this is application that allows you to be in the loop about everything happening in your neighborhood.
# The neighborhood

The neighborhood is a web-application which helps there users to know what's going on in their neighborhood.From contact information of different handyman to meeting announcements or even alerts.A user can create an account add also have a profile with his/her information.A user can also search for businesses around his neighborhood

 #### Prerequisites

* Virtual environment
* Python3.6
* Postgres
* pip
* Django 1.11

#### Activate virtual environment

```
$ python3.6 -m venv --without-pip virtual 
$ source venv/bin/activate
``` 

 #### Installing

Install dependancies that will create an environment for the app to run

#### Create Database
```
$ psql
CREATE DATABASE the
```

 #### Run initial Migrations
```
$ python manage.py makemigrations theNeighborhood
$ python3.6 manage.py migrate
```

#### Running the app
```
$ python3.6 manage.py runserver
```

## Running the tests

```
$ python3.6 manage.py test theNeighborhood
```
## Deployment

Add additional notes about how to deploy this on a live system

## Built With 

* [Django](http://www.django.io/1.0.2/docs/) - The web framework used

## Support and contact details

Having any issues?
Email:kangabejuliette@gmail.com
contact:0787873242


## License


[MIT](https://choosealicense.com/licenses/mit/)
Copyright (c) 2019 **KANGABE JULIETTE**
