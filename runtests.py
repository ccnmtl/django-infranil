""" run tests for infranil

$ virtualenv ve
$ ./ve/bin/pip install -r test_reqs.txt
$ ./ve/bin/python runtests.py
"""

import django
from django.conf import settings
from django.core.management import call_command


def main():
    # Dynamically configure the Django settings with the minimum necessary to
    # get Django running tests
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'infranil',
        ),
        TEST_RUNNER='django.test.runner.DiscoverRunner',

        ROOT_URLCONF='infranil.tests.urls',

        PROJECT_APPS=[
            'infranil',
        ],
        # Django replaces this, but it still wants it. *shrugs*
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
                'HOST': '',
                'PORT': '',
                'USER': '',
                'PASSWORD': '',
            }
        },
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True,
            },
        ]
    )

    django.setup()
    # Fire off the tests
    call_command('test')


if __name__ == '__main__':
    main()
