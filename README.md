# awwards-app

## Author

[Dan_Njoroge](https://github.com/greatdaniels)

# Description
A web application to post websites and other web projects as well as review posted projects. You can visit the live site on `https://awwards-mc27.herokuapp.com/`

## User Story

* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.   

### Cloning
* In your terminal:
        
        $ git clone https://github.com/greatdaniels/awwards-app.git
        $ cd awwards-app

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ python manage.py makemigrations awwardsapp
        $ python3.6 manage.py migrate 

* To run the application, in your terminal:

        $ python3.6 manage.py runserver
        
## Testing the Application
* To run the tests :

        $ python3.6 manage.py test 


## Technology used

* [Python3.6](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)


## Known Bugs
* Pull requests are allowed incase you spot a bug.

## License
[MIT LICENSE](./license)