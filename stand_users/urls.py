from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('standusers', views.list_standusers, name='list-standusers'),
    path('standusers/new', views.create_standuser, name='new-standuser'),
    path('standusers/edit/<int:id>', views.update_standuser, name='edit-standuser'),
    path('standusers/delete/<int:id>', views.delete_standuser, name='delete-standuser'),
    path('stands', views.list_stands, name='list-stands'),
    path('stands/new', views.create_stand, name='new-stand'),
    path('stands/edit/<int:id>', views.update_stand, name='edit-stand'),
    path('stands/delete/<int:id>', views.delete_stand, name='delete-stand'),
]