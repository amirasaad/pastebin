Pastebin
========

Share codes and notes with your friends!

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

.. image:: https://travis-ci.org/amirasaad/pastebin.svg?branch=master
    :target: https://travis-ci.org/amirasaad/pastebin
    :alt: Travis status
.. image:: https://circleci.com/gh/amirasaad/pastebin.svg?style=svg
    :target: https://circleci.com/gh/amirasaad/pastebin
    :alt: CircleCi Status

.. image:: https://app.codeship.com/projects/647c9040-de7d-0137-0848-562498d4ae94/status?branch=master
    :target: https://app.codeship.com/projects/372098 
    :alt: Codeship Status

.. image:: https://codecov.io/gh/amirasaad/pastebin/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/amirasaad/pastebin
  :alt: Codecov

.. image:: https://amirasaad.semaphoreci.com/badges/pastebin/branches/master.svg
   :target: https://amirasaad.semaphoreci.com/projects/pastebin
   :alt: Semaphore Status

:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser


Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy pastebin

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


Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd pastebin
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.




Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog



Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^
You will need to build the stack first. To do that, run:

.. code-block:: bash

    docker-compose -f production.yml build

Once this is ready, you can run it with:

.. code-block:: bash

    docker-compose -f production.yml up

To run the stack and detach the containers, run:

.. code-block:: bash

    docker-compose -f production.yml up -d

To run a migration, open up a second terminal and run:

.. code-block:: bash

    docker-compose -f production.yml run --rm django python manage.py migrate

To create a superuser, run:

.. code-block:: bash

    docker-compose -f production.yml run --rm django python manage.py createsuperuser

If you need a shell, run:

.. code-block:: bash

    docker-compose -f production.yml run --rm django python manage.py shell

To check the logs out, run:

.. code-block:: bash

    docker-compose -f production.yml logs


.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



