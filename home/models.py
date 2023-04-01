from django.db import models

class Workshop(models.Model):
    name = models.CharField(max_length=255)
    featured_image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.email})'
    
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
    
class TermsPrivacySection(models.Model):
    TYPE_CHOICES = (
        ('terms', 'Terms'),
        ('privacy', 'Privacy'),
    )
    sec_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    heading = models.CharField(max_length=255)
    s_order = models.IntegerField(default=0)
    description = models.TextField()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading
