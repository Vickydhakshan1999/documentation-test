from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import  DynamicSearchView, create_group, create_user_details, create_user_with_token, delete_user_with_token, export_users_to_excel, get_all_users_with_groups, list_groups, login, retrieve_group, update_group, delete_group
from .views import PlatformUser, PlatformUserCustomField
from . import views

router = DefaultRouter()
router.register(r"custom-fields/platform/users",PlatformUserCustomField,basename="platform.user.custom_fields")
router.register(r"platform/users", PlatformUser, basename="platform.user")


urlpatterns = [
    # path('auth/login', "")
    path('groups/', list_groups, name='list_groups'),
    path('groups/create/', create_group, name='create_group'),
    path('groups/<int:group_id>/', retrieve_group, name='retrieve_group'),
    path('groups/<int:group_id>/update/', update_group, name='update_group'),
    path('groups/<int:group_id>/delete/', delete_group, name='delete_group'),

    path('permissions/create/', views.create_permission, name='create_permission'),
    path('permissions/', views.list_permissions, name='list_permissions'),
    path('permissions/<int:permission_id>/', views.retrieve_permission, name='retrieve_permission'),
    path('permissions/update/<int:permission_id>/', views.update_permission, name='update_permission'),
    path('permissions/delete/<int:permission_id>/', views.delete_permission, name='delete_permission'),

    path('permissions/assign/', views.assign_permission_to_group, name='assign_permission_to_group'),

    path('users/assign_group/', views.assign_user_to_group, name='assign_user_to_group'),

    path('login/', login, name='login'),

    path('create-user/', create_user_with_token, name='create_user_with_token'),

    path('delete-user/<int:user_id>/', delete_user_with_token, name='delete_user_with_token'),


    # URL for the View User API
    path('view-user/<int:user_id>/', views.view_user_with_token, name='view_user'),

    # URL for the Edit User API
    path('edit-user/<int:user_id>/', views.edit_user_with_token, name='edit_user'),
    
    path("user-details/create/", create_user_details, name="create_user_details"),

    path('export_users/', export_users_to_excel, name='export_users_to_excel'),
    
    path('all-users-with-groups/', get_all_users_with_groups, name='get_all_users_with_groups'),

    path('search/', DynamicSearchView.as_view(), name='dynamic-search'),
]

urlpatterns += router.urls
