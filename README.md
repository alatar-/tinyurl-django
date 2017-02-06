# TinyUrl django site

## Pre

- Python 3.5
- `requirements.txt`

## Dev setup

    # set DJANGO_SETTINGS_MODULE to 'tinyurl.settings.dev'
    python manage.py migrate
    python manage.py create_fake_users 100
    pytest
