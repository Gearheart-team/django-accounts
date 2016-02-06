# Izeni Django Accounts

## Quickstart

Add the app to `INSTALLED_APPS` after the Django admin and auth, and after rest_framework if you're using it:

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'rest_framework',
    'izeni.django.accounts',
    ...
)
```

## Configuration

The following settings are available (the defaults are also shown below):

```python
IZENI = {
    'ACCOUNTS': {
        'DO_NOT_CLEANUP_ADMIN': False,
    }
}
```