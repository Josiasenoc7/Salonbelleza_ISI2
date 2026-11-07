

from pathlib import Path
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v%x(8&2frv3$oyn$-c8joe#7&3@3+np7q=-8o6l!z+mn*)!*pn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "usuarios",
    "servicios",
    "parametros",
    "citas",
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'salon.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'salon', 'templates')],
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

WSGI_APPLICATION = 'salon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'SalonBelleza',     
        'USER': 'postgres',              
        'PASSWORD': 'ANGELITO123.k',     
        'HOST': 'localhost',             
        'PORT': '5432',                  
    }
}

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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

JAZZMIN_SETTINGS = {
    "site_title": "Salon Belleza",
    "site_header": "Salon Belleza",
    "site_brand": "Salon Belleza Admin",
    "site_logo": None,
    "welcome_sign": "Bienvenido al Sistema del Salón",
    "copyright": "Salon Belleza",

    "topmenu_links": [
        {"name": "Inicio", "url": "admin:index"},
        {"app": "usuarios"},
        {"app": "servicios"},
        {"app": "parametros"},
        {"app": "citas"},
    ],

    "show_sidebar": True,
    "navigation_expanded": True,

    "icons": {
        "usuarios.Usuario": "fas fa-user",
        "usuarios.Rol": "fas fa-user-tag",
        "servicios.Servicio": "fas fa-scissors",
        "parametros.Parametro": "fas fa-cog",
        "citas.Cita": "fas fa-calendar",
        "citas.Cita_Empleado": "fas fa-user-clock",
        "citas.Clientes_Citas": "fas fa-users",
        "citas.Cliente_Cita_Detalle": "fas fa-list",
    },

    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",

     "custom_links": {
        "citas": [
            {
                "name": "Calendario de Citas",
                "url": "/citas/calendario/",
                "icon": "fas fa-calendar-alt",
                "permissions": ["citas.view_cita"],
            }
        ],
    },
    
}

JAZZMIN_UI_TWEAKS = {
    # Tema elegante (claro y moderno). Opciones buenas: "flatly", "cosmo", "litera", "lumen"
    "theme": "flatly",
    "dark_mode_theme": "darkly",

    # Navbar / Sidebar
    "navbar": "navbar-white navbar-light",
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,

    # Marca y acentos
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",

    # Botones más finos
    "button_classes": {
        "primary": "btn btn-primary",
        "secondary": "btn btn-outline-secondary",
        "info": "btn btn-info",
        "warning": "btn btn-warning",
        "danger": "btn btn-danger",
        "success": "btn btn-success",
    },

    # Efectos visuales
    "actions_sticky_top": True,

}


LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
