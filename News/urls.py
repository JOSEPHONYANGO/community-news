from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from News import views

urlpatterns=[
    path('',views.home, name='index'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html')),
    path('create_profile',views.create_profile, name='create_profile'),   
    path('profile/',views.profile,name = 'profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('create_hood',views.create_hood, name= 'create_hood'),
    path('hood/', views.hoods, name = 'hood'),
    path('<str:name>/hood',views.single_hood,name='single_hood'),
    path('join_hood/<name>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
    path('create_post',views.create_post, name= 'create_post'),
    path('create_business',views.create_business, name= 'create_business'),
    path('businesses',views.businesses, name= 'businesses'),
    path("search_business/", views.search_business, name="search_business"),

]
