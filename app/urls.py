from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload', views.upload, name='upload'),
    path('project/<slug>', views.single_project, name="single_project"),
    path('project/<id>/vote', views.rate_project, name="rate_project"),
    path('project/<project_id>/delete', views.delete_project, name="project_delete"),
    path('project/<project_id>/update', views.update_project, name="update_project"),
    path('profile', views.profile, name="profile"),
    path('update_profile', views.update_profile, name="update_profile"),
    path('update_avatar', views.update_avatar, name="update_avatar"),
    path('search', views.search, name="search"),
    path('api/projects', views.ProjectsList.as_view()),
    path('api/users', views.ProfilesList.as_view())
]
