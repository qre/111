from django.urls import path

from . import views

urlpatterns = [
path('', views.main, name="main"),
path('getfile', views.get_file),
path('refresh.php', views.refresh)
]