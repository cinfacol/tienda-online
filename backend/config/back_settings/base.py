import os
from datetime import timedelta
from pathlib import Path

# import environ

# env = environ.Env()
# environ.Env.read_env()

# ENVIRONMENT = env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# DOMAIN = os.environ.get('DOMAIN')

""" ALLOWED_HOSTS = [
    '127.0.0.1',
    '0.0.0.0',
    'localhost',
] """

# RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
# if RENDER_EXTERNAL_HOSTNAME:
#     ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

PROJECT_APPS = [
    'user.apps.UserConfig',
    'user_profile.apps.UserProfileConfig',
]

ECOMMERCE_APPS = [
    'category.apps.CategoryConfig',
    'product.apps.ProductConfig',
    'cart.apps.CartConfig',
    'shipping.apps.ShippingConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'coupons.apps.CouponsConfig',
    'wishlist.apps.WishlistConfig',
    'reviews.apps.ReviewsConfig',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'djoser',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'ckeditor',
    'ckeditor_uploader',
    'debug_toolbar',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + ECOMMERCE_APPS + THIRD_PARTY_APPS

SITE_ID = 1

CKEDITOR_CONFIGS = {'default': {'toolbar': 'full', 'autoParagraph': False}}

CKEDITOR_UPLOAD_PATH = '/media/'

BASE_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOCAL_MIDDLEWARE = []

THIRD_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

MIDDLEWARE = BASE_MIDDLEWARE + LOCAL_MIDDLEWARE + THIRD_MIDDLEWARE

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': env.db('DATABASE_URL'),
# }
# DATABASES['default']['ATOMIC_REQUESTS'] = True

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True


CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:1337',
    'http://127.0.0.1:80',
    'http://localhost:1337',
    'http://localhost:80',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:1337',
    'http://localhost:1337',
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/staticfiles/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
MEDIA_URL = '/mediafiles/'

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'build/static')]
STATICFILES_DIRS = []

INTERNAL_IPS = [
    '127.0.0.1',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 12,
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESFH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SET_USERNAME_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': [
        'http://localhost:8000/google',
        'http://localhost:8000/facebook',
    ],
    'SERIALIZERS': {
        'user_create': 'user.serializers.UserCreateSerializer',
        'user': 'user.serializers.UserCreateSerializer',
        'current_user': 'user.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
}

# BT_ENVIRONMENT = os.environ.get('BT_ENVIRONMENT')
# BT_MERCHANT_ID = os.environ.get('BT_MERCHANT_ID')
# BT_PUBLIC_KEY = os.environ.get('BT_PUBLIC_KEY')
# BT_PRIVATE_KEY = os.environ.get('BT_PRIVATE_KEY')

AUTH_USER_MODEL = 'user.UserAccount'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# si está en producción
""" if not DEBUG:
    DEFAULT_FROM_EMAIL = 'Cinfacol - Academia de Software <cinfacol@gmail.com>'
    EMAIL_BACKEND = env('EMAIL_BACKEND')
    EMAIL_HOST = env('EMAIL_HOST')
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = env('EMAIL_PORT')
    EMAIL_USE_TLS = env('EMAIL_USE_TLS') """


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
