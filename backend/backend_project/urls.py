from django.contrib import admin
from django.urls import path, include
from women import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'), 
    path('admin/', admin.site.urls),
    path('women/', include('women.urls')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)