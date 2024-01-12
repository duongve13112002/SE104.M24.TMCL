"""
Cấu hình ASGI cho core project.

 ASGI có thể gọi là một biến module-level có tên là 'ứng dụng'

Tìm hiểu thông tin về cái file này thì xem đường link sau
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()
