from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path("project/<slug:slug>/", views.project_detail, name="project_detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("ajax/send-message/", views.send_message, name="send_message"),
    path("ajax/get-projects/", views.get_projects_ajax, name="get_projects_ajax"),
]
