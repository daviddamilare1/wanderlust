from django.urls import path
from members import views









urlpatterns = [
    path('members/<str:pk>', views.profile, name='profile'),
    path('register/', views.Registration.as_view(), name= 'register'),
    path ('account/logout', views.logout_view, name = 'logout_view'),
    path('user_account', views.user_account, name = 'user_account'),
    path('delete_account', views.delete_useraccount, name= 'delete_account'),
    path('create_profile', views.create_profile, name= 'create_profile'),
    path('update_profile', views.update_userprofile, name='update_profile'),
   


   
     
]
