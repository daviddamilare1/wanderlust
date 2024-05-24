from django.urls import path
from . import views







urlpatterns = [
    path('', views.index, name='index'),
    path ('create', views.create_post, name= 'create'),
    path('detail/<slug:slug>/', views.blog_body, name='detail'),
    path('update/<slug:slug>/', views.update_post, name='update'),
    path('delete/<slug:slug>', views.delete_post, name= 'delete'),
    path('categorypage/<str:pk>', views.category_page, name='categorypage'),
    path('search', views.search_bar, name= 'search'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    # path('like_post', views.like_post, name='like'),
    

]