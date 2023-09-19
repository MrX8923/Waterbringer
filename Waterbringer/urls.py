from django.contrib import admin
from django.urls import path
from order.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('order/', water_order, name='order')
]
