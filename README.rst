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

Pycharm has been used to create the project. The majority of the below steps can be sped through quickly via that IDE.

1. Clone the github repo (into a new timeplanner directory)::

    $ git clone https://github.com/andytwoods/timeplanner

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

<NEED STUFF ON DB SETUP>

Running locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Within your ::

    $ git clone https://github.com/andytwoods/timeplanner



Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.




