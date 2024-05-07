from django.contrib import admin
from django.urls import path, re_path

from spaceTourApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/menu_items/', views.menu_items),
    re_path(r'^api/advantages/', views.advantages),
]
