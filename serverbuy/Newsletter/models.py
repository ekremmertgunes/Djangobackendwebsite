from django.db import models
class NewsletterUser(models.Model):
    email=models.EmailField(max_length=50)
    date_added=models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.email
        

