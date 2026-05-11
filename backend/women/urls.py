from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services, name='services'),
    path('account/', views.account, name='account'),
    path('service/<int:service_id>/', views.show_service, name='service'),
    path('about/', views.about, name='about'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),
    path('addpage/', views.addpage, name='addpage'),
    path('contacts/', views.contacts, name='contacts'),
    path('<slug:post_slug>/', views.show_post, name='post'),
]
