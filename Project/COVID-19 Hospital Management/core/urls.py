"""Cấu hình core URL 

Danh sách 'urlpatterns'  định tuyến URLs đến views. Tìm hiểu thêm tìm ở đây:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Ví dụ:
Chức năng của views
    1. Thêm 1 cái import:  from my_app import views
    2. Thêm URL đến urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Thêm 1 cái import:  from other_app.views import Home
    2. Thêm URL đến urlpatterns:  path('', Home.as_view(), name='home')
Bao gồm các URLconf
    1. Import the include() function: from django.urls import include, path
    2. Thêm URL đến urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
