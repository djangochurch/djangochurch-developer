Heroku
======

Before deploying on Heroku, we recommend that you read the `getting started
with Python`_ and `getting started with Django`_ documentation on the `Heroku
dev center`_ documentation site.

.. _getting started with Python: https://devcenter.heroku.com/articles/getting-started-with-python
.. _getting started with Django: https://devcenter.heroku.com/articles/getting-started-with-django
.. _Heroku dev center: https://devcenter.heroku.com/

These instructions are a modified version of the `getting started with Django`_
documentation from Heroku, adjusted to make it easier to get going with the
default applications provided by Django Church.

.. _getting started with Django: https://devcenter.heroku.com/articles/getting-started-with-django


Prerequisites
-------------

* The Heroku toolbelt, as described in `Getting Started with Python`_.
* Installed Python_ and Virtualenv_ in a unix-style environment. See `this
  guide`_ for guidance.
* An installed version of Postgres_ (if you want to test locally).
* A `Heroku user account`_.

.. _Getting Started with Python: https://devcenter.heroku.com/articles/getting-started-with-python
.. _this guide: http://install.python-guide.org/
.. _Python: https://www.python.org/
.. _Virtualenv: https://virtualenv.pypa.io/
.. _Postgres: http://www.postgresql.org/
.. _Heroku user account: https://signup.heroku.com/signup/dc


Start a Django app inside a Virtualenv
--------------------------------------

First, we'll create an empty top-level directory for our project:

.. code-block:: console

    $ mkdir mychurch && cd mychurch

.. note::

    Make sure you're using the latest virtualenv release. If you're using an
    older version, you may need to add the ``--no-site-packages`` flag.

Next, we'll create a Python Virtualenv_ (v1.0+):

.. _Virtualenv: https://virtualenv.pypa.io/

.. code-block:: console

    $ virtualenv venv
    New python executable in venv/bin/python
    Installing setuptools, pip...done.

To use the new virtualenv, we need to activate it. (You must source the
virtualenv environment for each terminal session where you wish to run your
app.):

.. code-block:: console

    $ source venv/bin/activate

Next, install our application's dependencies with pip_.

.. _pip: https://pip.pypa.io/

.. note::

    As of June 2014, Django 1.7 is currently in beta, so we have to install the
    beta version from the djangoproject.com site directly.

From your virtualenv:

.. code-block:: console

    $ pip install https://www.djangoproject.com/download/1.7.b4/tarball/
    Downloading/unpacking https://www.djangoproject.com/download/1.7.b4/tarball/
     ...
    Successfully installed Django
    Cleaning up...

Now that Django is installed, we can start the project using the Django Church
template:

.. note::

    Don't forget the ``.`` in the middle. This tells Django to extract into the
    current directory, instead of putting it in a new subdirectory.

.. code-block:: console

    $ django-admin.py startproject mychurch . --template=https://github.com/djangochurch/djangochurch-heroku/archive/master.zip --name=Procfile

Now we can install all the other required packages:

.. code-block:: console

    $ pip install -r requirements.txt
      ...
    Successfully installed pytz psycopg2 Pillow dj-database-url gunicorn pystache dj-static-dev static3 django-storages boto blanc-basic-assets easy-thumbnails blanc-basic-news django-mptt django-mptt-admin six blanc-basic-pages icalendar python-dateutil blanc-basic-events
    Cleaning up...


Adding a theme
--------------

We'll be using the House_ theme for this example. If you want a different theme
then please read more about :doc:`themes </themes>`.

.. _House: https://github.com/djangochurch/djangochurch-theme-house

Run the following commands:

.. code-block:: console

    $ curl -sL https://github.com/djangochurch/djangochurch-theme-house/tarball/master | tar zxv
     ...
    x djangochurch-djangochurch-theme-house-1852fc3/templates/pages/
    x djangochurch-djangochurch-theme-house-1852fc3/templates/pages/default.html
    $ mv djangochurch-djangochurch-theme-house-* theme


Store your app in Git
---------------------

Now that we've written and tested our application, we need to store the project
in a Git_ repository.

.. _Git: http://git-scm.org/

Next, we'll create a new git repository and save our changes.

.. code-block:: console

    $ git init
    Initialized empty Git repository in /Users/kreitz/hellodjango/.git/
    $ git add .
    $ git commit -m "my django app"
    [master (root-commit) 2943412] my django app
     12 files changed, 676 insertions(+)
     create mode 100644 .gitignore
     create mode 100644 Procfile
     create mode 100644 manage.py
     create mode 100644 mychurch/__init__.py
     create mode 100644 mychurch/settings.py
     create mode 100644 mychurch/templates/base.html
     create mode 100644 mychurch/urls.py
     create mode 100644 mychurch/wsgi.py
     create mode 100644 requirements.txt


Deploy to Heroku
----------------

The next step is to push the application's repository to Heroku. First, we have
to get a place to push to from Heroku. We can do this with the ``heroku
create`` command:

.. code-block:: console

    $ heroku create
    Creating simple-spring-9999... done, stack is cedar
    http://simple-spring-9999.herokuapp.com/ | git@heroku.com:simple-spring-9999.git
    Git remote heroku added

This automatically added the Heroku remote for our app
``(git@heroku.com:simple-spring-9999.git)`` to our repository. Now we can do a
simple ``git push`` to deploy our application:

.. code-block:: console

    $ git push heroku master
    Counting objects: 11, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (9/9), done.
    Writing objects: 100% (11/11), 4.01 KiB, done.
    Total 11 (delta 0), reused 0 (delta 0)
    -----> Python app detected
    -----> Preparing Python runtime (python-2.7.7)
    -----> Installing Setuptools (3.6)
    -----> Installing Pip (1.5.6)
    -----> Installing dependencies using Pip (1.5.6)
           ...
    -----> Collecting static files
           0 static files copied.

    -----> Discovering process types
           Procfile declares types -> web

    -----> Compiled slug size is 29.5MB
    -----> Launching... done, v6
           http://simple-spring-9999.herokuapp.com deployed to Heroku

    To git@heroku.com:simple-spring-9999.git
    * [new branch]      master -> master


Syncing the database
--------------------

The ``heroku run`` command lets you run `one-off dynos`_. You can use this to
sync the Django models with the database schema:

.. _one-off dynos: https://devcenter.heroku.com/articles/one-off-dynos

.. code-block:: console

    $ heroku run python manage.py migrate
    Running `python manage.py migrate` attached to terminal... up, run.1
    Operations to perform:
      Synchronize unmigrated apps: assets, admin, mptt, pages, sessions, news, events, contenttypes, auth
      Apply all migrations: easy_thumbnails
    Synchronizing apps without migrations:
      Creating tables...
        Creating table django_admin_log
        Creating table auth_permission
        Creating table auth_group_permissions
        Creating table auth_group
        Creating table auth_user_groups
        Creating table auth_user_user_permissions
        Creating table auth_user
        Creating table django_content_type
        Creating table django_session
        Creating table assets_imagecategory
        Creating table assets_image
        Creating table assets_filecategory
        Creating table assets_file
        Creating table news_category
        Creating table news_post
        Creating table pages_page
        Creating table events_specialevent
        Creating table events_recurringevent
      Installing custom SQL...
      Installing indexes...
    Running migrations:
      Applying easy_thumbnails.0001_initial... OK
      Applying easy_thumbnails.0002_thumbnaildimensions... OK

    You have installed Django's auth system, and don't have any superusers defined.
    Would you like to create one now? (yes/no): yes
    Username (leave blank to use 'u12733'): admin
    Email address: admin@example.org
    Password:
    Password (again):
    Superuser created successfully.


Heroku settings
---------------

As Heroku only offers an ephemeral filesystem, we need to configure a few
additional settings to keep media files. We'll be adding a few `environment
variables`_ on Heroku.

.. _environment variables: https://devcenter.heroku.com/articles/config-vars

Follow the instructions on the `Heroku S3 docs`_, and configure the environment
variables:

.. _Heroku S3 docs: https://devcenter.heroku.com/articles/s3

* ``AWS_ACCESS_KEY_ID``
* ``AWS_SECRET_ACCESS_KEY``
* ``S3_BUCKET_NAME``

As a quick reminder, the following command will get your environment variables
setup on Heroku:

.. code-block:: console

    heroku config:set AWS_ACCESS_KEY_ID=xxx AWS_SECRET_ACCESS_KEY=yyy S3_BUCKET_NAME=zzz


Visit your application
----------------------

You've deployed your code to Heroku, so we can now visit the app in our browser
with ``heroku open``.

.. code-block:: console

    $ heroku open
    Opening simple-spring-9999.herokuapp.com... done

You should see the satisfying "It worked!" Django welcome page.
