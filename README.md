# Django project structure
A basic template to start a new django project 'from scratch'. 

## Pre-requisites
To use this template you will need to have a running python installation and the `django-admin` command available (usually the case, once you installed django).
To further use the invoke command mentioned below, you will need to have the invoke package available (`pip install invoke`, you may find further details on invoke [here](http://www.pyinvoke.org)).

## Usage
To use this template, run the following command from your terminal:
```
$ django-admin startproject --template=https://github.com/firstdayofjune/django_template/archive/master.zip --name .env <project_name> optional/path/to/a/directory
```

The `--name` parameter is needed to also parse the _project_name/settings/.env_-file using the django template engine.
`<project_name>` is the name of your django project (e.g. _polls_) and the last parameter is a path to the directory where to create the app in (so the path to the parent directory which will hold the `manage.py`-file). If you omit this parameter, the project will be created in a folder also called <project_name> located at your current working directory.

For further details refer to the related chapter in the [django docs](https://docs.djangoproject.com/en/2.0/ref/django-admin/#startproject).

## Setup
After the project was created, cd into the directory and run:

```
$ invoke init
```

This will create a virtual environment, install the necessary python requirements, apply the initial migrations and also initialize an empty git repository. The virtual environment and the python requirements will be handled using pipenv (and a pipfile). For more information on pipenv check the [pipenv github page](https://github.com/pypa/pipenv). _Note: If you prefer managing your requirements yourself you may checkout version 0.1 which was using pip-tools for the requirement-handling._