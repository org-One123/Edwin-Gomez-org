#!/usr/bin/env python
import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line

def main():
    if not settings.configured:
        settings.configure(
            DEBUG=True,
            SECRET_KEY='clave-secreta-para-pruebas-ci',
            ROOT_URLCONF='mi_app.urls',
            APPEND_SLASH=True,
            STATIC_URL='/static/',  # <-- Definición requerida para staticfiles
            INSTALLED_APPS=[
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'mi_app',
            ],
            TEMPLATES=[
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': [],
                    'APP_DIRS': True,
                    'OPTIONS': {
                        'context_processors': [
                            'django.template.context_processors.request',
                            'django.contrib.auth.context_processors.auth',
                            'django.contrib.messages.context_processors.messages',
                        ],
                    },
                },
            ],
            MIDDLEWARE=[
                'django.middleware.security.SecurityMiddleware',
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.common.CommonMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
            ],
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.sqlite3'),
                }
            }
        )
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()