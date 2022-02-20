from django.urls import path
from members import views
from django.contrib.auth import views as auth_views

app_name = 'members'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit-profil/', views.UserEditProfileView.as_view(), name='edit-profil'),
    path('password/', views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='change-password'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success/', views.password_success, name='password_success'),
]