
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home.views import serve_logo, serve_logo_bw, serve_favicon, faq, RobotsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    
    path('logo/', serve_logo, name='logo'),
    path('logobw/', serve_logo_bw, name='logobw'),    
    path('favicon/', serve_favicon, name='favicon'),
    path("robots.txt", RobotsView.as_view(), name='robot'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    
