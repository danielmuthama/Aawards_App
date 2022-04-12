from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('search/', views.search_project, name='search'),
    path('project/<post>', views.project, name='project'),
    path('profile/<username>/', views.profile, name='profile'),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
]