from django.urls import path, re_path


from . import views

urlpatterns = [
    path('', views.spotifyTest, name='index'),
    path('callback/q', views.callback, name='index'),
]