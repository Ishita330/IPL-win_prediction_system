import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your_secret_key_here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to False in production

# Hosts allowed to connect to this Django app in production
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'your-domain.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions', 
    'corsheaders',
    'rest_framework',
    'prediction',  # Your app here
]

ROOT_URLCONF = 'urls'


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Static files location for production (typically served by a web server like Nginx)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Database configuration (default SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


# Template settings (optional, if you use HTML templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# CSRF (for APIs you can disable if necessary)
CSRF_COOKIE_SECURE = False  # Set to True for production

# REST Framework settings to force JSON responses
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

# Email settings (if you plan on sending emails in production)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.your-email-provider.com'  # Example
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'

# Security settings for production (add these for hardening your app)
SECURE_SSL_REDIRECT = False  # Disable for local development, set to True in production
CSRF_COOKIE_SECURE = False  # Disable for development, set to True in production
SESSION_COOKIE_SECURE = False  # Disable for development, set to True in production
X_FRAME_OPTIONS = 'DENY'  # Protect against clickjacking
