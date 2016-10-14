# {{cookiecutter.project_name}}
A Django DRF backend.

## Startup
Modify your models.py file in your app. Then navigate to where manage.py and script.py are located and run:
```console
$ python script.py
```
The script will install all requirements and automatically apply migrations.

That's it! You now have automatically-templated views, serializers, urls, and admin files based on your models.
To check it all out, run the server. Don't forget to activate your virtualenv! You may also want to createsuperuser so that you can log in to the admin interface.
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
