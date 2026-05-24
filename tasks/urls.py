from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('register/', views.register_user, name='register'),

    path('login/', views.login_user, name='login'),

    path('logout/', views.logout_user, name='logout'),

    path('delete/<int:pk>/', views.delete_task, name='delete'),

    path('complete/<int:pk>/', views.complete_task, name='complete'),

    path('update/<int:pk>/', views.update_task, name='update'),

]