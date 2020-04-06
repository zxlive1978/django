from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<pk>/remove/', views.post_remove, name='post_remove'),
    path('<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

]
