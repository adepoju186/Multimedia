from . import views
from django.urls import path

urlpatterns=[
    path('', views.main,name='main'),
    path('add_media/', views.add_media, name='add_media'),
    path('upload', views.upload, name='upload')
]
