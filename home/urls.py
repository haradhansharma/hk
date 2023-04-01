from django.urls import path
from .views import HomePageView, ContactMessageCreateView, serve_logo, serve_logo_bw, serve_favicon, faq, terms_privacy
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *

app_name = 'home'

sitemap_list = {
    'static': MySitemap,
    
}
urlpatterns = [
    
    
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactMessageCreateView.as_view(), name='contact'),
    # path('contact-success/', contact_success, name='contact_success'),
    path('faq/', faq, name='faq'),
    path('terms-and-privacy/', terms_privacy, name='terms_privacy'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemap_list}, name='django.contrib.sitemaps.views.sitemap'),      
    
    
]