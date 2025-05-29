from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/register/', register, name='register'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 