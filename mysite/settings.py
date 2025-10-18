from pathlib import Path
import os

# ------------------------------
# BASE DIR
# ------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------
# SECURITY
# ------------------------------
SECRET_KEY = 'django-insecure-u_d+vtjwh7ni_g*ao7%y%6zv8vj=m#!0s(-g2!b!b0988862j4'
DEBUG = True  # Set to False in production; enable True locally so static files are served during development
ALLOWED_HOSTS = ['my-django-website-ukd0.onrender.com', '127.0.0.1', 'localhost', '10.65.81.30']

# ------------------------------
# APPLICATIONS
# ------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myprofile',  # your app
]

# ------------------------------
# MIDDLEWARE
# ------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For serving static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------------
# URLS AND TEMPLATES
# ------------------------------
ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Global templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# ------------------------------
# DATABASE
# ------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ------------------------------
# PASSWORD VALIDATION
# ------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------
# INTERNATIONALIZATION
# ------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------
# STATIC FILES
# ------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "myprofile/static")]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Collected by collectstatic
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ------------------------------
# EMAIL SETTINGS
# ------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# IMPORTANT: store real credentials in environment variables
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
CONTACT_EMAIL = EMAIL_HOST_USER

# ------------------------------
# DEFAULT PRIMARY KEY
# ------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# IMPORTANT: store real credentials in environment variables, not in source control.
# Use names like EMAIL_HOST_USER and EMAIL_HOST_PASSWORD (or GMAIL_ADDRESS / GMAIL_APP_PASSWORD).
# Example (PowerShell):
#   $env:EMAIL_HOST_USER = "youremail@gmail.com"
#   $env:EMAIL_HOST_PASSWORD = "your-16-char-app-password"
# For deployments (Render, Heroku, etc.) set the environment variables in the service's settings.
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'emmanuelmuganzielc@gmail.com')  # e.g. 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'rfcxnrngnfswmoyg')  # 16-char app password

# Use the host address as the default "from" address
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# If credentials aren't set, use the console backend for local testing to avoid
# SMTP errors and 500 responses. In production, be sure to set the env vars.
if not EMAIL_HOST_USER or not EMAIL_HOST_PASSWORD:
    # Prints will appear in the server console; useful when running locally.
    print('WARNING: EMAIL_HOST_USER or EMAIL_HOST_PASSWORD is not set. Using console email backend for local testing.')
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Basic logging: write Django errors and our app logger to a file so we can inspect
# SMTP tracebacks and other exceptions without relying only on the server console.
LOG_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname} {name} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'django.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Our app logger
        'myprofile': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

