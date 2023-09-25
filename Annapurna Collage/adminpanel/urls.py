from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", admin_login, name="admin_login"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", Logoutpage, name="logout"),
    path("globalsetting/", globalsetting, name="globalsetting"),
    path("contactus/", contactus, name="contactus"),
    path("delete_contact/", delete_contact, name="delete_contact"),
    path("main_navigation/<int:parent_id>/", main_navigation, name="main_navigation"),
    path("main_navigation/", main_navigation, name="main_navigation"),
    path("navigation/", navigation_list, name="navigation"),
    path("navigation/<int:parent_id>/", navigation_list, name="navigation"),
    path("update/<int:pk>/", update, name="update"),
    path("delete_nav/<int:pk>/", delete_nav, name="delete_nav"),
    # path("admission_1/", admission_1, name="admission_1"),
    path("admission_1/<int:pk>/", admission_1, name="admission_1"),
    path("admissions/", admissions, name="admissions"),
    path("delete_admi/", delete_admissions, name="delete_admi"),
    path('generate-pdf/<int:pk>/', generate_pdf, name='generate-pdf'),
    path("gallery/", gallery, name="gallery"),
    path("gallery_1/", gallery_1, name="gallery_1"),
    path("delete_gall/<int:pk>/", delete_gall, name="delete_gall"),
]
