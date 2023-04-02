from django.contrib import admin
from .models import *

admin.site.register(Workshop)
# admin.site.register(ContactMessage)
admin.site.register(FAQ)
admin.site.register(TermsPrivacySection)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'interest_in', 'created_at' )  
    list_filter = ('interest_in', 'in_workshops' )
    search_fields = ('name', 'email', 'interest_in', 'in_workshops', 'message' )    
    ordering = ('-created_at',)