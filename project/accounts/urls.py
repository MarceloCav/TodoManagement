from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, PasswordChangeView, CustomLogoutView, profile_view

app_name = "accounts"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(next_page='todo:task_list'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_changed/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_changed.html'), name='password_changed'),
    path('profile/', profile_view, name='profile'),
]
