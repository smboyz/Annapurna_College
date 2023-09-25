"""
URL configuration for COLLAGE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from annapurna import views

urlpatterns = [
    path("", views.base, name="home"),
    path("about/", views.about, name="about"),
    path("plus2Program/", views.plus2Program, name="plus2Program"),
    path("bachelor/", views.bachelor, name="bachelor"),
    path("photogallery/", views.photogallery, name="photogallery"),
    # path("photogallery1/", views.photogallery1, name="photogallery1"),
    # path("photogallery1/<int:id>/", views.photogallery1, name="photogallery1"),
    path("videoGallery/", views.videoGallery, name="videoGallery"),
    path("admission/", views.admission, name="admission"),
    path("newsevents/", views.newsevents, name="newsevents"),
    # path("events/", views.events, name="events"),
    path("event/<int:id>/", views.event, name="event"),
    path("contact/", views.contact, name="contact"),
    path("why/", views.why, name="why"),
    path("menu/<str:name>/",views.redirect_to_url , name="menu"),
    path("submenu/<str:name>/", views.redirect_to_url, name="submenu"),
]
