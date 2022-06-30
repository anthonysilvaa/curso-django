from django.contrib import admin
from django.urls import path

from pypro.base.views import home

app_name = 'base'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home")
]
