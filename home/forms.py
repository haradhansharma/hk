from django import forms
from .models import ContactMessage

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'interest_in', 'in_workshops', 'message']
        
        
        widgets = {                      
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class':'form-control', 'aria-label':'Name',  }),
            'email': forms.EmailInput(attrs={'placeholder': 'email', 'class':'form-control', 'aria-label':'email' , }),    
            'interest_in' : forms.Select(attrs={ 'class':'form-select', 'aria-label':'Interested In', 'placeholder':'Select Related Question' }),           
            'in_workshops' : forms.SelectMultiple(attrs={ 'class':'form-select', 'aria-label':'In Wrkshops', 'size': 4 }),             
            'message': forms.Textarea(attrs={'rows':'5','placeholder': 'Message','class':'form-control', 'aria-label':'Message', }), 
        }