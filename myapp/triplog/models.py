from django.db import models
from django.contrib.auth import get_user_model

class Triplog(models.Model):
    
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    title = models.CharField(max_length=55)
    content = models.CharField(max_length=255)
    latitude = models.CharField(max_length=55)
    longitude = models.CharField(max_length=55)
    create_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title