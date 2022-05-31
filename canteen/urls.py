from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views # ANCHOR: Import It


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food.urls')),

    # path('accounts/', include('django.contrib.auth.urls')),

    
    # path("password_reset/", views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),      

    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
