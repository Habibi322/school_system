from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # уже есть

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('school.urls')),
    path('login/', auth_views.LoginView.as_view(
        template_name='school/login.html',
        next_page='/'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/',
        http_method_names=['get', 'post']
    ), name='logout'),
]