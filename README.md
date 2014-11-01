cronwatch
=========

Cronwatch is a simple utility for displaying cron file contents. This could be used, for example, to iframe into a wiki document.

Install
-------

    cd <source directory>
    pip install -r requirements.txt

Run
-------

    cd <source directory>/app
    python cronwatch.py

Usage
-----

To display a systemwide crontab which is in `/etc/cron.d/<crontab>`:

    http://localhost:57655/cron/?crontab=mycrontab

To display a user crontab:

    http://localhost:57655/cron/?user=username

Running with supervisor
-----------------------

    [program:cronwatch]
    command=/usr/bin/python cronwatch.py
    environment=PYTHONPATH=.
    directory=/opt/cronwatch/app
