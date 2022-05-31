from django.urls import include, path
from django.contrib.auth import views as auth_views # ANCHOR Import It

from . import views

urlpatterns = [

	# path('register/',views.registerPage, name="register"),
	# path('login/', views.loginPage, name="login"),
	# path('logout/',views.logoutUser, name="logout"),
	# path('forgotPass/',views.forgotPass, name="forgotPass"),

    # path("password_reset/", views.password_reset_request, name="password_reset"),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'), name='password_reset_complete'),      


]
