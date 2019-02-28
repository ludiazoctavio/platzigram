
from django.contrib import admin
from django.urls import path
from platzigram import views as local_views
from posts import views as post_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', post_views.list_posts, name='feed'),
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup, name='signup'),
]
