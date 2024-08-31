from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Authentication
    path('register', views.register, name='register'),
    path('login', views.my_login, name='login'),
    path('logout', views.user_logout, name='logout'),

    # CRUD
    path('dashboard', views.dashboard, name='dashboard'),
    path('create-record', views.create_record, name='create-record'),
    path('update-record/<int:pk>', views.update_record, name='update-record'),
    path('view-record/<int:pk>', views.read_record, name='view-record'),
    path('delete-record/<int:pk>', views.delete_record, name='delete-record'),
]
