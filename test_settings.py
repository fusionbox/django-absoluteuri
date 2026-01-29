# We just put it here to get the checks to shut up
MIDDLEWARE = []

INSTALLED_APPS = (
    'django.contrib.sites',
    'absoluteuri',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

SITE_ID = 1

SECRET_KEY = 'test-secret-key'

ROOT_URLCONF = 'absoluteuri.tests'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]
