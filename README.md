# Django Template Project for KMUHelper on Heroku

Dies ist ein Django Vorlagenprojekt, welches dabei hilft, direkt mit dem KMUHelper loszulegen.

Diese Vorlage ist für [Heroku](https://heroku.com) ausgelegt. Andere Anbieter benötigen unter Umständen andere Konfigurationen!

## Installation

Siehe [hier](https://rafaelurben.github.io/django-kmuhelper/installation).

## Deploy on Heroku

Using custom database:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/rafaelurben/djangoproject-template-kmuhelper-heroku)

Using Heroku Postgres: (ignore DB-related fields in the form)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/rafaelurben/djangoproject-template-kmuhelper-heroku&addons=[heroku-postgresql]&env[DJANGO_SUPERUSER_USERNAME]=REPLACE_WITH_YOUR_USERNAME&env[DJANGO_SUPERUSER_PASSWORD]=REPLACE_WITH_YOUR_PASSWORD&env[DJANGO_SUPERUSER_EMAIL]=REPLACE_WITH_YOUR_EMAIL)
