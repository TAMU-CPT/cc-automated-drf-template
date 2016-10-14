# cc-automated-drf-template
cc_automated_drf_template uses [Cookiecutter](https://github.com/audreyr/cookiecutter) and a custom script to automatically populate a Django REST project given a models.py. Just 
provide your models.py and cc_automated_drf_template will write your views, serializers, urls, and admin files for you.

## Features
- Django REST Framework integration
- Support for multiple apps
- [JWT authentication](https://getblimp.github.io/django-rest-framework-jwt/)
- Fully populated serializers.py, views.py, urls.py, admin.py

## Installation
Install Cookiecutter:
```console
$ pip install cookiecutter
```
Give names for your directory, project, and app when prompted by Cookiecutter:
```console
$ cookiecutter https://github.com/TAMU-CPT/cc-automated-drf-template.git
dir_name [test-project]:
project_name [project]:
app_name [base_app]:
```
Modify your models.py file in your app. Then navigate to where manage.py and script.py are located and run:
```console
$ python script.py
```
The script will install all requirements and automatically apply migrations.

That's it! You now have automatically-templated views, serializers, urls, and admin files based on your models.
To check it all out, run the server. Don't forget to activate your virtualenv! You may also want to createsuperuser so that
you can log in to the admin interface.
```console
$ . venv/bin/activate
$ python manage.py createsuperuser
$ python manage.py runserver
```

#### Note on virtual environments:
If you have already set up/activated a virtual environment, make sure to use the ```--disable-venv``` flag.
Otherwise, a virtualenv will be created for you. 

## Multiple app support
Some Django projects have multiple apps in addition to the base application.
If you want to similarly generate files for these apps, you may run the script again
using the ```--app_name``` flag, like this:
```console
(venv) $ python script.py --app_name another_app --disable-venv
```
Since I am already in a venv, I also used ```--disabe-venv```.

#### Note on file changes:
If you have modified views, serializers, urls, or admin files before running the script or are
unsure of the changes made after running it, make sure to ```git add -p``` to add or ignore changes
that will be staged in the next commit.

## What's next?
If you are looking to add a front end, check out [CICADA](https://github.com/tamu-cpt/CICADA), which will 
automatically template an AngularJS frontend that will plug in to the backend you just created.

## License
This software is licensed under BSD-3-Clause
