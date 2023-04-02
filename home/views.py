from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Workshop, FAQ
from django.conf.urls.static import static
import os
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from .models import ContactMessage, TermsPrivacySection
from .forms import ContactUsForm
from django.contrib import messages
from django.core.mail import send_mail
from .helper import custom_send_mail

def serve_favicon(request):
    logo_path = os.path.join(settings.MEDIA_ROOT, 'favicon.ico')
    with open(logo_path, 'rb') as f:
        logo_data = f.read()
    return HttpResponse(logo_data, content_type='image/ico')


def serve_logo(request):
    logo_path = os.path.join(settings.MEDIA_ROOT, 'logo.png')
    with open(logo_path, 'rb') as f:
        logo_data = f.read()
    return HttpResponse(logo_data, content_type='image/png')

def serve_logo_bw(request):
    logo_path = os.path.join(settings.MEDIA_ROOT, 'logobw.png')
    with open(logo_path, 'rb') as f:
        logo_data = f.read()
    return HttpResponse(logo_data, content_type='image/png')

class HomePageView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        context['organization_acronym'] = '<span class="fl">H</span>ASE<span class="fl">K</span>USE'
        context['organization_name_clean'] = 'Harmony Association For Spiritual Empowerment And Knowledge Of Universal Serenity'
        context['organization_name'] = '<span class="text-spurple">H</span>armony <span class="text-spurple">A</span>ssociation for <span class="text-spurple">S</span>piritual <span class="text-spurple">E</span>mpowerment and <span class="text-spurple">K</span>nowledge of <span class="text-spurple">U</span>niversal <span class="text-spurple">Se</span>renity'
        context['organization_mission'] = "At the Harmony Association for Spiritual Empowerment and Knowledge of Universal Serenity, we are committed to promoting peace, spiritual growth, and harmonious coexistence among people of all nations and cultures. We strive to achieve this through various means such as yoga and meditation practices, as well as drawing inspiration from the ancient principles of Hinduism and its texts. Our ultimate goal is to help individuals reach their fullest potential and live a fulfilling life while contributing to the greater good of society."
        context['organization_vision'] = "Our vision is to create a world where individuals are empowered to live a life of inner peace and harmony, leading to a global society of peaceful coexistence. We envision a future where people from all walks of life can come together to practice yoga and meditation, leading to personal and collective growth. We believe that the principles of Hinduism, as taught by Adi Shankaracharya, can provide a framework for a more harmonious world, and we aim to spread these teachings to as many people as possible."
     
        context['workshops'] = Workshop.objects.all()
        context['form'] = ContactUsForm()
        # context['contact_info'] = '123 Main St, Anytown USA\ninfo@gitaorganization.com'
        
        context['meta_title'] = 'Home'
        context['meta_description'] = 'The Harmony Association for Spiritual Empowerment and Knowledge of Universal Serenity (HASEKUSE) is a non-profit organization dedicated to promoting peace, spiritual growth, and harmonious coexistence among people of all nations and cultures.'
        
        context['og_image'] = self.request.build_absolute_uri(reverse('logo'))
        
        
        
        
        
        return context
    
    


class ContactMessageCreateView(CreateView):
    model = ContactMessage
    # fields = ['name', 'email', 'message']
    form_class = ContactUsForm
    success_url = reverse_lazy('home:home')
    
    def form_valid(self, form):
        # Save the form data
        form.save()

        # Set a success message to be displayed to the user
        messages.success(self.request, 'Your message has been sent. We will get back to you soon.')
        in_workshops_list = "\n".join([f"- {ws.name}" for ws in form.cleaned_data['in_workshops']])
        # Send email to the site admin
        subject = f'HASEKUSE:-New contact form submission in {form.cleaned_data["interest_in"]}'
        message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nInWorkshop:\n {in_workshops_list}\n\nMessage: {form.cleaned_data['message']}"
        reply_to = [form.cleaned_data['email']]
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [a[1] for a in settings.ADMINS] 
        custom_send_mail(subject, message, from_email, recipient_list, reply_to = reply_to,  fail_silently=True)


        # Redirect to the success URL
        return super().form_valid(form)

    def form_invalid(self, form):
        # Set an error message to be displayed to the user
        messages.error(self.request, 'There was an error with your submission. Please try again.')

        # Render the template with the invalid form
        return self.render_to_response(self.get_context_data(form=form))
    
    
    
    
def faq(request):
    context = {}
    faqs = FAQ.objects.all()
    context['organization_name_clean'] = 'Harmony Association For Spiritual Empowerment And Knowledge Of Universal Serenity'    
    context['meta_title'] = 'Frequently Asked Questions'
    context['faqs'] = faqs
    context['og_image'] = request.build_absolute_uri(reverse('logo'))
    

    return render(request, 'home/faq.html', context = context )


def terms_privacy(request):
    clauses = TermsPrivacySection.objects.all().order_by('s_order')
    context = {}
    context['organization_name_clean'] = 'Harmony Association For Spiritual Empowerment And Knowledge Of Universal Serenity'    
    context['meta_title'] = 'Terms and Privacy Policy'
    context['clauses'] = clauses
    context['og_image'] = request.build_absolute_uri(reverse('logo'))
    
    
    return render(request, 'home/terms_and_service.html', context = context)



class RobotsView(TemplateView):
    template_name = "robots.txt"
    content_type = "text/plain"


    
