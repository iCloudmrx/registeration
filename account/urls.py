from django.urls import path, include
from .views import dashboard, register, edit
from django.contrib.auth import views as auth_views


urlpatterns = [
    # first step
    # path('login/', user_login, name='login'),
    #     path('login/', auth_views.LoginView.as_view(), name='login'),



    #       #second step
    #     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #     path('', dashboard, name='dashboard'),


    #     # chance password urls
    #     path('password-chance/', auth_views.PasswordChangeView.as_view(),
    #          name='password_chance'),
    #     path('password-chance/done/', auth_views.PasswordResetDoneView.as_view(),
    #          name='password_chance_done'),

    #     # rest password urls
    #     path('oassword-reset/', auth_views.PasswordResetView.as_view(),
    #          name='password_reset'),
    #     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
    #          name='password_reset_done'),
    #     path('password-reset/<uidb64>/<token>/',
    #          auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #     path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(),
    #          name='password_reset_complete'),





    path('', dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
]
