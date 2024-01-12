"""
Cài đặt Django cho core project.

Được tạo từ 'django-admin startproject' sử dụng Django phiên bản 3.1.3.

-Nguồn tham khảo 
+ Link xem thêm thông tin của tệp này
https://docs.djangoproject.com/en/3.1/topics/settings/

+ Link xem đầy đủ các cài đặt và giá trị của chúng
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import os.path
from pathlib import Path
from django.contrib.messages import constants as messages
# Xây dựng đường dẫn bên trong project
BASE_DIR = Path(__file__).resolve().parent.parent


# Cài đặt phát triển nhanh - dự án này ko phải là 1 sản phâm cho doanh nghiệp nên chỉ cần cài đặt phát triển nhanh 
# Xem tại link: https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# Secret_key là 1 điều quan trọng dùng để mã hóa (ko dc lộ ra nếu là sản phẩm thực tế thì sẽ ảnh hưởng đến thông tin .....)
SECRET_KEY = '6=drjci9-24*%p-ru1sbqbl0$$!b)_q&_cu5z26y7wk+wk9g!^'


DEBUG = True

ALLOWED_HOSTS = ['covid19_hopital_management.com', '127.0.0.1']


# Định nghĩa ứng dụng có những gì

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'django_filters',
    'multiselectfield',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

#Xem thêm về database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation - Phần xác thực mật khẩu
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) - Các tệp dữ liệu tĩnh cho website VD hình ảnh ,....
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/images/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
