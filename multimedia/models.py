from django.db import models

# Create your models here.
class Media(models.Model):
    name = models.CharField(max_length=100)
    media = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name