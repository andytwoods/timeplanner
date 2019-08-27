timeplanner
===========

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


Development
-----------



Installing locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PyCharm has been used to create the project. The majority of the below steps can be sped through quickly via that IDE.

1. Clone the github repo (into a new timeplanner directory)::

    git clone https://github.com/andytwoods/timeplanner

2. Create a virtual environment (you need python >3.6 installed, and you may need to install some additional packages https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)::

    cd timeplanner
    py -m venv VENV

3. Activate your virtual environment::

    cd VENV
    cd scripts
    activate
    cd..
    cd..

4. Install all the required packages. Updating pip before::

    python -m pip install --upgrade pip
    pip install -r requirements/local.txt

5. Set up local postgres DB on your system, via https://www.postgresql.org/download/. I use pgAdmin to easily manage my postgres DBs (see https://www.pgadmin.org/).

6. Set up a postgres db. You will want to update DB settings in config/settings/local.py if you use db settings other than those below::

        'NAME': 'timeplanner',
        'USER': 'postgres',
        'PASSWORD': 'drizzt1',
        'HOST': '127.0.0.1',
        'PORT': '5433'

7. We need to create the project database tables. Within the project directory (the same directory containing manage.py), run the following::

    python manage.py migrate


Running locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

7. Within the timeplanner directory, the same directory holding the file manage.py, let's start up a local dev server::

    python manage.py runserver

8. If everything has installed correctly, navigating to http://127.0.0.1:8000/tasks/ in your browser will take you to the tasks page.

