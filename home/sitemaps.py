from django.contrib import sitemaps
from django.urls import reverse
from .models import *
from django.conf import settings

   


class MySitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home:home','home:contact','home:faq','home:terms_privacy', ] 
        
        
    def location(self, item):
        return reverse(item)      
    


    

               
    