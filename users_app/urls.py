from django.urls import path
from users_app import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('groups/', views.groups, name='groups'),
    path('add-user/', views.add_user, name='add user'),
    path('add-group/', views.add_group, name='add group'),
    path('edit-user/<int:user_id>', views.edit_user, name='edit user'),
    path('edit-group/<int:group_id>', views.edit_group, name='edit group'),
    path('users/<int:user_id>/delete-user', views.delete_user, name='delete user' ),
    path('groups/<int:group_id>/delete-group', views.delete_group, name='delete group' ),
    # Rest API for users
    path('api/users/', views.UsersList.as_view()),
    path('api/users/<int:pk>/', views.UserDetail.as_view()),
    # Rest API for groups
    path('api/groups/', views.GroupsList.as_view()),
    path('api/groups/<int:pk>/', views.GroupDetail.as_view()),
]