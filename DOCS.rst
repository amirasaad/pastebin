Pastebin Docs
=============
Docs are available in Sphinx just run

.. code-block:: bash

    $ cd docs
    $ make html

Quick Start
-----------
To bootstrap this app locally cd to the top level for repo and run:


.. code-block:: bash

    $ python3 -m vevn venv
    $ source venv/bin/activate
    $ pip install -r requirements/local.txt
    $ ./manage migrate
    $ ./manage collectstatics
    $ ./manage runserver

You may need to add '.env' file at the top level of the repo i.e.:

.. code-block::

    DATABASE_URL='psql://pastebin_user:password@localhost:5432/pastebin'
    DJANGO_DEBUG=True
    REDIS_URL='redis://localhost:6379'
    DJANGO_READ_DOT_ENV_FILE=True
    DJANGO_SETTINGS_MODULE='config.settings.local'
    CELERY_BROKER_URL='redis://localhost:6379'
    USE_DOCKER=True


Helper scripts to export statistics:

After bootstrapping the app by migrate & runserver command access those urls via a web browser:


localhost:8000/export/csv/

localhost:8000/export/xls/
