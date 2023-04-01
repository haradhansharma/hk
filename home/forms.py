from django import forms
from .models import ContactMessage

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        
        
        widgets = {                      
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class':'form-control', 'aria-label':'Name',  }),
            'email': forms.EmailInput(attrs={'placeholder': 'email', 'class':'form-control', 'aria-label':'email' , }),              
            
            'message': forms.Textarea(attrs={'rows':'5','placeholder': 'Message','class':'form-control', 'aria-label':'Message', }), 
        }